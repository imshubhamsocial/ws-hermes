# Hard Invariants: Gauntlet G — microsoft/markitdown Document Ingestion

> 1. **100% Offline Local Conversion (convert_local)**: Never configure Azure Document Intelligence (docintel_endpoint), Azure Content Understanding (--use-cu), or remote OpenAI clients. All conversions MUST execute 100% locally inside ws-hermes.
> 2. **Third-Party Plugins Disabled by Default**: Always instantiate MarkItDown(enable_plugins=False) and never pass --use-plugins unless explicitly requested by a human gate.
> 3. **Restricted Input Surface**: In Python code, always call md.convert_local(filepath) rather than permissive md.convert(uri) to prevent SSRF or unintended network fetches (microsoft/markitdown Security Rule).
> 4. **Structural GFM Preservation**: Converted Markdown outputs MUST preserve # heading hierarchies and pipe | ... | table structures with zero raw binary garbage or unclosed code blocks.
> 5. **Context Budget Discipline**: Never dump raw multi-megabyte documents into active context; inspect converted .md headers and table summaries selectively within the 2,000–8,000 token stage budget.
