---
artifact_type: icm_stage_audit_receipt
stage_id: "{NN}-{stage_name}"
run_id: "{run_id}"
timestamp_utc: "{timestamp_utc}"
kv_slot_erased: true
contract_exit_code: 0
vram_mib: 40
auditor_verdict: "PASS"
---

# Stage Audit Receipt: {NN}-{stage_name}

## Deterministic Verification Checklist

* [x] Stage output artifact exists on disk and is non-empty.
* [x] llama-server Slot 0 KV cache erased prior to verification (POST /slots/0?action=erase).
* [x] Stage contract.sh executed in fresh process and returned exit code 0.
* [x] Hardware VRAM utilization verified below 5,800.0 MiB active / 100.0 MiB quiescent ceiling.
