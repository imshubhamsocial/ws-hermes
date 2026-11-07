#!/usr/bin/env bash
set -euo pipefail
test -f "output/recon_report.md"
test -f "output/recon_evidence.json"
python3 -c '
import json, hashlib
ev = json.load(open("output/recon_evidence.json"))
assert ev.get("mcp_tools_invoked") == 0, "Zero MCP tools invariant violated"
assert ev.get("original_sha256_preserved") is True, "Original target mutated"
claims = ev.get("claims", [])
assert len(claims) >= 3, "Must report at least 3 verified recon claims"
valid_states = {"seen", "inferred", "unknown"}
for c in claims:
    assert c.get("epistemic_status") in valid_states, f"Invalid epistemic_status in {c}"
    assert len(c.get("evidence_cmd", "")) > 0, f"Missing evidence_cmd in {c}"
print("[PASS] Gauntlet D leanrea Recon Contract Verified:", len(claims), "claims validated.")
'
