# Procedural Rules: Gauntlet G — microsoft/markitdown Document Ingestion

> 1. **Step 1 — Fixture Preparation (output/fixtures/)**:
   * Create deterministic multi-format test fixtures (output/fixtures/substrate_report.html, output/fixtures/vram_ledger.csv, and output/fixtures/phase55_summary.docx) containing known ground-truth headings (# Hermes Substrate Report) and tabular metrics (4303, 5800, 38.83).
> 2. **Step 2 — CLI & Python API Conversion (output/ingested/)**:
   * Execute markitdown output/fixtures/substrate_report.html -o output/ingested/substrate_report.md.
   * Execute Python MarkItDown(enable_plugins=False).convert_local() on all remaining fixtures and write .markdown to output/ingested/.
> 3. **Step 3 — Post-Ingestion Normalization**:
   * Verify that every output .md file is non-empty, UTF-8 encoded, contains preserved markdown tables (|), and passes bash ./contract.sh.
