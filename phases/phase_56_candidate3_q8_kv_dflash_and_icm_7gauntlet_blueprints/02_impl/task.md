# Phase 56 Implementation Task: Substrate Hardening & ICM 7-Gauntlet Blueprints

* **Stage**: 02_impl
* **ICM Layer**: Layer 4 (Execution Task Definition)

## Implementation Steps
1. Reconfigure `/var/home/imshubhamsocial/.local/bin/llama-server` to export `GGML_CUDA_GRAPH_OPT=1`, default `GGML_CUDA_FORCE_MMQ=0`, `--spec-draft-n-max 6 --spec-draft-n-min 2 --spec-draft-p-min 0.75`, and verify active VRAM at 4,285 MiB (5,800.0 MiB ceiling).
2. Execute Dream-RSI Pass 1 Pre-Gauntlet Warm-Start pass by reloading `hermes-rsi-daemon.service` and verifying `.hermes/cache/rsi_last_distill.json`.
3. Scaffold 21 staged prompt files across all 7 gauntlets in `benchmarks/`:
   - Stages 1-3 for Gauntlets A through G adhering strictly to Section 4 of `GDR32 Certification & ICM Blueprint.md`.
4. Update `launch_konsole.sh` in each gauntlet folder to support staged execution (`PROMPT_STAGE1.txt`, `PROMPT_STAGE2.txt`, `PROMPT_STAGE3.txt`) with canonical CLI flags and `--max-turns`.
5. Update `benchmarks/launch_all_konsole.sh` to support interactive gauntlet and stage selection.
6. Verify line budget limits across all gauntlet markdown files (`CONTEXT.md`, `invariants.md`, `rules.md`, `references.md`).
7. Execute `03_verify/contract.sh`, confirm all assertions pass cold, and seal `status.json`.
