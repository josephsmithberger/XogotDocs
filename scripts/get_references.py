import os
import csv
import re
import sys

def find_title_and_ref(filepath):
    title = None
    ref = None
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Find title (first line underlined with '=')
    for i in range(1, len(lines)):
        if lines[i].strip() and set(lines[i].strip()) == {'='}:
            title = lines[i-1].strip()
            # Search for reference above the title
            for j in range(i-1, -1, -1):
                m = re.match(r'\.\.\s+_([a-zA-Z0-9_\-:]+):', lines[j].strip())
                if m:
                    ref = m.group(1)
                    break
            break
    return title, ref

def main(root_dir, output_csv):
    results = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.rst'):
                filepath = os.path.join(dirpath, filename)
                title, ref = find_title_and_ref(filepath)
                results.append([filename, ref or '', title or ''])
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['filename', 'reference', 'title'])
        writer.writerows(results)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <output.csv>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])