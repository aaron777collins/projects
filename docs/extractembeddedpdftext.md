# extractembeddedpdftext

## 🔗 Quick Links

- [View on GitHub](https://github.com/aaron777collins/extractembeddedpdftext)
- [Latest Release: v1.0.0](https://github.com/aaron777collins/extractembeddedpdftext/releases/tag/v1.0.0) (January 21, 2026)

## 📊 Project Details

- **Primary Language:** Python
- **Languages Used:** Python, C, PowerShell, Go Template, Shell, HTML
- **License:** MIT License
- **Created:** January 21, 2026
- **Last Updated:** January 21, 2026

## 📝 About

# extractembeddedpdftext

A simple Python tool to extract embedded text from PDF files. **No OCR** - extracts only the actual text embedded in the PDF.

## Features

- Fast text extraction using PyMuPDF (fitz)
- Cross-platform: Windows and Linux binaries included
- Simple command-line interface
- Can output to file or stdout

## Download Binaries

Grab the pre-compiled binary for your platform from the [Releases](https://github.com/aaron777collins/extractembeddedpdftext/releases) page.

- **Windows**: `extract_pdf_text.exe`
- **Linux**: `extract_pdf_text`

## Usage

```bash
# Extract text to <pdf>.txt
extract_pdf_text document.pdf

# Extract to specific output file
extract_pdf_text document.pdf -o output.txt

# Print to stdout
extract_pdf_text document.pdf --stdout
```

## Building from Source

```bash
# Install dependencies
pip install -r requirements.txt

# Run directly
python extract_pdf_text.py document.pdf
```

## Compilation

### Linux
```bash
pip install pyinstaller
pyinstaller --onefile --name extract_pdf_text extract_pdf_text.py
```

### Windows (PowerShell)
```powershell
pip install pyinstaller
pyinstaller --onefile --name extract_pdf_text extract_pdf_text.py
```

## Requirements

- Python 3.8+
- PyMuPDF 1.24.12

## License

MIT

