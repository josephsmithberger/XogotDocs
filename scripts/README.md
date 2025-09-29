# XogotDocs Script Collection

This directory contains a collection of scripts for converting Godot documentation (RST format) to DocC format for use in Apple platforms. These scripts should be run in a specific order to generate a complete and properly formatted documentation set.

## Script Execution Order

Follow these steps in order to generate the complete documentation:

### 1. Generate References

```bash
python3 get_references.py <godot_docs_dir> references.csv
```

This script scans the Godot documentation directory and generates a CSV file mapping document IDs to filenames, which is used to correctly process cross-references in the documentation.

### 2. Process Images

```bash
./process_images.sh <source_directory> <target_directory>
```

We prefer to use webp, but docc does not accept webp files.  To work around this, we convert all the 
pngs to webp, and then rename all webp files to have a png extension.

This script handles image conversion by:
- Finding all `img` directories in the source
- Mirroring the directory structure to the target
- Converting PNG images to WebP
- Renaming WebP files to have PNG extension
- Copying all other media as-is

### 3. Convert RST Files to DocC

```bash
python3 rst_to_docc.py <source_directory> <output_directory>
```

This script converts reStructuredText (RST) files to Markdown format compatible with DocC:
- Preserves the directory structure from source to output
- Skips `index.rst` files (they're handled separately)
- Converts RST formatting to Markdown
- Processes special Godot elements like code blocks, asides, and references
- Handles image directives

### 4. Generate Table of Contents

```bash
python3 generate_docc_toc.py <source_directory> [output_file]
```

This script generates a consolidated table of contents by:
- Finding all `index.rst` files in the source directory
- Extracting table of contents entries
- Creating a single Markdown file with all tables of contents organized by directory

**Important**: The generated `documentation.md` file should be integrated into the existing documentation.md file in the root of your DocC project. You may need to manually merge this file with any existing content to maintain your documentation structure.

### 5. Remove the publish blocker from articles that are to be published

```bash
./remove-publish-blocker.sh <output_directory>
```

This script iterates the list of files in publish.csv and, if the first line of the file is 
<!-- Remove this line to publish to docs.xogot.com -->
It will remove that line.  This step is deferred to a separate script to simplify keeping Xogot docs in sync with the Godot manual.

## Requirements

- Python 3.6+
- BeautifulSoup4 (`pip install beautifulsoup4`)
- Docutils (`pip install docutils`)
- ImageMagick (for image processing)

## Workflow Example

```bash
# 1. Generate references
python3 get_references.py ~/GitHub/godot-docs references.csv

# 2. Process images (if needed)
./process_images.sh ~/GitHub/godot-docs/tutorials ~/GitHub/XogotDocs/Documentation.docc/Manual

# 3. Convert RST files to DocC format
python3 rst_to_docc.py ~/GitHub/godot-docs/tutorials ~/GitHub/XogotDocs/Documentation.docc/Manual

# 4. Generate table of contents
python3 generate_docc_toc.py ~/GitHub/godot-docs/tutorials ~/GitHub/XogotDocs/Documentation.docc/documentation.md
```

# 5. Remove the publish blocker from articles that are to be published
./remove-publish-blocker.sh ~/GitHub/XogotDocs/Documentation.docc/Manual                               
```

After completing these steps, review and integrate the generated table of contents into your main DocC documentation.md file.
