---
name: markitdown
description: "Convert multi-modal files (PDF, DOCX, XLSX, PPTX, HTML, CSV, JSON, XML, ZIP, EPUB, Images, Audio) to clean GitHub-Flavored Markdown (GFM) using Microsoft MarkItDown. Supports offline conversion via CLI (markitdown <input> -o <output.md>) and Python API (MarkItDown(enable_plugins=False).convert_local(path))."
---

# markitdown: Multi-Modal Document to Markdown Ingestion

Convert multi-format documents and data files into clean, token-efficient GitHub-Flavored Markdown (GFM) preserving tables, headings, and lists.

## Hard Rules
1. **100% Offline Local Conversion**: Never configure Azure Document Intelligence (docintel_endpoint) or Azure Content Understanding (--use-cu). Run 100% locally.
2. **Plugins Disabled**: Always instantiate MarkItDown(enable_plugins=False) and avoid --use-plugins unless authorized.
3. **Local File Restriction**: In Python, always call md.convert_local(filepath) to avoid SSRF or remote URL fetching.
4. **Working Context Discipline**: Inspect converted .md selectively rather than dumping full multi-megabyte files into active context.

## CLI Usage
```bash
# Convert a file to Markdown
markitdown document.pdf -o document.md
markitdown spreadsheet.xlsx -o spreadsheet.md
markitdown report.html -o report.md

# Convert from standard input
cat document.html | markitdown > document.md
```

## Python API Usage
```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False)
result = md.convert_local("document.docx")
print(result.markdown)
```
