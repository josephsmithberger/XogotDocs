#!/usr/bin/env python3
"""
Fix broken web URL links in .md and .tutorial files inside the .docc folder.

Only processes links pointing to docs.godotengine.org. All other URLs are
left untouched. Does NOT touch <doc:...> DocC links.

Strategy for each link:
  1. Skip if not a docs.godotengine.org URL.
  2. Fetch the URL; skip if it is NOT a 404 (including soft-404s detected via
     the ReadTheDocs <meta name="readthedocs-http-status"> tag).
  3. For broken links, derive the equivalent live Godot Docs page for the
     current file using path mappings:
       Manual/    -> tutorials/
       Tutorials/ -> getting_started/
  4. Fetch that live page and extract all <a> href links, resolving relative
     URLs (e.g. ../../classes/foo.html) against the page base.
  5. Match the broken link's display text (lowercased, backtick-stripped)
     against the scraped link texts to find the correct URL.
  6. If a match is found, replace the broken URL with the live page's version.
  7. Flag anything still unresolved for manual review at the end.
"""

import re
import ssl
import sys
import urllib.request
import urllib.error
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path
from collections import defaultdict

from tqdm import tqdm

# ---------------------------------------------------------------------------
# SSL context
# ---------------------------------------------------------------------------
_SSL_CTX = ssl.create_default_context()
_SSL_CTX.check_hostname = False
_SSL_CTX.verify_mode = ssl.CERT_NONE

GODOT_BASE = 'https://docs.godotengine.org/en/stable'

# ---------------------------------------------------------------------------
# Path mapping: docc subdir -> Godot Docs subdir
# ---------------------------------------------------------------------------
PATH_MAP = {
    'Manual':    'tutorials',
    'Tutorials': 'getting_started',
}

# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------
# Captures: [1]=open bracket+text, [2]=link text, [3]='](' [4]=URL, [5]=')'
LINK_RE = re.compile(r'(\[)([^\]]+)(\]\()(https?://[^)]+)(\))')
URL_RE = LINK_RE  # alias used in URL counting
_RTD_STATUS_RE = re.compile(
    r'<meta\s+name="readthedocs-http-status"\s+content="(\d+)"',
    re.IGNORECASE,
)

# Member types, longest-first so 'private_method' beats 'method'
_MEMBER_TYPES = ('private_method', 'property', 'method', 'constant', 'signal', 'annotation')
_MEMBER_TYPE_PAT = '|'.join(_MEMBER_TYPES)
_MEMBER_SLUG_RE = re.compile(
    r'/classes/(.+?)(?:\.html)?(?:#.*)?$', re.IGNORECASE
)

# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------
_url_status_cache: dict[str, int | None] = {}
_page_links_cache: dict[str, dict[str, str]] = {}  # page_url -> {norm_text: full_url}
_verbose = False


# ---------------------------------------------------------------------------
# URL slug extraction (fallback when text match fails)
# ---------------------------------------------------------------------------
def _extract_member_slug(url: str) -> str | None:
    """
    From a broken class-member URL, extract the normalised member slug.

    e.g. .../classes/class_projectsettings_property_physics/common/physics_ticks_per_second.html
         -> 'physics-common-physics-ticks-per-second'
    """
    m = _MEMBER_SLUG_RE.search(url)
    if not m:
        return None
    # Collapse any slashes in the path into underscores for uniform parsing
    path = m.group(1).replace('/', '_')
    # Find the member-type keyword and take everything after it
    type_m = re.search(r'_(' + _MEMBER_TYPE_PAT + r')_(.+)$', path, re.IGNORECASE)
    if not type_m:
        return None
    member = type_m.group(2)
    return member.replace('_', '-')


# ---------------------------------------------------------------------------
# HTML link extractor
# ---------------------------------------------------------------------------
def _norm_text(text: str) -> str:
    """Normalize link text for comparison: lowercase, strip whitespace/backticks."""
    return text.strip().strip('`').lower()


class LinkExtractor(HTMLParser):
    def __init__(self, page_url: str):
        super().__init__()
        self.page_url = page_url
        self.links: dict[str, str] = {}  # norm_text -> actual_url (no fragment)
        self._current_href: str | None = None
        self._current_text: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href = dict(attrs).get('href', '')
            if href:
                # Resolve relative URLs (e.g. ../../classes/foo.html) against the page
                href = urllib.parse.urljoin(self.page_url, href)
            if href.startswith('http'):
                self._current_href = href  # preserve fragment
            else:
                self._current_href = None
            self._current_text = []

    def handle_data(self, data):
        if self._current_href is not None:
            self._current_text.append(data)

    def handle_endtag(self, tag):
        if tag == 'a' and self._current_href:
            text = _norm_text(''.join(self._current_text))
            if text:
                self.links[text] = self._current_href
            self._current_href = None
            self._current_text = []


# ---------------------------------------------------------------------------
# Networking helpers
# ---------------------------------------------------------------------------
def _get(url: str, timeout: int = 10) -> tuple[int, str]:
    """Fetch url, return (effective_status, body_text)."""
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=_SSL_CTX) as resp:
            status = resp.status
            body = resp.read().decode('utf-8', errors='ignore')
            if status == 200:
                m = _RTD_STATUS_RE.search(body)
                if m:
                    status = int(m.group(1))
            return status, body
    except urllib.error.HTTPError as e:
        return e.code, ''
    except Exception as e:
        if _verbose:
            tqdm.write(f'    ERROR fetching {url}: {type(e).__name__}: {e}')
        return -1, ''


def fetch_status(url: str) -> int | None:
    bare = url.split('#')[0]
    if bare in _url_status_cache:
        return _url_status_cache[bare]
    status, _ = _get(bare)
    result = status if status > 0 else None
    _url_status_cache[bare] = result
    return result


def fetch_page_links(page_url: str) -> dict[str, str]:
    """Return {norm_url: actual_url} for all hrefs on page_url."""
    if page_url in _page_links_cache:
        return _page_links_cache[page_url]

    status, body = _get(page_url)
    if status != 200:
        if _verbose:
            tqdm.write(f'    Could not fetch Godot page ({status}): {page_url}')
        _page_links_cache[page_url] = {}
        return {}

    extractor = LinkExtractor(page_url)
    extractor.feed(body)
    _page_links_cache[page_url] = extractor.links

    if _verbose:
        tqdm.write(f'    Fetched {len(extractor.links)} links from {page_url}')

    return extractor.links


# ---------------------------------------------------------------------------
# Path mapping
# ---------------------------------------------------------------------------
def godot_url_for(file_path: Path, docc_root: Path) -> str | None:
    """Derive the equivalent Godot Docs URL for a given XogotDocs file."""
    try:
        rel = file_path.relative_to(docc_root)
    except ValueError:
        return None

    parts = rel.parts
    if not parts:
        return None

    top = parts[0]
    if top not in PATH_MAP:
        return None

    godot_subdir = PATH_MAP[top]
    rest = '/'.join(parts[1:])
    rest_html = re.sub(r'\.(md|tutorial)$', '.html', rest)

    return f'{GODOT_BASE}/{godot_subdir}/{rest_html}'


# ---------------------------------------------------------------------------
# Per-file processing
# ---------------------------------------------------------------------------
def process_file(
    path: Path,
    docc_root: Path,
    url_bar: tqdm,
    dry_run: bool = False,
) -> tuple[bool, list[str]]:
    original = path.read_text(encoding='utf-8')
    changed = False
    still_broken: list[str] = []

    # Derive the live Godot Docs page for this file (fetched lazily)
    godot_page_url = godot_url_for(path, docc_root)
    page_links: dict[str, str] | None = None  # loaded on first 404

    def maybe_fix(match: re.Match) -> str:
        nonlocal changed, page_links

        open_bracket  = match.group(1)   # [
        link_text     = match.group(2)   # visible text
        mid_bracket   = match.group(3)   # ](
        url           = match.group(4)   # URL
        close_bracket = match.group(5)   # )

        url_bar.update(1)

        # Only process Godot docs links
        if 'docs.godotengine.org' not in url:
            return match.group(0)

        status = fetch_status(url)

        if _verbose:
            tqdm.write(f'    {status}  [{link_text}]({url})')

        if status != 404:
            return match.group(0)

        # Lazy-load the live Godot Docs page links
        if page_links is None:
            if godot_page_url:
                if _verbose:
                    tqdm.write(f'  Fetching live page: {godot_page_url}')
                page_links = fetch_page_links(godot_page_url)
            else:
                page_links = {}

        # Match by link text against links scraped from the live page
        norm_text = _norm_text(link_text)
        correct_url = page_links.get(norm_text)

        if correct_url and correct_url != url:
            changed = True
            if _verbose:
                tqdm.write(f'    FIXED via text "{link_text}": {url} -> {correct_url}')
            return f'{open_bracket}{link_text}{mid_bracket}{correct_url}{close_bracket}'

        # Fallback: match by URL slug against live page anchor fragments.
        # Handles cases where the XogotDocs link text differs slightly from
        # the live page (e.g. "Tick" vs "Ticks").
        slug = _extract_member_slug(url)
        if slug:
            for full_url in page_links.values():
                if '#' in full_url:
                    anchor = full_url.split('#', 1)[1]
                    if anchor.endswith(slug):
                        changed = True
                        if _verbose:
                            tqdm.write(f'    FIXED via slug "{slug}": {url} -> {full_url}')
                        return f'{open_bracket}{link_text}{mid_bracket}{full_url}{close_bracket}'

        # Last resort: try lowercasing the URL and see if it resolves
        lowered = url.lower()
        if lowered != url:
            low_status = fetch_status(lowered)
            if low_status == 200:
                changed = True
                if _verbose:
                    tqdm.write(f'    FIXED via lowercase: {url} -> {lowered}')
                return f'{open_bracket}{link_text}{mid_bracket}{lowered}{close_bracket}'

        # Nothing worked — flag for manual review
        still_broken.append(f'[{link_text}]({url})')
        if _verbose:
            tqdm.write(f'    UNRESOLVED: [{link_text}]({url})')
        return match.group(0)

    updated = LINK_RE.sub(maybe_fix, original)

    if changed and not dry_run:
        path.write_text(updated, encoding='utf-8')

    return changed, still_broken


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    global _verbose
    dry_run = '--dry-run' in sys.argv
    _verbose = '--verbose' in sys.argv or '-v' in sys.argv

    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    docc_dirs = list(project_root.glob('*.docc'))

    if not docc_dirs:
        print('ERROR: No .docc directory found in project root.')
        sys.exit(1)

    # Collect files
    files: list[tuple[Path, Path]] = []  # (file, docc_root)
    for docc_dir in docc_dirs:
        for ext in ('*.md', '*.tutorial'):
            for fp in sorted(docc_dir.rglob(ext)):
                if any(part.startswith('.') for part in fp.parts):
                    continue
                files.append((fp, docc_dir))

    if not files:
        print('No .md or .tutorial files found.')
        sys.exit(0)

    # Count total URLs for the URL progress bar
    tqdm.write(f'Found {len(files)} file(s). Counting URLs...')
    total_urls = 0
    for fp, _ in files:
        text = fp.read_text(encoding='utf-8')
        total_urls += len(LINK_RE.findall(text))
    tqdm.write(f'Found {total_urls} URL reference(s) across all files.\n')

    changed_count = 0
    broken_report: dict[Path, list[str]] = defaultdict(list)

    with tqdm(total=len(files), desc='Files', unit='file', position=0) as file_bar:
        with tqdm(total=total_urls, desc='URLs ', unit='url',  position=1) as url_bar:
            for fp, docc_root in files:
                file_bar.set_postfix_str(fp.name, refresh=True)
                changed, still_broken = process_file(
                    fp, docc_root, url_bar, dry_run=dry_run
                )
                if changed:
                    changed_count += 1
                if still_broken:
                    broken_report[fp].extend(still_broken)
                file_bar.update(1)

    label = 'Would update' if dry_run else 'Updated'
    tqdm.write(f'\n{label} {changed_count} file(s).')

    if broken_report:
        tqdm.write('\nLinks that could not be resolved (manual review needed):')
        for fp, urls in broken_report.items():
            tqdm.write(f'  {fp.relative_to(project_root)}')
            for url in sorted(set(urls)):
                tqdm.write(f'    {url}')


if __name__ == '__main__':
    main()
