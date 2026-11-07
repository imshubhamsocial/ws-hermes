---
artifact_type: icm_benchmark_audit_receipt
benchmark_id: "gauntlet_b_splatbox"
session_id: "local-f948114c5b5f0faebf2c2f343c014305022a19fa7aeaed656fbaebc558add6f1"
timestamp_utc: "2026-11-07T17:28:00Z"
kv_slot_erased: true
contract_exit_code: 0
vram_mib: 5009
score: 299
duration_sec: 58.1
frames_processed: 242
embeddinggemma2_verified: true
auditor_verdict: "PASS"
---

# Benchmark Audit Receipt: Gauntlet B Splatbox

## Deterministic Verification Checklist

* [x] Stage 01-probe certified: PointerLock active (`stages/01-probe/output/probe_state.json`).
* [x] Stage 02-controller certified: Closed-loop target centroid verified (`stages/02-controller/output/tracker_verified.json`).
* [x] Stage 03-execute certified: Genuine autonomous match completed (`output/telemetry.json` and `stages/03-execute/output/telemetry.json`).
* [x] Zero Fake Green: Genuine Splatbox DOM `#score` reached 299 (>= 25), 242 frames (>= 120), match duration 58.1s (>= 55s), and semantic embedding verification `embeddinggemma2_verified == true`.
* [x] Stage contract `contract.sh` executed in fresh process and returned exit code 0.
* [x] Hardware VRAM utilization verified at 5,009 MiB (<= 5,800.0 MiB ceiling).
