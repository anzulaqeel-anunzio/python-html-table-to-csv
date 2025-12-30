# HTML Table to CSV Converter

Extract data from HTML `<table>` elements and save them as CSV files. A zero-dependency tool using Python's `html.parser`.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Multi-Table Extraction**: Finds all tables in an HTML file.
*   **Selective Extraction**: Specify which table to convert using an index.
*   **Standard CSV**: Outputs compliant CSV format ready for Excel or analysis.

## Usage

```bash
python run_converter.py [file] [options]
```

### Options

*   `--output`, `-o`: Output filename prefix.
*   `--index`, `-i`: Index of the specific table to extract (0-based).

### Examples

**1. Extract All Tables**
```bash
python run_converter.py report.html
```

**2. Extract First Table to File**
```bash
python run_converter.py report.html -i 0 -o data.csv
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
