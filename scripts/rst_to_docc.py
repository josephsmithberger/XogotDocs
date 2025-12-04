#!/usr/bin/env python3

"""
Usage: python3 convert_rst_to_docc.py <source_directory> <output_directory>
Example: python3 convert_rst_to_docc.py ./rst_docs ./MyDocumentation.docc

This script:
- Reads all .rst files in the specified source directory.
- Parses and massages the content to handle deviations from standard reST.
- Converts the content to Markdown suitable for DocC integration without additional directory structure or metadata headers.
- Converts image directives (.. image::) to @Image(source: filename) format for DocC, changing .webp extensions to .png.
- Preserves inline code formatting (``text`` becomes `text`).
- Displays parsing errors on the command line but excludes them from the generated output.
- Outputs only the .md files in the specified output directory.

Dependencies:
- docutils (`pip install docutils`)
- beautifulsoup4 (`pip install beautifulsoup4`)
"""

import os
import sys
import re
from docutils.core import publish_string
from docutils.writers.html5_polyglot import Writer
from bs4 import BeautifulSoup


def convert_images(rst_content):
    """
    Convert .. image:: or .. figure:: directives to @Image(source: ...) format,
    appending alt text if present, and capturing indented caption text as a block.
    Handles multi-line captions correctly and avoids duplicate caption lines.
    Ignores :figclass: and :align: attributes but properly processes :alt: attributes.
    """
    lines = rst_content.splitlines()
    output_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        image_match = re.match(r"^\s*\.\.\s+(image|figure)::\s+(.+)$", line)
        if image_match:
            image_path = os.path.basename(image_match.group(2).strip())
            image_path = image_path.replace(".webp", ".png")
            alt_text = ""
            caption_lines = []
            
            # Look ahead for image attributes and skip them
            j = i + 1
            while j < len(lines) and j < i + 10:  # Look at most 10 lines ahead
                next_line = lines[j].strip()
                
                # Check for alt text
                alt_match = re.match(r"^:alt:\s+(.+)$", next_line)
                if alt_match:
                    alt_text = alt_match.group(1).strip()
                    j += 1
                    continue
                
                # Skip other attribute lines (like :figclass: and :align:)
                if next_line.startswith(':') and ':' in next_line:
                    j += 1
                    continue
                
                # If it's an empty line, we can skip it
                if not next_line:
                    j += 1
                    continue
                
                # If we reach here, we're done with the attributes
                break
            
            # Look ahead for indented caption lines
            while j < len(lines):
                next_line = lines[j]
                if next_line.strip() == "":
                    caption_lines.append("")  # preserve blank lines in caption
                    j += 1
                    continue
                if re.match(r"^\s{2,}\S", next_line):  # At least 2 spaces indentation
                    caption_lines.append(next_line.strip())
                    j += 1
                else:
                    break
            i = j - 1  # Move i to last caption line
            # Remove leading/trailing blank lines in caption
            while caption_lines and caption_lines[0] == "":
                caption_lines.pop(0)
            while caption_lines and caption_lines[-1] == "":
                caption_lines.pop()
            caption = "\n".join(caption_lines)
            image_args = f'source: "{image_path}"'
            if alt_text:
                image_args += f', alt: "{alt_text}"'
            if caption:
                output_lines.append(f"@Image({image_args}) {{{caption}}}")
            else:
                output_lines.append(f"@Image({image_args})")
            output_lines.append("")  # Insert an empty line after the image
        else:
            output_lines.append(line)
        i += 1
    return "\n".join(output_lines)

def process_code_tabs(rst_content):
    """
    Process RST tab directives and code-tab directives.
    - If a tabs directive contains a GDScript code-tab, extract only that tab and format as a code block
    - Discard other language tabs
    - Also converts regular code blocks using ::: to ```
    - Preserves function declarations and code block structure
    - Keeps original indentation in code blocks
    """
    # First, handle the regular code blocks
    rst_content = rst_content.replace(":::", "```")
    
    lines = rst_content.splitlines()
    result_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check for tabs directive
        tabs_match = re.match(r"^\s*\.\.\s+tabs::\s*$", line)
        if tabs_match:
            i += 1  # Move past the tabs line
            found_gdscript_tabs = []  # Store multiple GDScript tabs
            
            # Scan for code tabs
            while i < len(lines):
                line = lines[i]
                
                # Check if we've exited the tabs section (non-indented line that's not a directive)
                if line.strip() and not line.startswith(" ") and not line.startswith(".."):
                    break
                
                # Check for beginning of code-tab
                code_tab_match = re.match(r"^\s*\.\.\s+code-tab::\s+(\w+).*$", line)
                if code_tab_match:
                    language = code_tab_match.group(1).lower()
                    
                    # If we find gdscript, extract its content
                    if language == "gdscript":
                        # Move to the next line after the code-tab directive
                        i += 1
                        gdscript_code = []
                        
                        # Skip empty lines at the beginning
                        while i < len(lines) and not lines[i].strip():
                            gdscript_code.append("")
                            i += 1
                        
                        # Get the base indentation from the first non-empty line (for reference only)
                        base_indent = None
                        if i < len(lines) and lines[i].strip():
                            base_indent = len(lines[i]) - len(lines[i].lstrip())
                        
                        # Extract code lines until we hit a non-indented line or another code-tab
                        while i < len(lines):
                            current_line = lines[i]
                            
                            # Check if we've reached the end of this code tab
                            # End conditions:
                            # 1. Found a new code-tab directive
                            # 2. Found a line that begins with no whitespace (completely unindented),
                            #    but not a new directive starting with ".."
                            if re.match(r"^\s*\.\.\s+code-tab::", current_line) or \
                               (not current_line.startswith(" ") and current_line.strip() and not current_line.strip().startswith("..")):
                                break
                            
                            # Add the line as is (with original indentation)
                            gdscript_code.append(current_line)
                            i += 1
                        
                        # Only add non-empty code blocks
                        if any(line.strip() for line in gdscript_code):
                            found_gdscript_tabs.append(gdscript_code)
                    else:
                        # Skip non-gdscript tab
                        i += 1
                        
                        # Skip all content until we hit a non-indented line or another code-tab
                        while i < len(lines):
                            current_line = lines[i]
                            if re.match(r"^\s*\.\.\s+code-tab::", current_line) or \
                               (not current_line.startswith(" ") and current_line.strip() and not current_line.strip().startswith("..")):
                                break
                            i += 1
                else:
                    # Just move to the next line in the tabs section
                    i += 1
            
            # Add all found GDScript code blocks
            for gdscript_code in found_gdscript_tabs:
                result_lines.append(".. code-block:: gdscript")
                # append gdscript code lines joined with newlines and indented
                gdscript_code = [f"    {line}" for line in gdscript_code]
                # Don't filter out empty lines as they may be important for code formatting
                
                # code_lines = "\n".join(gdscript_code)
                
                # Add the code block to the result
                result_lines.append("")  # Add empty line after code block
                result_lines.extend(gdscript_code)
                result_lines.append("")  # Add empty line after code block
        else:
            result_lines.append(line)
            i += 1
    
    return "\n".join(result_lines)

def preserve_inline_code(rst_content):
    """Preserve inline code formatting by converting ``text`` to `text` without mangling content."""
    inline_code_pattern = re.compile(r"``(.*?)``")
    return inline_code_pattern.sub(lambda m: f"```{m.group(1)}```", rst_content)


def remove_kbd_tags(rst_content):
    """Remove all :kbd: blocks using a greedy substitution, converting :kbd:`...` to `...`."""
    kbd_pattern = re.compile(r":kbd:`(.*?)`", re.DOTALL)
    return kbd_pattern.sub(lambda m: f"```{m.group(1)}```", rst_content)

def retain_multiline_blocks(rst_content):
    """Retain all multi-line blocks that begin with ".." and print them for debugging."""
    block_pattern = re.compile(r"(?ms)(^\s*\.\.\s+.+?::.*?(?:^\s{2,}.+)+)")

    def wrap_block(match):
        block_content = match.group(1)
        print(f"🔍 Retained block:\n{block_content}\n{'=' * 40}")  # Debug print
        return f"""```
{block_content}
```"""

    return block_pattern.sub(wrap_block, rst_content)

def convert_godot_references(rst_content):
    """
    Convert Godot documentation references to appropriate formats:
    - Class references to Markdown links pointing to the Godot documentation
    - Document references to DocC links using data from references.csv
    """
    # First, load the reference mappings from references.csv
    reference_map = {}
    try:
        csv_path = os.path.join(os.path.dirname(__file__), 'references.csv')
        if os.path.exists(csv_path):
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                # Skip the header line
                next(csvfile, None)
                for line in csvfile:
                    if ',' in line and not line.startswith('//'):
                        parts = line.strip().split(',', 2)
                        if len(parts) >= 2:
                            filename = parts[0].strip()
                            ref_id = parts[1].strip()
                            if ref_id:  # Only add if reference ID is not empty
                                reference_map[ref_id] = filename
    except Exception as e:
        print(f"Warning: Error loading references.csv: {e}")
    
    # Handle format: :ref:`MeshInstance3D <class_MeshInstance3D>`
    ref_pattern = re.compile(r":ref:`([^<`]+)\s*<class_([^>`]+)>`")
    
    def replace_ref(match):
        display = match.group(1).strip()
        cls = match.group(2).strip().lower()
        url = f"https://docs.godotengine.org/en/stable/classes/class_{cls}.html#class-{cls}"
        return f"[{display}]({url})"
    
    rst_content = ref_pattern.sub(replace_ref, rst_content)
    
    # Handle format: :ref:`class_AnimationPlayer`
    class_pattern = re.compile(r":ref:`class_([^`]+)`")
    
    def replace_class(match):
        cls = match.group(1).lower()
        url = f"https://docs.godotengine.org/en/stable/classes/class_{cls}.html#class-{cls}"
        return f"[{match.group(1)}]({url})"
    
    rst_content = class_pattern.sub(replace_class, rst_content)
    
    # Handle format: :ref:`doc_introduction_animation`
    doc_pattern = re.compile(r":ref:`doc_([^`]+)`")
    
    def replace_doc(match):
        original_ref = match.group(1)
        doc_ref = f"doc_{original_ref}"
        
        if doc_ref in reference_map:
            # Extract the filename from the CSV value
            ref_value = reference_map[doc_ref]
            # If the value contains a filename with extension, extract just the filename
            if '.' in ref_value:
                # Get the filename without extension
                ref_value = os.path.splitext(ref_value)[0]
            return f"<doc:{ref_value}>"
        else:
            # Try to handle deep links by progressively shortening the reference
            parts = original_ref.split('_')
            
            # Try different prefix lengths until we find a match or run out of options
            for i in range(len(parts) - 1, 0, -1):
                prefix = '_'.join(parts[:i])
                potential_ref = f"doc_{prefix}"
                
                if potential_ref in reference_map:
                    # We found a match!
                    ref_value = reference_map[potential_ref]
                    if '.' in ref_value:
                        ref_value = os.path.splitext(ref_value)[0]
                    
                    # The rest is the section title
                    section_parts = parts[i:]
                    section_id = '-'.join(section_parts)
                    
                    # Initialize the first character of each word to uppercase
                    section_id = '-'.join(part[0].upper() + part[1:] if part else '' for part in section_parts)
                    
                    return f"<doc:{ref_value}#{section_id}>"
            
            # If we still can't find a match, fall back to the original behavior
            print(f"Warning: Reference '{doc_ref}' not found in references.csv.")
            return f"<doc:{original_ref}>"
    
    rst_content = doc_pattern.sub(replace_doc, rst_content)
    
    # Handle format: :ref:`displayed as pre-recorded videos <doc_playing_videos>`
    doc_display_pattern = re.compile(r":ref:`([^<`]+)\s*<doc_([^>`]+)>`")
    
    def replace_doc_display(match):
        # We ignore the display text for DocC links as requested
        original_ref = match.group(2)
        doc_ref = f"doc_{original_ref}"
        
        if doc_ref in reference_map:
            # Extract the filename from the CSV value
            ref_value = reference_map[doc_ref]
            # If the value contains a filename with extension, extract just the filename
            if '.' in ref_value:
                # Get the filename without extension
                ref_value = os.path.splitext(ref_value)[0]
            return f"<doc:{ref_value}>"
        else:
            # Try to handle deep links by progressively shortening the reference
            parts = original_ref.split('_')
            
            # Try different prefix lengths until we find a match or run out of options
            for i in range(len(parts) - 1, 0, -1):
                prefix = '_'.join(parts[:i])
                potential_ref = f"doc_{prefix}"
                
                if potential_ref in reference_map:
                    # We found a match!
                    ref_value = reference_map[potential_ref]
                    if '.' in ref_value:
                        ref_value = os.path.splitext(ref_value)[0]
                    
                    # The rest is the section title
                    section_parts = parts[i:]
                    section_id = '-'.join(section_parts)
                    
                    # Initialize the first character of each word to uppercase
                    section_id = '-'.join(part[0].upper() + part[1:] if part else '' for part in section_parts)
                    
                    return f"<doc:{ref_value}#{section_id}>"
            
            # If we still can't find a match, fall back to the original behavior
            print(f"Warning: Reference '{doc_ref}' not found in references.csv.")
            return f"<doc:{original_ref}>"
    
    rst_content = doc_display_pattern.sub(replace_doc_display, rst_content)
    
    return rst_content

def convert_rst_asides(rst_content):
    """
    Convert RST asides (e.g., .. tip:, .. note:) and their following indented text or same-line text into Markdown blockquotes.
    Handles both indented blocks and single-line asides.
    """
    lines = rst_content.splitlines()
    output = []
    i = 0
    aside_pattern = re.compile(r"^\s*\.\.\s+(tip|note|warning|caution|important|attention|seealso)::(?:\s*(.*))?$", re.IGNORECASE)
    while i < len(lines):
        aside_match = aside_pattern.match(lines[i])
        if aside_match:
            aside_type = aside_match.group(1).capitalize()
            same_line_text = aside_match.group(2) or ""
            output.append(f"> {aside_type}:" + (f" {same_line_text}" if same_line_text else ""))
            i += 1
            # Collect indented lines as blockquote
            while i < len(lines):
                if lines[i].strip() == "":
                    output.append(">")
                    i += 1
                    continue
                indented = re.match(r"^\s{2,}(.*)", lines[i])
                if indented:
                    output.append(f"> {indented.group(1)}")
                    i += 1
                else:
                    break
            output.append("")
        else:
            output.append(lines[i])
            i += 1
    return "\n".join(output)

def rst_to_markdown(rst_content):
    """Convert reStructuredText to Markdown, filtering out error messages from output and applying transformations."""
    # Extract and handle the title - find the first line followed by a line of equal signs
    lines = rst_content.split('\n')
    title = None
    title_index = -1
    
    for i in range(len(lines) - 1):
        if lines[i].strip() and i < len(lines) - 1 and all(c == '=' for c in lines[i+1].strip()) and lines[i+1].strip():
            title = lines[i].strip()
            title_index = i
            break
    
    # If we found a title, remove all content before it
    if title_index > 0:
        # Remove metadata before the title
        rst_content = '\n'.join(lines[title_index:])
    
    rst_content = convert_images(rst_content)
    rst_content = convert_rst_asides(rst_content)
    rst_content = remove_kbd_tags(rst_content)
    #rst_content = preserve_inline_code(rst_content)
    rst_content = process_code_tabs(rst_content)
    #rst_content = retain_multiline_blocks(rst_content)
    writer = Writer()

    try:
        html = publish_string(
            rst_content,
            writer=writer,
            settings_overrides={'report_level': 5, 'halt_level': 6}
        ).decode('utf-8')
    except Exception as e:
        print(f"⚠️ Parsing error (not included in output): {e}")
        html = ""

    # print(html)

    soup = BeautifulSoup(html, 'html.parser')

    # Process HTML formatting tags
    for cite in soup.find_all('cite'):
        if cite.string:  # Only process if there's actual text content
            # Replace the cite tag with a new string containing backticks
            new_text = f"`{cite.string}`"
            cite.replace_with(new_text)
    
    # Process <strong> tags (convert to double-asterisk format)
    for strong in soup.find_all('strong'):
        if strong.string:  # Only process if there's actual text content
            # Replace the strong tag with a new string containing double-asterisks
            new_text = f"**{strong.string}**"
            strong.replace_with(new_text)
    
    # Process span tags with class "docutils literal" (inline code)
    for span in soup.find_all('span', class_='docutils literal'):
        if span.get_text():
            new_text = f"`{span.get_text()}`"
            span.replace_with(new_text)
    
    markdown = []
    # If we extracted a title, add it as the first line with a leading #
    if title:
        markdown.append(f"# {title}")
    
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'ul', 'ol', 'table', 'pre']):
        # Skip the h1 tag if we've already extracted the title
        if tag.name == 'h1' and title:
            continue
        elif tag.name == 'h1':
            markdown.append(f"# {tag.get_text()}")
        elif tag.name == 'h2':
            markdown.append(f"## {tag.get_text()}")
        elif tag.name == 'h3':
            markdown.append(f"### {tag.get_text()}")
        elif tag.name == 'p':
            # Only append <p> if its parent is not an <li>, <th>, or <td>
            if tag.parent.name not in ['li', 'th', 'td']:
                markdown.append(tag.get_text())
        elif tag.name in ['ul', 'ol']:
            for li in tag.find_all('li'):
                prefix = '-' if tag.name == 'ul' else '1.'
                markdown.append(f"{prefix} {li.get_text()}")
        elif tag.name == 'table':
            # Convert HTML table to Markdown table (DocC style)
            rows = tag.find_all('tr')
            if not rows:
                continue
            # Extract header
            header_cells = rows[0].find_all(['th', 'td'])
            header = [cell.get_text(strip=True) for cell in header_cells]
            table_lines = []
            table_lines.append(" | ".join(header))
            table_lines.append(" | ".join(['-' * max(3, len(h)) for h in header]))
            # Extract table body
            for row in rows[1:]:
                columns = row.find_all(['td', 'th'])
                table_lines.append(" | ".join(col.get_text(strip=True) for col in columns))
            markdown.append('\n'.join(table_lines))
        elif tag.name == 'pre':
            markdown.append("""```
{0}
```""".format(tag.get_text()))

    return '\n\n'.join(markdown)


def process_rst_file(rst_path, out_dir):
    """Process a single RST file and convert it to Markdown."""
    filename = os.path.basename(rst_path)
    
    with open(rst_path, 'r', encoding='utf-8') as file:
        rst_content = file.read()

    print(f"Processing {filename}...")
    md_content = rst_to_markdown(rst_content)

    md_content = convert_godot_references(md_content)
    
    # Add the comment at the beginning of the file
    md_content = "<!-- Remove this line to publish to docs.xogot.com -->\n" + md_content
    
    md_path = os.path.join(out_dir, f"{os.path.splitext(filename)[0]}.md")
    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

    print(f"✅ Generated {md_path}")
    return md_path

def process_directory_recursively(src_dir, out_dir, base_dir=None):
    """
    Recursively process all RST files in the source directory and its subdirectories,
    preserving the directory structure in the output directory.
    
    Args:
        src_dir: Source directory containing RST files
        out_dir: Output directory for Markdown files
        base_dir: Base directory for calculating relative paths (defaults to src_dir)
    
    Returns:
        Number of processed files
    """
    if base_dir is None:
        base_dir = src_dir
        
    files_processed = 0
    
    # Process all RST files in the current directory
    for filename in os.listdir(src_dir):
        file_path = os.path.join(src_dir, filename)
        
        # Process only .rst files that are not index.rst
        if os.path.isfile(file_path) and filename.endswith(".rst") and filename != "index.rst":
            # Calculate the relative directory structure
            rel_dir = os.path.relpath(src_dir, base_dir)
            if rel_dir == ".":
                # We're in the base directory
                target_dir = out_dir
            else:
                # We're in a subdirectory, recreate the structure
                target_dir = os.path.join(out_dir, rel_dir)
                
            # Create the target directory if it doesn't exist
            os.makedirs(target_dir, exist_ok=True)
            
            # Process the file
            process_rst_file(file_path, target_dir)
            files_processed += 1
        
        elif os.path.isdir(file_path):
            # Recursively process subdirectories
            files_processed += process_directory_recursively(file_path, out_dir, base_dir)
    
    return files_processed


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 convert_rst_to_docc.py <source_path> <output_directory>")
        print("  <source_path> can be a single .rst file or a directory containing .rst files")
        sys.exit(1)

    src_path, out_dir = sys.argv[1], sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)

    # Check if source is a file or directory
    if os.path.isfile(src_path):
        if not src_path.endswith('.rst'):
            print(f"Error: {src_path} is not an RST file")
            sys.exit(1)
        # Process single file
        md_path = process_rst_file(src_path, out_dir)
        print(f"\n🎉 File processed. The Markdown file is at {md_path}.")
    elif os.path.isdir(src_path):
        # Process directory recursively
        files_processed = process_directory_recursively(src_path, out_dir)
                
        if files_processed == 0:
            print("No .rst files found in the directory or its subdirectories.")
        else:
            print(f"\n🎉 All {files_processed} files processed. The Markdown files are in {out_dir}, preserving the original directory structure.")
    else:
        print(f"Error: {src_path} is not a valid file or directory")
        sys.exit(1)


if __name__ == "__main__":
    main()