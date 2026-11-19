#!/usr/bin/env bash
set -euo pipefail
test -f "output/ingested/substrate_report.md"
test -f "output/ingested/consolidated_digest.md"
grep -q "Hermes Substrate Report" "output/ingested/substrate_report.md"
grep -q "|" "output/ingested/substrate_report.md"
grep -q "4303" "output/ingested/consolidated_digest.md"
grep -q "38.83" "output/ingested/consolidated_digest.md"
python3 -c '
from markitdown import MarkItDown
md = MarkItDown(enable_plugins=False)
res = md.convert_local("output/fixtures/substrate_report.html")
assert "4303" in res.markdown and "|" in res.markdown
print("[PASS] Gauntlet G microsoft/markitdown Ingestion Contract Verified")
'
