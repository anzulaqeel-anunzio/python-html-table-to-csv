# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from converter.core import HtmlToCsvConverter

def main():
    parser = argparse.ArgumentParser(description="HTML Table to CSV Converter")
    parser.add_argument("file", help="Input HTML file")
    parser.add_argument("--index", "-i", type=int, help="Extract specific table index (0-based)")
    parser.add_argument("--output", "-o", help="Output CSV file (if multiple tables, appends index)")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    csv_tables = HtmlToCsvConverter.get_tables_as_csv(html_content)
    
    if not csv_tables:
        print("No tables found in the HTML file.")
        sys.exit(0)

    # Filter by index if requested
    if args.index is not None:
        if 0 <= args.index < len(csv_tables):
            csv_tables = [csv_tables[args.index]]
        else:
            print(f"Error: Table index {args.index} out of range (Found {len(csv_tables)} tables).")
            sys.exit(1)

    # Output
    for i, csv_data in enumerate(csv_tables):
        header = f"--- Table {i} ---"
        if args.output:
            # Determine filename
            filename = args.output
            if len(csv_tables) > 1 and args.index is None:
                # Append index to filename if dumping all tables
                base, ext = os.path.splitext(filename)
                filename = f"{base}_{i}{ext}"
            
            try:
                with open(filename, 'w', encoding='utf-8', newline='') as f:
                    f.write(csv_data)
                print(f"Saved: {filename}")
            except Exception as e:
                print(f"Error writing output {filename}: {e}")
        else:
            print(header)
            print(csv_data)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
