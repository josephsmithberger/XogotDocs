#!/usr/bin/env python3

"""
This script recursively scans directories for index.rst files, extracts toctree elements,
and converts them to a single consolidated DocC-formatted table of contents file.

Usage:
    python3 generate_docc_toc.py <source_directory> [output_file]

Example:
    python3 generate_docc_toc.py /path/to/godot/docs [/path/to/output/documentation.md]

The script will:
1. Find all index.rst files in the source directory and its subdirectories
2. Extract toctree elements from each index.rst
3. Convert the toctree entries to DocC-format links
4. Create a single consolidated documentation.md file with all TOCs organized by directory
   (with each directory as a level-3 header, sorted alphabetically)
"""

import os
import sys
import re


def extract_title_from_index(index_content):
    """Extract the title from an index.rst file."""
    # Look for the first line followed by a line of equal signs (=)
    lines = index_content.split("\n")
    for i in range(len(lines) - 1):
        if lines[i].strip() and i < len(lines) - 1 and all(c == '=' for c in lines[i+1].strip()) and lines[i+1].strip():
            return lines[i].strip()
    
    # Fallback: Use the directory name
    return None


def extract_toctree_sections(index_content):
    """
    Extract multiple toctree sections from an index.rst file.
    Returns a list of (section_title, entries) tuples.
    Each section has a title (heading above the toctree) and a list of entries.
    """
    sections = []
    main_title = extract_title_from_index(index_content)
    
    # Split the content into lines for processing
    lines = index_content.split('\n')
    
    # Find all headings (lines followed by underlines of - or =)
    headings = {}
    for i in range(len(lines) - 1):
        if lines[i].strip() and i < len(lines) - 1:
            # Check if the next line is an underline of = or -
            if all(c == '=' for c in lines[i+1].strip()) and lines[i+1].strip():
                headings[i] = (lines[i].strip(), "main")
            elif all(c == '-' for c in lines[i+1].strip()) and lines[i+1].strip():
                headings[i] = (lines[i].strip(), "section")
    
    # Regular expression to find toctree directive and its content
    toctree_pattern = re.compile(r"\.\.[\s]+toctree::(.*?)(?=\.\.[\s]+|$)", re.DOTALL)
    
    # Find all toctree blocks with their line positions
    toctree_blocks = []
    for match in toctree_pattern.finditer(index_content):
        start_pos = index_content[:match.start()].count('\n')
        toctree_content = match.group(1)
        
        # Extract entries from this toctree
        entries = []
        for line in toctree_content.strip().split('\n'):
            lline = line
            line = line.strip()
            if not line or line.startswith(':'):
                continue
            if lline == line:
                continue  # Skip lines that are not indented
            entries.append(line)
        
        if entries:  # Only add if there are entries
            toctree_blocks.append((start_pos, entries))
    
    # For each toctree block, find the nearest heading above it
    for toc_pos, entries in toctree_blocks:
        nearest_heading = None
        nearest_distance = float('inf')
        
        for heading_pos, (heading_text, heading_type) in headings.items():
            if heading_pos < toc_pos and toc_pos - heading_pos < nearest_distance:
                nearest_distance = toc_pos - heading_pos
                nearest_heading = heading_text
        
        # Use nearest heading or fall back to main title
        section_title = nearest_heading or main_title
        
        # For non-main headings, prefix with main title if available
        if nearest_heading and nearest_heading != main_title and main_title:
            section_title = f"{main_title} - {section_title}"
            
        sections.append((section_title, entries))
    
    return sections


def extract_toctree(index_content):
    """
    Extract all toctree entries from an index.rst file, flattened into a single list.
    Returns a list of entries. This is kept for backward compatibility.
    """
    entries = []
    
    # Use the new function and flatten the results
    sections = extract_toctree_sections(index_content)
    for _, section_entries in sections:
        entries.extend(section_entries)
    
    return entries


def process_directory(directory_path, root_path, toc_collection):
    """
    Process a directory: look for index.rst, extract toctree sections, and add to the TOC collection.
    
    Args:
        directory_path: Path to the directory to process
        root_path: The base directory path for calculating relative paths
        toc_collection: Dictionary to collect TOC data {relative_path: [(section_title, entries), ...]}
    """
    index_path = os.path.join(directory_path, "index.rst")
    
    # Skip if there's no index.rst
    if not os.path.exists(index_path):
        return
    
    print(f"Processing {index_path}")
    
    # Read the index.rst file
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()
    
    # Extract toctree sections (each section has a title and entries)
    sections = extract_toctree_sections(index_content)
    
    # Skip if no sections found
    if not sections:
        print(f"  No toctree sections found in {index_path}")
        return
    
    # Get relative path from root
    rel_path = os.path.relpath(directory_path, root_path)
    if rel_path == ".":
        # For the root directory, use a special name
        base_name = "Root"
    else:
        # Use the directory name or the extracted title
        main_title = extract_title_from_index(index_content)
        base_name = main_title or os.path.basename(directory_path)
    
    # Add to collection with the relative path as key for sorting
    toc_collection[rel_path] = (base_name, sections)
    
    total_entries = sum(len(entries) for _, entries in sections)
    print(f"  Found {len(sections)} section(s) with {total_entries} total entries in '{base_name}'")


def scan_directories(root_path, base_path, toc_collection):
    """
    Recursively scan directories for index.rst files and collect TOC information.
    
    Args:
        root_path: Directory to scan (changes during recursion)
        base_path: Base directory path for calculating relative paths (stays constant)
        toc_collection: Dictionary to collect TOC data {relative_path: (base_name, [(section_title, entries), ...])}
    """
    # Process the current directory first
    process_directory(root_path, base_path, toc_collection)
    
    # Recursively process subdirectories
    for item in os.listdir(root_path):
        item_path = os.path.join(root_path, item)
        if os.path.isdir(item_path):
            scan_directories(item_path, base_path, toc_collection)


def create_consolidated_toc(toc_collection, output_path):
    """
    Create a consolidated DocC-formatted table of contents markdown file.
    
    Args:
        toc_collection: Dictionary with TOC data {relative_path: (base_name, [(section_title, entries), ...])}
        output_path: Path to write the output file
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Documentation\n\n")
        
        # Sort sections alphabetically by relative path
        for rel_path in sorted(toc_collection.keys()):
            base_name, sections = toc_collection[rel_path]
            
            # Write main directory header
            f.write(f"## {base_name}\n\n")
            
            # Write each section with its entries
            for section_idx, (section_title, entries) in enumerate(sections):
                # If there's only one section with the same title as base_name, don't repeat the header
                # if len(sections) == 1 and section_title == base_name:
                #     # Just write entries without a subheader
                #     for entry in entries:
                #         f.write(f"- <doc:{entry}>\n")
                # else:
                    # Write section subheader
                    display_title = section_title
                    
                    f.write(f"### {display_title}\n\n")
                    
                    # Write entries
                    for entry in entries:
                        f.write(f"- <doc:{entry}>\n")
                    
                    # Add space between subsections if not the last one
                    if section_idx < len(sections) - 1:
                        f.write("\n")
            
            # Add space between main sections
            f.write("\n")
    
    # Count total sections and entries for summary
    total_sections = sum(len(sections) for _, sections in toc_collection.values())
    total_entries = sum(sum(len(entries) for _, entries in sections) for _, sections in toc_collection.values())
    
    print(f"Created consolidated TOC at {output_path} with {len(toc_collection)} directories, {total_sections} sections, and {total_entries} total entries")


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python3 generate_docc_toc.py <source_directory> [output_file]")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    
    # Determine output file path
    if len(sys.argv) == 3:
        output_file = sys.argv[2]
    else:
        output_file = os.path.join(os.path.dirname(source_dir), "documentation.md")
    
    if not os.path.isdir(source_dir):
        print(f"Error: {source_dir} is not a valid directory")
        sys.exit(1)
    
    print(f"Scanning {source_dir} for index.rst files...")
    
    # Dictionary to collect all TOC entries
    toc_collection = {}
    
    # Scan all directories and collect TOC entries
    scan_directories(source_dir, source_dir, toc_collection)
    
    # Create the consolidated TOC file
    create_consolidated_toc(toc_collection, output_file)
    
    print(f"Done! Consolidated TOC written to {output_file}")


if __name__ == "__main__":
    main()
