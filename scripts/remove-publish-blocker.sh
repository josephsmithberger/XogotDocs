#!/bin/bash

set -euo pipefail

# Check for required argument
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <document-root>"
  exit 1
fi

DOC_ROOT="$1"
DOC_ROOT="${DOC_ROOT%/}"  # Remove trailing slash if present

# Define the marker line to remove
MARKER="<!-- Remove this line to publish to docs.xogot.com -->"

# Read each line of the CSV
while IFS= read -r rel_path; do
  # Skip blank lines
  [[ -z "$rel_path" ]] && continue

  # Remove leading ./ from CSV path if present
  rel_path="${rel_path#./}"

  # Construct absolute path to file
  filepath="$DOC_ROOT/$rel_path"

  if [[ ! -f "$filepath" ]]; then
    echo "File not found: $filepath"
    continue
  fi

  # Check if first line matches marker
  if head -n 1 "$filepath" | grep -Fxq "$MARKER"; then
    echo "Removing marker from: $filepath"
    tail -n +2 "$filepath" > "$filepath.tmp" && mv "$filepath.tmp" "$filepath"
  fi
done < publish.csv
