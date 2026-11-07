# Master Consultation Brief: Autonomous ICM Repository Organization & System Safeguards (GDR37)

> **To**: Lead Architect Argon (Gemini Argon / High Thinking)  
> **From**: Antigravity Pair-Programming Agent (Autonomous Substrate Engine)  
> **Release Package**: GDR37  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Engine**: Gemma 4 Exact (`gemma-4-E4B-it-q4_0-exact.gguf` + MTP Drafter)  
> **Context Window**: 131,072 tokens (128K context, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Envelope**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, 4,997 MiB allocated)  
> **Workspace Root**: `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes` (`ws-hermes`)  
> **Status**: Phase 58 Sealed | Gauntlets A, B, C Operational | Native Git Operational  

---

## 1. Executive Summary & Context

In GDR36, Argon delivered the 5-layer Interpretable Context Methodology (ICM) blueprint and sealed Phase 58.
In this session, the engineering team executed the physical deployment:
1. Configured the Gemma 4 Exact model with 128K context and TurboQuant KV cache on Port 8138.
2. Repaired Gauntlet A (20 Hz netcode), Gauntlet B (OpenCV HoughCircles), and Gauntlet C (Three.js aquarium shader).
3. Converted the workspace from chezmoi dotfiles into a clean, native Git repository at `https://github.com/imshubhamsocial/ws-hermes`.
4. Ingested all historical research packages (`GDR30` through `GDR37`) under `docs/research/`.

We now commission Lead Architect Argon to author the complete, non-breaking repository reorganization plan.

---

## 2. Ingested Repository Context

The full `ws-hermes` repository snapshot is already loaded into your memory via the **Import code** feature.
You have direct, immediate access to:
1. **System Invariants & Configs**: `_config/`, `IDENTITY.md`, `CONTEXT.md`, `AGENTS.md`.
2. **Deterministic Stages & Benchmarks**: `stages/`, `benchmarks/`, `phases/status_ledger.json`.
3. **Execution Tools**: `_tools/hermes_stage_runner.py`, `_tools/hermes_icm_validator.py`.
4. **Historical Research Packages**: `docs/research/GDR30` through `docs/research/GDR37`.

You do not need external file uploads. All facts and code exist in your loaded context.

---

## 3. Four Core Architectural Mandates for Lead Architect Argon

### Mandate 1: Pre-Migration Safety Audit (Keep-Out Inventory)
Protect runtime services and hardware bounds:
- Port 8138: Local inference daemon (`hermes-llama-server.service`).
- Port 1933: Hierarchical memory server (`hermes-openviking.service`).
- Port 8642: Hermes Gateway daemon.
- Port 9222: Chrome CDP headless service.
- Upstream Submodule: `.hermes/hermes-agent` must maintain 100% clean git status (0 unstaged changes).
- Status Ledger: `phases/status_ledger.json` and all verification contracts in `phases/` must remain valid.

### Mandate 2: Four-Category Triage Classification
Inspect all tracked repository files and classify each into:
- **Category A (Retain In Place)**: Core substrate files, Layer 0 map (`AGENTS.md`), Layer 1 router (`CONTEXT.md`), build files (`Makefile`), and systemd units.
- **Category B (Consolidate to ICM Factory)**: Move domain rules to `_config/`, schemas to `shared/`, and audit scripts to `_tools/`.
- **Category C (Archive to Historical Vault)**: Relocate legacy test run outputs and old logs into `archive/` or corresponding `phases/`.
- **Category D (Prune / Safe Deletion)**: Remove stale temporary caches and empty directories without active references.

### Mandate 3: Structured, Actionable Migration Table
Deliver the migration plan as an explicit mapping table:
`| Original Path | Destination Path | Triage Category | Rationale / Invariant | Exact Git Command | Verification Check | Rollback Command |`

### Mandate 4: Post-Migration Health Verification Suite
Define the exact, sequential verification suite to confirm complete system integrity:
1. `python3 _tools/hermes_icm_validator.py` (0 errors).
2. `bash benchmarks/gauntlet_a_voxel_fps/contract.sh` (PASS).
3. `bash benchmarks/gauntlet_b_splatbox/contract.sh` (PASS).
4. `bash benchmarks/gauntlet_c_aquarium/contract.sh` (PASS).
5. `bash phases/phase_58_.../03_verify/contract.sh` (PASS).
