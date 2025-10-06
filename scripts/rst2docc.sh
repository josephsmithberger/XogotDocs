#!/bin/bash

# Usage: ./convert_rst_to_docc.sh <source_directory> <output_directory>
# Example: ./convert_rst_to_docc.sh ./rst_docs ./MyDocumentation.docc

set -e

SRC_DIR="$1"
OUT_DIR="$2/Documentation"

if [ -z "$SRC_DIR" ] || [ -z "$OUT_DIR" ]; then
  echo "Usage: $0 <source_directory> <output_directory>"
  exit 1
fi

if ! command -v pandoc &> /dev/null; then
  echo "Error: pandoc is not installed. Install it with 'brew install pandoc'."
  exit 1
fi

mkdir -p "$OUT_DIR"

echo "Converting .rst files in $SRC_DIR to DocC-compatible Markdown in $OUT_DIR..."

for rst_file in "$SRC_DIR"/*.rst; do
  [ -e "$rst_file" ] || continue
  
  filename=$(basename -- "$rst_file")
  filename_no_ext="${filename%.rst}"
  md_file="$OUT_DIR/$filename_no_ext.md"

  echo "Processing $filename..."

  # Convert .rst to markdown
  pandoc "$rst_file" -f rst -t gfm -o "$md_file.tmp"

  # Add DocC metadata header - Using tr for capitalization instead of ${var^}
  first_char=$(echo "$filename_no_ext" | cut -c1 | tr '[:lower:]' '[:upper:]')
  rest_chars=$(echo "$filename_no_ext" | cut -c2-)
  title="$first_char$rest_chars"
  
  cat <<EOF > "$md_file"
---
kind: article
title: $title
---

EOF
  
  # Append the converted content
  cat "$md_file.tmp" >> "$md_file"
  rm "$md_file.tmp"

echo "Generated $md_file"
done

echo "✅ All files converted successfully. The DocC articles are in $OUT_DIR."

# Optional: Provide basic DocC catalog structure
echo "\n🔧 Setting up basic DocC catalog structure..."
mkdir -p "$2/Resources"
echo "{
  \"documentation\": {
    \"topics\": []
  }
}" > "$2/documentation.doccindex"

echo "📚 DocC catalog ready at $2"
