#!/usr/bin/env bash
set -euo pipefail

PORT=8000
HOST="127.0.0.1"
SITE_DIR="docs-local"

usage() {
  cat <<'EOF'
Host a previously built Xogot DocC static site locally.

Usage:
  scripts/host-preview-pages.sh [--dir DIR] [--port PORT] [--host HOST]

Options:
  --dir DIR    Directory containing generated static site (default: docs-local)
  --port PORT  Local server port (default: 8000)
  --host HOST  Local bind host (default: 127.0.0.1)
  -h, --help   Show this help text
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dir)
      SITE_DIR="$2"
      shift 2
      ;;
    --port)
      PORT="$2"
      shift 2
      ;;
    --host)
      HOST="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SITE_PATH="$REPO_ROOT/$SITE_DIR"

if [[ ! -d "$SITE_PATH" ]]; then
  echo "Site directory not found: $SITE_PATH" >&2
  echo "Run ./scripts/preview-pages.sh first."
  exit 1
fi

echo "Serving: $SITE_PATH"
echo "Preview URL: http://$HOST:$PORT/documentation/xogot"
exec python3 -m http.server "$PORT" --bind "$HOST" --directory "$SITE_PATH"
