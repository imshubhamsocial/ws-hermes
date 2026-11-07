# GDR37 Hermes Unified ICM Architecture & Repository Reorganization Blueprint

> **Release Package**: GDR37  
> **Author**: Lead Architect Argon  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Engine**: Gemma 4 Exact (`gemma-4-E4B-it-q4_0-exact.gguf` + MTP Drafter)  
> **Context Window**: 131,072 tokens (128K context, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Envelope**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB GDDR6, 4,997 MiB active, 861 MiB free headroom)  
> **Target Repository**: `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes` (`ws-hermes`)  
> **Compliance Standard**: ASD-STE100 Simplified Technical English & Jake Van Clief ICM (arXiv:2603.16021)  

---

## 1. Executive Architectural Audit & Forensic Findings

We inspected all 2,622 tracked entries in the imported `ws-hermes` repository snapshot (`656069dc79894786fd2299dcb6c119db8d00f9be`). The physical deployment of Phase 58 and the 5-layer Interpretable Context Methodology (ICM) structure passes `python3 _tools/hermes_icm_validator.py` with zero errors. However, our forensic audit identified five structural discrepancies that require remediation during this reorganization:

1. **Daemon Wrapper Drift in `.local/bin/llama-server`**: The tracked repository file `.local/bin/llama-server` still launches Candidate 3 (`NVIDIA-Nemotron-3.5-Bolt-E4B-UD-Q4_K_XL.gguf` at `--ctx-size 65536`). You must update this tracked wrapper to match the live Gemma 4 Exact 128K MTP daemon reported in Document 01.

2. **Broken Link Failures in `_tools/links.py`**: Running `python3 -I _tools/links.py` across the workspace exits with code 1 due to 16 relative Wayback Machine links inside `logs/gaia_custom_tui/*.md`. Relocating `logs/` to `_archive/logs/` resolves this failure because `_tools/links.py` automatically skips `_archive/`.

3. **Layer 3 Dual-Directory Split (`rules/` vs `_config/`)**: Phases 54 and 55 assert the existence of `rules/*.md` and `references/*.md`, whereas Phase 58 routes agents to `_config/*.md` and `shared/*.md`. Consolidating all physical Layer 3 files into `_config/` and deploying relative POSIX symlinks in `rules/` and `references/` enforces **One Fact, One Home** without breaking sealed phase contracts.

4. **Validator Duplication (`scripts/` vs `_tools/`)**: Two different versions of `hermes_icm_validator.py` exist in `scripts/` and `_tools/`. Consolidating the validator in `_tools/hermes_icm_validator.py` and symlinking `scripts/hermes_icm_validator.py` preserves backward compatibility with Phases 50, 52, 55, 56, and 57.

5. **Root Workspace Clutter & Zero-Byte Placeholders**: Stray root files (`20261030_211600_eca196`, `fib.py`, `my_fibonacci`, `.chezmoiignore`), temporary directories (`temp_test_run/`, `scenario/`), and zero-byte SQLite placeholders (`.hermes/state-db`, `.hermes/state_db`, `.hermes/statedb`) pollute the repository root.

## 2. Directive 1: Pre-Migration Safety Audit (Keep-Out Enforcement)

### 2.1 Immutable Keep-Out Inventory

Do not delete or break any path listed in the Keep-Out Inventory below.

| System Component | Repository / Host Path | Bound Port / Resource | Invariant Protection Mandate |
| :--- | :--- | :--- | :--- |
| **Inference Daemon Unit** | `.config/systemd/user/hermes-llama-server.service` | Port `8138` (`127.0.0.1`) | Retain in place; bound to systemd user manager. |
| **Memory Daemon Unit** | `.config/systemd/user/hermes-openviking.service` | Port `1933` (`127.0.0.1`) | Retain in place; bound to systemd user manager. |
| **CPU Embedding Unit** | `~/.config/systemd/user/hermes-embedding-cpu.service` | Port `8139` (`127.0.0.1`) | Retain on host; pinned to CPU cores 6-11 at 0 MiB VRAM. |
| **Inference Binary Wrapper** | `.local/bin/llama-server` | Port `8138` / Cores `0-5` | Retain in place; sync flags to Gemma 4 Exact 128K. |
| **OpenViking Bootstrap** | `.local/bin/openviking-server` | Port `1933` (`0` MiB VRAM) | Retain in place; required by `hermes-openviking.service`. |
| **OpenViking Configs** | `.openviking/ov.conf` & `.openviking/ovcli.conf` | Port `1933` Storage | Retain in place; configures `.openviking/data` graph store. |
| **Hermes Master Config** | `.hermes/config.yaml` | Port `8642` & Port `9222` | Retain in place; binds Gateway (`8642`) and CDP (`9222`). |
| **Upstream Submodule** | `.hermes/hermes-agent` | Rule 9 Substrate Purity | Never touch; `git status --porcelain` must remain empty. |
| **Layer 0 Protocol Map** | `AGENTS.md`, `CLAUDE.md`, `IDENTITY.md`, `SOUL.md` | Layer 0 (< 60 lines) | Retain at workspace root; entry point for all agents. |
| **Layer 1 Task Router** | `CONTEXT.md` | Layer 1 (< 80 lines) | Retain at workspace root; maps tasks to stage contracts. |
| **Master Status Ledger** | `phases/status_ledger.json` | Phases 1 to 58 | Retain in place; cryptographic ledger for 58 sealed phases. |
| **Phase Verify Contracts** | `phases/phase_*/03_verify/contract.sh` | Phases 1 to 58 | Retain in place; all verification scripts must exit 0. |
| **Active Gauntlet A** | `benchmarks/gauntlet_a_voxel_fps/` | Port `8080` WebSocket | Retain in place; 20 Hz tick multiplayer voxel FPS testbed. |
| **Active Gauntlet B** | `benchmarks/gauntlet_b_splatbox/` | Port `9222` CDP + CPU CV | Retain in place; 3-stage OpenCV HoughCircles tracker. |
| **Active Gauntlet C** | `benchmarks/gauntlet_c_aquarium/` | WebGL Three.js `0.165.0` | Retain in place; `uniforms: {}` shader & buoyancy testbed. |

### 2.2 Synchronization of .local/bin/llama-server to Gemma 4 Exact (128K)

Update the tracked `.local/bin/llama-server` file so the Git repository matches your live Phase 58 daemon configuration:

```bash
cat << 'EOF' > /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.local/bin/llama-server
#!/usr/bin/env bash
# Hermes GDR37 Production llama-server: Gemma 4 Exact (128K TurboQuant + MTP Drafter)
set -euo pipefail
SITE_PACKAGES="$(python3 -m site --user-site 2>/dev/null || python3.14 -m site --user-site 2>/dev/null || python3.13 -m site --user-site 2>/dev/null || echo "${HOME}/.local/lib/python3.14/site-packages")"
LLAMA_LIB_DIR="${HOME}/.local/lib:${WORKSPACE_ROOT:-$(pwd)}/.local/lib"
SERVER_BIN="${HOME}/.local/bin/llama-server.bin"
export LD_LIBRARY_PATH="${LLAMA_LIB_DIR}:${SITE_PACKAGES}/nvidia/cu13/lib:${SITE_PACKAGES}/nvidia/cublas/lib:${SITE_PACKAGES}/nvidia/cuda_nvrtc/lib:${SITE_PACKAGES}/nvidia/nccl/lib:${SITE_PACKAGES}/nvidia/cuda_runtime/lib:${HOME}/.local/share/cuda-libs:${LD_LIBRARY_PATH:-}"

if [[ $# -gt 0 ]]; then
    exec "$SERVER_BIN" "$@"
fi

export GGML_CUDA_GRAPH_OPT=1
export GGML_CUDA_FORCE_MMQ=1

exec taskset -c 0-5 "$SERVER_BIN" \
    --model "${HOME}/.hermes/models/gemma-4-E4B-it-q4_0-exact.gguf" \
    --model-draft "${HOME}/.hermes/models/gemma-4-E4B-it-qat-assistant-q4_0-exact.gguf" \
    --n-gpu-layers-draft all \
    --spec-type draft-mtp \
    --spec-draft-n-max 2 \
    --alias "gemma-4-E4B-it-qat-exact,gemma-4-e4b-exact,google/gemma-4-E4B-it,nemotron-3.5-bolt-e4b,dory" \
    --host 127.0.0.1 --port 8138 \
    --ctx-size 131072 \
    --cache-type-k q4_0 --cache-type-v q4_0 \
    --batch-size 2048 --ubatch-size 1024 \
    --flash-attn on \
    --reasoning on \
    --jinja \
    --n-gpu-layers 99 \
    --threads 6 --threads-batch 6 --parallel 1 --cont-batching \
    --temp 1.0 --top-p 0.95 --top-k 64 --metrics
EOF
chmod +x /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.local/bin/llama-server
```

## 3. Directive 2: Comprehensive Repository Triage & Classification

We classify every path in `ws-hermes` into one of four strict ICM triage categories:

### 3.1 Category A: Retain In Place (Critical Substrate & Orchestration Core)

- **Layer 0 & Layer 1 Root Files**: `AGENTS.md`, `CLAUDE.md`, `IDENTITY.md`, `SOUL.md`, `CONTEXT.md`.
- **Build & Package Manifests**: `Makefile`, `README.md`, `.gitignore`, `.pre-commit-config.yaml`, `pyproject.toml`, `requirements.txt`, `package.json`, `package-lock.json`, `hermes-pack.yaml`, `conftest.py`.
- **ICM Factory Core**: `_config/`, `_templates/`, `_tools/`, `shared/`, `skills/icm-architect/`.
- **Active Stage & Benchmark Contracts**: `stages/01-probe/`, `stages/02-controller/`, `stages/03-execute/`, `stages/01-spec/`, `stages/02-plan/`, `stages/04-verify/`, and all seven benchmark directories under `benchmarks/` (`gauntlet_a_voxel_fps`, `gauntlet_b_splatbox`, `gauntlet_c_aquarium`, `leanrea_eval`, `ffmpeg_skill_eval`, `diagram_design_eval`, `markitdown_eval`, `gaia`, `tau_bench`, `ast_grep_eval`).
- **Sealed Verification Registry & Research Corpus**: `phases/` (Phases 1 to 58 and `status_ledger.json`) and `docs/` (`docs/reference/` and `docs/research/GDR30` through `GDR37`).
- **Runtime Substrate Directories**: `.config/systemd/user/`, `.local/bin/`, `.openviking/`, and active `.hermes/` subdirectories (`config.yaml`, `SOUL.md`, `biome.json`, `cron/`, `guardrails/`, `hermes-rsi-daemon.service`, `hub/`, `memories/`, `rules/`, `runtime_hooks/`, `skills/`).

### 3.2 Category B: Consolidate to ICM Factory (Layer 3 Unification + Symlink Bridges)

- **Domain Rules (`rules/*.md` -> `_config/`)**: Move `rules/anti_rationalization_tables.md`, `rules/anti_sycophancy_directives.md`, `rules/hardware_vram_invariants.md`, and `rules/rules.md` into `_config/`. Replace `rules/*.md` with relative symlinks to `../_config/*.md` so Phase 50, 54, and 55 verification contracts pass without modification.
- **Port & Literature References (`references/*.md` -> `_config/`)**: Deduplicate `references/substrate_ports.md` into `_config/substrate_ports.md` via a relative symlink, and move `references/references.md` to `_config/references.md` with a symlink at `references/references.md`.
- **Validator Consolidation (`scripts/hermes_icm_validator.py` -> `_tools/`)**: Remove the outdated duplicate validator in `scripts/hermes_icm_validator.py` (which checks non-existent `artifacts/`) and replace it with a relative symlink to `../_tools/hermes_icm_validator.py`.

### 3.3 Category C: Archive to Historical Vault (_archive/)

We use `_archive/` as the physical vault directory and link `archive -> _archive` so `_tools/links.py` automatically skips archived artifacts during link validation:

- **Root Session & Benchmark Reports**: Move `20261030_211600_eca196`, `BENCHMARK_ANALYSIS_REPORT.md`, and `BENCHMARK_SESSIONS.md` into `_archive/reports/`.
- **Historical Evaluation Logs (`logs/*`)**: Move all October 2026 `.eval` files and subdirectories (`gaia_custom_tui`, `inspect_gaia_test`, `inspect_tau2_retail_test`, `tau_bench_*`) into `_archive/logs/`, leaving an empty `logs/.gitkeep` directory.
- **Legacy DPO & Scenario Workspaces**: Move `dream_rsi_workspace/` to `_archive/dream_rsi_workspace/` and `scenario/` to `_archive/scenario/`.
- **Superseded Gauntlet Baseline & Debug Captures**: Move `benchmarks/gauntlet_c_aquarium/output/aquarium-sim.baseline` to `_archive/benchmarks/aquarium-sim.baseline`, and move the 10 intermediate debug screenshots in `benchmarks/gauntlet_b_splatbox/output/*.png` to `_archive/benchmarks/gauntlet_b_splatbox_debug/`.
- **Legacy Phase 01-30 Testbeds (`tests/*`)**: Move `tests/` to `_archive/tests/` and create a relative symlink `tests -> _archive/tests` so `phases/remediation_gauntlet/03_verify/contract.sh` and legacy phase contracts resolve their paths.

### 3.4 Category D: Prune / Safe Deletion (Zero Contract References)

- **Retired Chezmoi Manifest**: Delete `.chezmoiignore` (chezmoi was retired in GDR37 Section 5).
- **Root Scratch Binaries & Scripts**: Delete `fib.py` and the compiled ELF binary `my_fibonacci` at the workspace root.
- **Duplicate Temporary Directories**: Delete `temp_test_run/` and the empty stub directory `tests/phase26/` (superseded by `tests/phase26_zero_spoon_eval/`).
- **Zero-Byte SQLite Placeholders & Transient Lock Ledger**: Delete `.hermes/state-db`, `.hermes/state_db`, `.hermes/statedb` (all 0 bytes), and `.hermes/spawn-ledger.json` (ephemeral runtime state).
- **Duplicate Root Gauntlet Receipts & Stale Rule File**: Delete duplicate root receipts `benchmarks/gauntlet_a_voxel_fps/stage1_spec_receipt.json`, `benchmarks/gauntlet_a_voxel_fps/stage2_client_receipt.json`, `benchmarks/gauntlet_c_aquarium/stage1_physics_receipt.json`, `benchmarks/gauntlet_c_aquarium/stage2_scene_receipt.json` (authoritative copies reside in each gauntlet's `output/` folder), and `rules/rule_icm_validation_script_missing.md`.

## 4. Directive 3: Actionable Migration Mapping Table

Execute the following atomic operations in order. Every row preserves git history and provides a deterministic verification check and rollback command.

| Original Path | Destination Path | Triage Category | Rationale / Invariant | Exact Git Command | Verification Check | Rollback Command |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `AGENTS.md` | `AGENTS.md` | Cat A | Retain Layer 0 protocol map (< 60 lines) | `true` | `test -f AGENTS.md` | `git checkout -- AGENTS.md` |
| `CONTEXT.md` | `CONTEXT.md` | Cat A | Retain Layer 1 task router (< 80 lines) | `true` | `test -f CONTEXT.md` | `git checkout -- CONTEXT.md` |
| `CLAUDE.md` | `CLAUDE.md` | Cat A | Convert 1-line pointer to symlink for Phase 50 | `ln -sf AGENTS.md CLAUDE.md && git add CLAUDE.md` | `test -L CLAUDE.md` | `git checkout -- CLAUDE.md` |
| `IDENTITY.md` | `IDENTITY.md` | Cat A | Retain 1-line pointer to `AGENTS.md` | `true` | `test -f IDENTITY.md` | `git checkout -- IDENTITY.md` |
| `SOUL.md` | `SOUL.md` | Cat A | Retain Layer 0 epistemic disposition | `true` | `test -f SOUL.md` | `git checkout -- SOUL.md` |
| `Makefile` | `Makefile` | Cat A | Retain master build and verification targets | `true` | `test -f Makefile` | `git checkout -- Makefile` |
| `.config/systemd/user/` | `.config/systemd/user/` | Cat A | Keep-Out: Ports 8138 and 1933 systemd services | `true` | `test -f .config/systemd/user/hermes-llama-server.service` | `git checkout -- .config/systemd/user/` |
| `.local/bin/` | `.local/bin/` | Cat A | Keep-Out: `llama-server` and `openviking-server` | `git add .local/bin/llama-server` | `test -x .local/bin/llama-server` | `git checkout -- .local/bin/llama-server` |
| `.openviking/` | `.openviking/` | Cat A | Keep-Out: Port 1933 graph daemon configuration | `true` | `test -f .openviking/ov.conf` | `git checkout -- .openviking/` |
| `.hermes/config.yaml` | `.hermes/config.yaml` | Cat A | Keep-Out: Canonical substrate config | `true` | `test -f .hermes/config.yaml` | `git checkout -- .hermes/config.yaml` |
| `phases/` | `phases/` | Cat A | Keep-Out: Phases 1 to 58 and `status_ledger.json` | `true` | `test -f phases/status_ledger.json` | `git checkout -- phases/` |
| `benchmarks/gauntlet_a_voxel_fps/` | `benchmarks/gauntlet_a_voxel_fps/` | Cat A | Keep-Out: Gauntlet A 20 Hz netcode suite | `true` | `test -f benchmarks/gauntlet_a_voxel_fps/contract.sh` | `git checkout -- benchmarks/gauntlet_a_voxel_fps/` |
| `benchmarks/gauntlet_b_splatbox/` | `benchmarks/gauntlet_b_splatbox/` | Cat A | Keep-Out: Gauntlet B 3-stage OpenCV suite | `true` | `test -f benchmarks/gauntlet_b_splatbox/contract.sh` | `git checkout -- benchmarks/gauntlet_b_splatbox/` |
| `benchmarks/gauntlet_c_aquarium/` | `benchmarks/gauntlet_c_aquarium/` | Cat A | Keep-Out: Gauntlet C WebGL aquarium suite | `true` | `test -f benchmarks/gauntlet_c_aquarium/contract.sh` | `git checkout -- benchmarks/gauntlet_c_aquarium/` |
| `rules/anti_rationalization_tables.md` | `_config/anti_rationalization_tables.md` | Cat B | Consolidate Layer 3 rules into `_config/` + symlink | `git mv rules/anti_rationalization_tables.md _config/anti_rationalization_tables.md && ln -s ../_config/anti_rationalization_tables.md rules/anti_rationalization_tables.md && git add rules/anti_rationalization_tables.md` | `test -f _config/anti_rationalization_tables.md && test -L rules/anti_rationalization_tables.md` | `git rm -f rules/anti_rationalization_tables.md && git mv _config/anti_rationalization_tables.md rules/anti_rationalization_tables.md` |
| `rules/anti_sycophancy_directives.md` | `_config/anti_sycophancy_directives.md` | Cat B | Consolidate Layer 3 directives into `_config/` + symlink | `git mv rules/anti_sycophancy_directives.md _config/anti_sycophancy_directives.md && ln -s ../_config/anti_sycophancy_directives.md rules/anti_sycophancy_directives.md && git add rules/anti_sycophancy_directives.md` | `test -f _config/anti_sycophancy_directives.md && test -L rules/anti_sycophancy_directives.md` | `git rm -f rules/anti_sycophancy_directives.md && git mv _config/anti_sycophancy_directives.md rules/anti_sycophancy_directives.md` |
| `rules/hardware_vram_invariants.md` | `_config/hardware_vram_invariants.md` | Cat B | Consolidate 128K VRAM rules into `_config/` + symlink | `git mv rules/hardware_vram_invariants.md _config/hardware_vram_invariants.md && ln -s ../_config/hardware_vram_invariants.md rules/hardware_vram_invariants.md && git add rules/hardware_vram_invariants.md` | `test -f _config/hardware_vram_invariants.md && test -L rules/hardware_vram_invariants.md` | `git rm -f rules/hardware_vram_invariants.md && git mv _config/hardware_vram_invariants.md rules/hardware_vram_invariants.md` |
| `rules/rules.md` | `_config/operational_rules.md` | Cat B | Consolidate stage rules into `_config/` + symlink | `git mv rules/rules.md _config/operational_rules.md && ln -s ../_config/operational_rules.md rules/rules.md && git add rules/rules.md` | `test -f _config/operational_rules.md && test -L rules/rules.md` | `git rm -f rules/rules.md && git mv _config/operational_rules.md rules/rules.md` |
| `rules/invariants.md` | `_config/invariants.md` | Cat B | Deduplicate `rules/invariants.md` to `_config/invariants.md` | `git rm -f rules/invariants.md && ln -s ../_config/invariants.md rules/invariants.md && git add rules/invariants.md` | `test -L rules/invariants.md && test -f rules/invariants.md` | `git checkout HEAD -- rules/invariants.md` |
| `references/substrate_ports.md` | `_config/substrate_ports.md` | Cat B | Deduplicate port map to `_config/substrate_ports.md` | `git rm -f references/substrate_ports.md && ln -s ../_config/substrate_ports.md references/substrate_ports.md && git add references/substrate_ports.md` | `test -L references/substrate_ports.md` | `git checkout HEAD -- references/substrate_ports.md` |
| `references/references.md` | `_config/references.md` | Cat B | Consolidate literature index into `_config/` + symlink | `git mv references/references.md _config/references.md && ln -s ../_config/references.md references/references.md && git add references/references.md` | `test -f _config/references.md && test -L references/references.md` | `git rm -f references/references.md && git mv _config/references.md references/references.md` |
| `scripts/hermes_icm_validator.py` | `_tools/hermes_icm_validator.py` | Cat B | Unify validator to `_tools/hermes_icm_validator.py` + symlink | `git rm -f scripts/hermes_icm_validator.py && ln -s ../_tools/hermes_icm_validator.py scripts/hermes_icm_validator.py && git add scripts/hermes_icm_validator.py` | `test -L scripts/hermes_icm_validator.py` | `git checkout HEAD -- scripts/hermes_icm_validator.py` |
| `20261030_211600_eca196` | `_archive/sessions/20261030_211600_eca196.json` | Cat C | Archive stray TUI session dump from workspace root | `mkdir -p _archive/sessions && git mv 20261030_211600_eca196 _archive/sessions/20261030_211600_eca196.json` | `test -f _archive/sessions/20261030_211600_eca196.json` | `git mv _archive/sessions/20261030_211600_eca196.json 20261030_211600_eca196` |
| `BENCHMARK_ANALYSIS_REPORT.md` | `_archive/reports/BENCHMARK_ANALYSIS_REPORT.md` | Cat C | Archive GDR30 benchmark report from workspace root | `mkdir -p _archive/reports && git mv BENCHMARK_ANALYSIS_REPORT.md _archive/reports/BENCHMARK_ANALYSIS_REPORT.md` | `test -f _archive/reports/BENCHMARK_ANALYSIS_REPORT.md` | `git mv _archive/reports/BENCHMARK_ANALYSIS_REPORT.md BENCHMARK_ANALYSIS_REPORT.md` |
| `BENCHMARK_SESSIONS.md` | `_archive/reports/BENCHMARK_SESSIONS.md` | Cat C | Archive session registry from workspace root | `mkdir -p _archive/reports && git mv BENCHMARK_SESSIONS.md _archive/reports/BENCHMARK_SESSIONS.md` | `test -f _archive/reports/BENCHMARK_SESSIONS.md` | `git mv _archive/reports/BENCHMARK_SESSIONS.md BENCHMARK_SESSIONS.md` |
| `logs/` | `_archive/logs/` | Cat C | Archive October 2026 eval logs and fix `links.py` errors | `git mv logs _archive/logs && mkdir -p logs && touch logs/.gitkeep && git add logs/.gitkeep` | `test -d _archive/logs && test -f logs/.gitkeep` | `rm -rf logs && git mv _archive/logs logs` |
| `dream_rsi_workspace/` | `_archive/dream_rsi_workspace/` | Cat C | Archive GDR24 DPO pair compilation workspace | `git mv dream_rsi_workspace _archive/dream_rsi_workspace` | `test -d _archive/dream_rsi_workspace` | `git mv _archive/dream_rsi_workspace dream_rsi_workspace` |
| `scenario/` | `_archive/scenario/` | Cat C | Archive legacy root scenario script | `git mv scenario _archive/scenario` | `test -d _archive/scenario` | `git mv _archive/scenario scenario` |
| `benchmarks/gauntlet_c_aquarium/output/aquarium-sim.baseline` | `_archive/benchmarks/aquarium-sim.baseline` | Cat C | Archive broken pre-remediation shader baseline | `mkdir -p _archive/benchmarks && git mv benchmarks/gauntlet_c_aquarium/output/aquarium-sim.baseline _archive/benchmarks/aquarium-sim.baseline` | `test -d _archive/benchmarks/aquarium-sim.baseline` | `git mv _archive/benchmarks/aquarium-sim.baseline benchmarks/gauntlet_c_aquarium/output/aquarium-sim.baseline` |
| `benchmarks/gauntlet_b_splatbox/output/*.png` | `_archive/benchmarks/gauntlet_b_splatbox_debug/` | Cat C | Archive intermediate debug PNGs from Gauntlet B root output | `mkdir -p _archive/benchmarks/gauntlet_b_splatbox_debug && git mv benchmarks/gauntlet_b_splatbox/output/*.png _archive/benchmarks/gauntlet_b_splatbox_debug/` | `test -d _archive/benchmarks/gauntlet_b_splatbox_debug` | `git mv _archive/benchmarks/gauntlet_b_splatbox_debug/*.png benchmarks/gauntlet_b_splatbox/output/` |
| `tests/` | `_archive/tests/` | Cat C | Archive Phase 01-30 testbeds with root symlink bridge | `git rm -rf tests/phase26 && git mv tests _archive/tests && ln -s _archive/tests tests && git add tests` | `test -L tests && test -d _archive/tests` | `git rm -f tests && git mv _archive/tests tests` |
| `.chezmoiignore` | `(Deleted)` | Cat D | Prune obsolete chezmoi ignore file after native Git migration | `git rm -f .chezmoiignore` | `test ! -e .chezmoiignore` | `git checkout HEAD -- .chezmoiignore` |
| `fib.py` | `(Deleted)` | Cat D | Prune stray root Fibonacci test script | `git rm -f fib.py` | `test ! -e fib.py` | `git checkout HEAD -- fib.py` |
| `my_fibonacci` | `(Deleted)` | Cat D | Prune stray root compiled ELF binary | `git rm -f my_fibonacci` | `test ! -e my_fibonacci` | `git checkout HEAD -- my_fibonacci` |
| `temp_test_run/` | `(Deleted)` | Cat D | Prune temporary duplicate Phase 20 test directory | `git rm -rf temp_test_run` | `test ! -d temp_test_run` | `git checkout HEAD -- temp_test_run` |
| `rules/rule_icm_validation_script_missing.md` | `(Deleted)` | Cat D | Prune obsolete Phase 20 failure note | `git rm -f rules/rule_icm_validation_script_missing.md` | `test ! -e rules/rule_icm_validation_script_missing.md` | `git checkout HEAD -- rules/rule_icm_validation_script_missing.md` |
| `.hermes/state-db`, `.hermes/state_db`, `.hermes/statedb` | `(Deleted)` | Cat D | Prune zero-byte SQLite typo files in `.hermes/` | `git rm -f .hermes/state-db .hermes/state_db .hermes/statedb` | `test ! -e .hermes/state-db` | `git checkout HEAD -- .hermes/state-db .hermes/state_db .hermes/statedb` |
| `.hermes/spawn-ledger.json` | `(Deleted)` | Cat D | Prune transient PID spawn ledger tracked in Git | `git rm -f .hermes/spawn-ledger.json` | `test ! -e .hermes/spawn-ledger.json` | `git checkout HEAD -- .hermes/spawn-ledger.json` |
| `benchmarks/gauntlet_a_voxel_fps/stage*_receipt.json` | `(Deleted)` | Cat D | Prune duplicate receipts already stored in `output/` | `git rm -f benchmarks/gauntlet_a_voxel_fps/stage1_spec_receipt.json benchmarks/gauntlet_a_voxel_fps/stage2_client_receipt.json` | `test -f benchmarks/gauntlet_a_voxel_fps/output/stage1_spec_receipt.json` | `git checkout HEAD -- benchmarks/gauntlet_a_voxel_fps/stage1_spec_receipt.json benchmarks/gauntlet_a_voxel_fps/stage2_client_receipt.json` |
| `benchmarks/gauntlet_c_aquarium/stage*_receipt.json` | `(Deleted)` | Cat D | Prune duplicate receipts already stored in `output/` | `git rm -f benchmarks/gauntlet_c_aquarium/stage1_physics_receipt.json benchmarks/gauntlet_c_aquarium/stage2_scene_receipt.json` | `test -f benchmarks/gauntlet_c_aquarium/output/stage1_physics_receipt.json` | `git checkout HEAD -- benchmarks/gauntlet_c_aquarium/stage1_physics_receipt.json benchmarks/gauntlet_c_aquarium/stage2_scene_receipt.json` |

## 5. Directive 4: Jake Van Clief ICM Tooling, Routing Synchronization, & Line Limits

### 5.1 Enforced ICM Line and Token Budgets

We enforce the following deterministic structural bounds across all 5 ICM layers:

| ICM Layer | Canonical Files | Line Limit | Measured Lines | Token Budget |
| :--- | :--- | :--- | :--- | :--- |
| **Layer 0 (Identity & Map)** | `AGENTS.md`, `CLAUDE.md`, `IDENTITY.md`, `SOUL.md` | `< 60` lines | `35` lines (`AGENTS.md`) | `~450` tokens |
| **Layer 1 (Task Router)** | `CONTEXT.md` | `< 80` lines | `29` lines (`CONTEXT.md`) | `~320` tokens |
| **Layer 2 (Stage Contracts)** | `stages/*/CONTEXT.md`, `benchmarks/*/CONTEXT.md` | `< 80` lines | `28` to `34` lines | `200-500` tokens |
| **Layer 3 (Factory Rules)** | `_config/*.md`, `shared/*.md` | `< 200` lines | `10` to `45` lines | `500-2,000` tokens |
| **Layer 4 (Working Surface)** | Active stage `Inputs` + `output/` deliverables | Bounded | Stage-scoped | `2,000-8,000` tokens |

### 5.2 Synchronized Layer 0 (AGENTS.md) and Layer 1 (CONTEXT.md)

Update `AGENTS.md` (35 lines, strictly under the 60-line limit) and `CONTEXT.md` (30 lines, strictly under the 80-line limit) to reflect the unified `_archive/` vault and ICM tooling:

````markdown
# Layer 0: Hermes ICM Compiler Operating Protocol

## 1. Identity and Workspace Map

You operate inside ws-hermes (/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes). You are a single-pass stage compiler inside a 5-layer Interpretable Context Methodology (ICM) state machine. Do not explore the filesystem randomly. Read CONTEXT.md at the workspace root to route your task.

## 2. Core Directory Locations

* CONTEXT.md: Layer 1 task router mapping objectives to stage folders.
* _config/: Layer 3 system invariants, conventions, hardware ceilings, and domain rules.
* _templates/: Layer 3 starter templates for stages, checks, and checkpoints.
* _tools/: Layer 3 deterministic Python/POSIX validators and stage runners.
* shared/: Layer 3 cross-stage mathematical, netcode, vision, and shader schemas.
* skills/: Layer 3 domain skills (icm-architect, icm-stage-compiler).
* stages/: Layer 2 & 4 sequential compiler pipeline (01-probe/, 02-controller/, 03-execute/).
* benchmarks/: Layer 2 & 4 Frontier Gauntlets A, B, and C.
* phases/status_ledger.json: Layer 4 sealed verification ledger (Phases 1 to 58).
* _archive/: Historical vault for superseded logs, sessions, and legacy evaluations.

## 3. Ten Non-Negotiable Compiler Rules

> 1. One Stage, One Job: Execute only the contract inside the target folder's CONTEXT.md.
> 2. Bounded Context (2,000-8,000 Tokens): Load only the exact file paths and sections listed in Inputs.
> 3. One Fact, One Home: Never duplicate rules from _config/invariants.md. Link to them.
> 4. Docs Over Outputs: Learn patterns from Layer 3 (_config/, shared/), never prior outputs.
> 5. Read Before Edit: Always call read_file on a target file in the current session before editing it.
> 6. Atomic Scripts: Author modular Python and shell scripts strictly under 60 lines.
> 7. Browser Verification: Use Playwright (connect_over_cdp or headless Chromium) to verify 0 runtime errors.
> 8. Fresh Context Auditing: Never grade your own output in the generating context; use _tools/ check gates.
> 9. Substrate Purity: Never modify files inside /var/home/imshubhamsocial/.hermes/hermes-agent.
> 10. Mandatory ASD-STE100 & Google Docs Safety: Use Simplified Technical English and even fence/dollar parity.
````

Update `CONTEXT.md` (30 lines, including the 4-column table standard required by all phase validators):

````markdown
# Layer 1: Workspace Task Routing Map

## 1. Keyword Triggers

* setup: Run workspace onboarding or verify directory scaffolding via python3 _tools/hermes_icm_validator.py.
* status: Inspect pipeline completion state across stages/*/output/check.md and phases/status_ledger.json.
* walk-test: Execute the cold 8-point ICM Walk Test via python3 _tools/hermes_icm_validator.py.
* icm-sync: Audit relative links and regenerate context graphs via python3 -I _tools/links.py . --skip docs --skip phases --skip benchmarks --skip skills.
* quiesce: Stop hermes-llama-server.service and verify GPU VRAM <= 100 MiB via python3 _tools/check_vram_limit.py --mode quiescent.

## 2. Task Routing Table

| User Objective / Task Description | Target Directory | Entry Contract / Script | Layer / Scope |
| :--- | :--- | :--- | :--- |
| Execute Gauntlet B Stage 1 (Browser CDP Probe) | `stages/01-probe/` | `stages/01-probe/CONTEXT.md` | Layer 2 Stage |
| Execute Gauntlet B Stage 2 (CPU HoughCircles Aim) | `stages/02-controller/` | `stages/02-controller/CONTEXT.md` | Layer 2 Stage |
| Execute Gauntlet B Stage 3 (Action & Telemetry) | `stages/03-execute/` | `stages/03-execute/CONTEXT.md` | Layer 2 Stage |
| Run or audit Frontier Gauntlet A (3D Voxel FPS) | `benchmarks/gauntlet_a_voxel_fps/` | `benchmarks/gauntlet_a_voxel_fps/contract.sh` | Layer 4 Gauntlet |
| Run or audit Frontier Gauntlet B (3D Splatbox CV) | `benchmarks/gauntlet_b_splatbox/` | `benchmarks/gauntlet_b_splatbox/contract.sh` | Layer 4 Gauntlet |
| Run or audit Frontier Gauntlet C (3D WebGL Aquarium) | `benchmarks/gauntlet_c_aquarium/` | `benchmarks/gauntlet_c_aquarium/contract.sh` | Layer 4 Gauntlet |
| Design or restructure a workspace using ICM | `skills/icm-architect/` | `skills/icm-architect/SKILL.md` | Layer 3 Skill |
| Compile a single ICM stage with KV cache isolation | `_tools/` | `_tools/hermes_stage_runner.py` | Layer 3 Tool |
| Audit Phase 58 and seal the master status ledger | `phases/phase_58_autonomous_icm_factory_and_multi_gauntlet_certification/` | `03_verify/contract.sh` | Layer 4 Gate |
| Check system invariants, ports, and VRAM limits | `_config/` | `_config/invariants.md` | Layer 3 Config |

## 3. Context Takeover Rule

Once routed to a target stage or benchmark directory, read that directory's local CONTEXT.md and load only the files specified in its Inputs table. Do not load sibling stage folders.
````

Update `README.md` (currently outdated at GDR17 v4.4.0) so the repository landing page accurately documents the GDR37 5-layer ICM architecture:

````markdown
# Hermes Agent OS (ws-hermes) — GDR37 5-Layer ICM Software Factory

> **Substrate**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Engine**: Gemma 4 Exact (`gemma-4-E4B-it-q4_0-exact.gguf` + MTP Drafter) on Port 8138  
> **Context Window**: 131,072 tokens (128K context, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Envelope**: NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB GDDR6, ceiling <= 5,800.0 MiB)  
> **Methodology**: Jake Van Clief's Interpretable Context Methodology (ICM, arXiv:2603.16021)  

## 1. Five-Layer ICM Architecture

* **Layer 0 (`AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `CLAUDE.md`)**: Workspace map and 10 non-negotiable compiler rules (< 60 lines).
* **Layer 1 (`CONTEXT.md`)**: Task router and keyword triggers (< 80 lines).
* **Layer 2 (`stages/*/CONTEXT.md`, `benchmarks/*/CONTEXT.md`)**: Bounded single-job stage contracts (< 80 lines).
* **Layer 3 (`_config/`, `shared/`, `_templates/`, `_tools/`, `skills/`)**: System invariants, domain schemas, and deterministic validators (< 200 lines).
* **Layer 4 (`stages/*/output/`, `benchmarks/*/output/`, `phases/`)**: Inspectable plain-text deliverables and sealed verification receipts.

## 2. Quickstart Verification Commands

```bash
python3 _tools/hermes_icm_validator.py
make all
make phase-58-seal
```
````


### 5.3 Automated ICM Tooling Integration (`_tools/`)

Use the four deterministic `RinDig/icm-architect` scripts already installed in `_tools/` alongside `hermes_icm_validator.py` and `hermes_stage_runner.py`:

```bash
# 1. Validate 8-Point ICM Walk Test and line budgets
python3 _tools/hermes_icm_validator.py

# 2. Verify all relative Markdown links across active ICM layers (0 broken links)
python3 -I _tools/links.py . --skip docs --skip phases --skip benchmarks --skip skills --graph /tmp/ws_hermes_graph.jsonl

# 3. Generate _index.md catalog in _config/ and shared/ if needed
python3 -I _tools/index.py _config shared

# 4. Render interactive Cytoscape context dependency graph
python3 -I _tools/viz.py /tmp/ws_hermes_graph.jsonl -o _archive/reports/ws_hermes_icm_graph.html
```

## 6. Directive 5: Atomic Migration Script & Post-Migration Verification Protocol

### 6.1 Drop-In Non-Breaking Reorganization Script

Run this complete script from `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes` to execute all Category A, B, C, and D actions atomically:

```bash
#!/usr/bin/env bash
# GDR37 Atomic Non-Breaking ICM Workspace Reorganization Script
set -euo pipefail

cd /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes

echo "=== [Step 1/5] Pre-Flight Safety & Keep-Out Audit ==="
git -C /var/home/imshubhamsocial/.hermes/hermes-agent diff --quiet
python3 _tools/hermes_icm_validator.py

echo "=== [Step 2/5] Category B: Consolidating Layer 3 Factory (_config/ & _tools/) ==="
ln -sf AGENTS.md CLAUDE.md
git add CLAUDE.md

for rule_file in anti_rationalization_tables.md anti_sycophancy_directives.md hardware_vram_invariants.md; do
    if [[ -f "rules/${rule_file}" && ! -L "rules/${rule_file}" ]]; then
        git mv "rules/${rule_file}" "_config/${rule_file}"
        ln -s "../_config/${rule_file}" "rules/${rule_file}"
        git add "rules/${rule_file}"
    fi
done

if [[ -f "rules/rules.md" && ! -L "rules/rules.md" ]]; then
    git mv "rules/rules.md" "_config/operational_rules.md"
    ln -s "../_config/operational_rules.md" "rules/rules.md"
    git add "rules/rules.md"
fi

if [[ -f "rules/invariants.md" && ! -L "rules/invariants.md" ]]; then
    git rm -f "rules/invariants.md"
    ln -s "../_config/invariants.md" "rules/invariants.md"
    git add "rules/invariants.md"
fi

if [[ -f "references/substrate_ports.md" && ! -L "references/substrate_ports.md" ]]; then
    git rm -f "references/substrate_ports.md"
    ln -s "../_config/substrate_ports.md" "references/substrate_ports.md"
    git add "references/substrate_ports.md"
fi

if [[ -f "references/references.md" && ! -L "references/references.md" ]]; then
    git mv "references/references.md" "_config/references.md"
    ln -s "../_config/references.md" "references/references.md"
    git add "references/references.md"
fi

if [[ -f "scripts/hermes_icm_validator.py" && ! -L "scripts/hermes_icm_validator.py" ]]; then
    git rm -f "scripts/hermes_icm_validator.py"
    ln -s "../_tools/hermes_icm_validator.py" "scripts/hermes_icm_validator.py"
    git add "scripts/hermes_icm_validator.py"
fi

echo "=== [Step 3/5] Category C: Archiving Legacy Outputs & Logs to _archive/ ==="
mkdir -p _archive/sessions _archive/reports _archive/benchmarks
ln -sfn _archive archive
git add archive

[[ -f "20261030_211600_eca196" ]] && git mv "20261030_211600_eca196" "_archive/sessions/20261030_211600_eca196.json"
[[ -f "BENCHMARK_ANALYSIS_REPORT.md" ]] && git mv "BENCHMARK_ANALYSIS_REPORT.md" "_archive/reports/BENCHMARK_ANALYSIS_REPORT.md"
[[ -f "BENCHMARK_SESSIONS.md" ]] && git mv "BENCHMARK_SESSIONS.md" "_archive/reports/BENCHMARK_SESSIONS.md"

if [[ -d "logs" && ! -d "_archive/logs" ]]; then
    git mv logs _archive/logs
    mkdir -p logs
    touch logs/.gitkeep
    git add logs/.gitkeep
fi

[[ -d "dream_rsi_workspace" && ! -L "dream_rsi_workspace" ]] && git mv dream_rsi_workspace _archive/dream_rsi_workspace
[[ -d "scenario" && ! -L "scenario" ]] && git mv scenario _archive/scenario
[[ -d "benchmarks/gauntlet_c_aquarium/output/aquarium-sim.baseline" ]] && git mv benchmarks/gauntlet_c_aquarium/output/aquarium-sim.baseline _archive/benchmarks/aquarium-sim.baseline

if compgen -G "benchmarks/gauntlet_b_splatbox/output/*.png" > /dev/null; then
    mkdir -p _archive/benchmarks/gauntlet_b_splatbox_debug
    git mv benchmarks/gauntlet_b_splatbox/output/*.png _archive/benchmarks/gauntlet_b_splatbox_debug/
fi

if [[ -d "tests" && ! -L "tests" ]]; then
    [[ -d "tests/phase26" ]] && git rm -rf "tests/phase26"
    git mv tests _archive/tests
    ln -s _archive/tests tests
    git add tests
fi

echo "=== [Step 4/5] Category D: Pruning Stale Artifacts & Zero-Byte Placeholders ==="
git rm -f --ignore-unmatch \
    .chezmoiignore \
    fib.py \
    my_fibonacci \
    rules/rule_icm_validation_script_missing.md \
    .hermes/state-db \
    .hermes/state_db \
    .hermes/statedb \
    .hermes/spawn-ledger.json \
    benchmarks/gauntlet_a_voxel_fps/stage1_spec_receipt.json \
    benchmarks/gauntlet_a_voxel_fps/stage2_client_receipt.json \
    benchmarks/gauntlet_c_aquarium/stage1_physics_receipt.json \
    benchmarks/gauntlet_c_aquarium/stage2_scene_receipt.json

[[ -d "temp_test_run" ]] && git rm -rf temp_test_run

echo "=== [Step 5/5] Reorganization Complete ==="
```

### 6.2 Sequential Post-Migration Verification Suite

Run these exact verification commands sequentially after executing the reorganization script. Every command must return exit code `0`:

```bash
# 1. Static ICM Walk Test & Line Budget Validator (0 errors, 0 broken stage links)
python3 _tools/hermes_icm_validator.py

# 2. Workspace Relative Link Integrity Check (0 broken links across active ICM layers)
python3 -I _tools/links.py . --skip docs --skip phases --skip benchmarks --skip skills

# 3. Gauntlet A Verification (3D Voxel FPS & 20 Hz WebSocket Netcode)
bash benchmarks/gauntlet_a_voxel_fps/contract.sh

# 4. Gauntlet B Verification (3-Stage OpenCV CPU HoughCircles Tracker)
bash benchmarks/gauntlet_b_splatbox/contract.sh

# 5. Gauntlet C Verification (Three.js 0.165.0 WebGL Shader & Clamped Buoyancy)
bash benchmarks/gauntlet_c_aquarium/contract.sh

# 6. Historical Phase Compatibility Gates (Phases 50, 54, 55, 57, and 58)
bash phases/phase_54_agent_harness_evaluation_and_128k_realism/03_verify/contract.sh
bash phases/phase_55_icm_tripartite_scaffolding_and_v45_sealing/03_verify/contract.sh
bash phases/phase_58_autonomous_icm_factory_and_multi_gauntlet_certification/03_verify/contract.sh

# 7. Master Makefile Suite (Exit status check: $?)
make all
```
