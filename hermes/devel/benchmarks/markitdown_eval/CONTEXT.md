# Stage Contract: Gauntlet G — microsoft/markitdown Document Ingestion

## Inputs
* Workspace Root Map: ../../AGENTS.md
* Installed Skill: ~/.hermes/skills/markitdown/SKILL.md
* Hard Operational & Security Bounds: ./invariants.md
* Format Conversion Heuristics: ./rules.md
* microsoft/markitdown CLI & Python API Schemas: ./references.md

## Process
> 1. Read ./invariants.md, ./rules.md, and ./references.md.
> 2. Generate multi-format local document fixtures inside output/fixtures/ (substrate_report.html, vram_ledger.csv, and phase55_summary.docx) containing structured headings, tables, and bulleted invariants.
> 3. Convert each fixture into clean GitHub-Flavored Markdown inside output/ingested/ using both the markitdown CLI (markitdown <input> -o <output.md>) and the targeted Python API (MarkItDown(enable_plugins=False).convert_local()).
> 4. Consolidate the ingested Layer 3 reference digest into output/ingested/consolidated_digest.md and run bash ./contract.sh.

## Outputs
* Ingested Markdown Files: output/ingested/*.md
* Verification Receipt: output/status.json

## Verify
* Run bash ./contract.sh and confirm exit code 0.
