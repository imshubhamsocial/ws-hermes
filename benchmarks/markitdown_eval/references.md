# Layer 3 Reference Schemas: Gauntlet G (microsoft/markitdown)

## 1. Upstream Repository & Supported Formats
* **Source**: https://github.com/microsoft/markitdown (Python 3.10–3.14, pip install 'markitdown[all]')
* **Supported Local Formats**: PDF (.pdf), Word (.docx), Excel (.xlsx, .xls), PowerPoint (.pptx), HTML (.html), Text (CSV, JSON, XML), ZIP archives (.zip), EPubs (.epub), Images (EXIF), Audio (EXIF/local transcription).

## 2. Canonical CLI Syntax
* **Direct File-to-File Conversion**: `markitdown output/fixtures/substrate_report.html -o output/ingested/substrate_report.md`
* **Standard Input Pipe Conversion**: `cat output/fixtures/substrate_report.html | markitdown > output/ingested/substrate_report.md`

## 3. Canonical Python API (convert_local Security Pattern)
```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)
result = md.convert_local("output/fixtures/substrate_report.html")
with open("output/ingested/substrate_report.md", "w", encoding="utf-8") as f:
    f.write(result.markdown)
```
