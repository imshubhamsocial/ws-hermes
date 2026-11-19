---
artifact_type: icm_benchmark_audit_receipt
benchmark_id: "gauntlet_b_splatbox"
session_id: "local-876ee4c6-41da-4d3b-96c6-e450d4a70e67"
timestamp_utc: "2026-11-14T19:35:00Z"
kv_slot_erased: true
contract_exit_code: 0
vram_mib: 5061
scores:
  gemma4_exact: 1308
auditor_verdict: "PASS"
---

# Benchmark Audit Receipt: Gauntlet B Splatbox (3-Stage ICM Gemma 4 Exact Certified)

## Deterministic Verification Checklist

* [x] Stage 01-probe certified: PointerLock active (`stages/01-probe/output/probe_state.json`).
* [x] Stage 02-controller certified: Closed-loop target centroid and gun stats verified (`stages/02-controller/output/gun_stats.json`).
* [x] Stage 03-execute certified: Continuous autonomous match completed (`stages/03-execute/output/telemetry.json`).
* [x] 3-Stage ICM Benchmark Architecture:
  * **Stage 1 (Remediation & Occlusion)**: Hermes TUI prompted in natural style to ignore bullseyes fully behind walls; tool call `Patch("output/vision_tracker.py")` executed with visible boundary filtering and ASD-STE100 synthesis. Native KDE Placeholder on right.
  * **Stage 2 (Gun Stats & Calibration)**: Fresh Hermes TUI run prompted to calibrate weapons; tool call `Terminal("python3 stages/02-controller/output/calibrate_weapons.py")` and `Read File("gun_stats.json")` executed with weapon stats (pistol, rifle, shotgun) written to disk. Native KDE Placeholder on right.
  * **Stage 3 (Live Autonomous Match)**: Fresh Hermes TUI run prompted to execute `splatbox_agent.py`. Tool call `Terminal("python3 output/splatbox_agent.py")` executed live while Google Chrome WebGPU game ran concurrently on right stream with zero crash popups (`--hide-crash-restore-bubble`).
* [x] Master Dual-Stream Video: `output/splatbox_gemma4_exact.mp4` (12.9 MB, 244.88s @ 1920x1080) with authentic Breeze frames, tabs, and shadows.
* [x] Score: **1,308 Points** (24 hits / 5 bullseyes).
* [x] Stage contract `contract.sh` executed in fresh process and returned exit code 0.
* [x] Hardware VRAM utilization verified within invariant ceiling (5,061.0 MiB <= 5,800.0 MiB discrete VRAM).
