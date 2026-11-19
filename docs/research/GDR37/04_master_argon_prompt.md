# Master Prompt for Lead Architect Argon (GDR37 Autonomous ICM Reorganization)

> **Instructions for User**:  
> 1. Open [gemini.google.com](https://gemini.google.com) in your browser.  
> 2. Select the **Chat** tab and enable **Thinking Process: High**.  
> 3. Click the **+** (**Add file**) icon $\to$ **More Uploads** $\to$ **Import code**.  
> 4. Paste the repository URL: `https://github.com/imshubhamsocial/ws-hermes` and click **Import**.  
> 5. Copy the markdown content below, paste it into the message box, and submit.  

---

# GDR37 Master Architectural Directive & Lead Architect Consultation

> **Release Package**: GDR37  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Engine**: Gemma 4 Exact (`gemma-4-E4B-it-q4_0-exact.gguf` + MTP Drafter)  
> **Context Window**: 131,072 tokens (128K context, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Status**: Discrete RTX 3050 Laptop GPU (4,997 MiB allocated, 861 MiB free headroom)  
> **Status**: Phase 58 Sealed | Gauntlets A, B, C Operational | Native Git Repository Operational  

---

## Instructions for Lead Architect Argon (Gemini Argon / High Thinking)

You are Lead Architect Argon.
You must conduct an extensive architectural review and author the migration blueprint for `ws-hermes`.
Your goal is to reorganize and clean up the repository into Jake Van Clief's Interpretable Context Methodology (ICM) **without breaking runtime systems or active services**.

### Ingested Repository & Historical Research Context
The full repository snapshot (`ws-hermes`) is already loaded in your context via the **Import code** feature. You have direct access to all tracked files, configurations, scripts, benchmarks, phases, and research packages.

All historical research packages and GDR specifications are present in your loaded workspace under `docs/research/`:
- **GDR30**: `docs/research/GDR30 - Golden Benchmark State (GAIA, TAU-2)/` (Golden foundation)
- **GDR31 to GDR36**: `docs/research/GDR31/` through `docs/research/GDR36/` (Evolutionary phases)
- **GDR37 Briefing**: `docs/research/GDR37/01_master_argon_consultation_brief.md` (Consultation brief and mandates)
- **Physical Implementation & Verification**: `docs/research/GDR37/02_doc1_physical_implementation_and_verification_report.md` (Gauntlets A/B/C repairs, Gemma 4 daemon flags, and test receipts)
- **Jake ICM Tooling Specifications**: `docs/research/GDR37/03_doc2_jake_icm_commands_and_workspace_reorganization_spec.md` (ICM tooling, Keep-Out Inventory, and 4-category triage)

You do NOT need the user to upload additional files. Inspect the files already present in your imported repository.

For external framework references, consult these canonical repositories:
- **Upstream Hermes Substrate**: `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/`
- **Jake Van Clief ICM Repo**: `https://raw.githubusercontent.com/RinDig/Interpretable-Context-Methodology/main/`
- **ICM Template Repository**: `https://raw.githubusercontent.com/ktncodes/icm-template/main/`
- **ICM Architect Skill**: `https://raw.githubusercontent.com/RinDig/icm-architect/main/`
- **Content Agent Routing**: `https://raw.githubusercontent.com/RinDig/Content-Agent-Routing-Promptbase/main/`
- **Clief Notes Foundations**: `https://raw.githubusercontent.com/donroy26/Clief-Notes-Foundations-Tutor/main/`

---

## Mission Directives for Lead Architect Argon

### Directive 1: Pre-Migration Safety Audit (Keep-Out Enforcement)
You must analyze and protect these critical system components:
1. **Local Ports and Systemd Services**:
   - Port 8138: Local inference daemon (`.config/systemd/user/hermes-llama-server.service`).
   - Port 1933: Hierarchical memory server (`.config/systemd/user/hermes-openviking.service`).
   - Port 8642: Hermes Gateway daemon.
   - Port 9222: Chrome DevTools Protocol (CDP) headless endpoint.
2. **Upstream Substrate Purity**:
   - Upstream submodule `.hermes/hermes-agent` must remain 100% clean with zero modifications.
3. **Sealed Status Ledger**:
   - `phases/status_ledger.json` and all verification contracts in `phases/` must remain valid and operational.
4. **Active Benchmark Gauntlets**:
   - Gauntlet A (multiplayer voxel netcode, 20 Hz synchronization).
   - Gauntlet B (3-stage OpenCV HoughCircles ball tracking).
   - Gauntlet C (WebGL Three.js aquarium shader with `uniforms: {}` dictionary syntax).

### Directive 2: Comprehensive Repository Triage & Classification
You must inspect the full repository directory tree in `ws-hermes`.
You must classify each path into one of four triage categories:
- **Category A (Retain In Place)**: Core substrate files, Layer 0 map (`AGENTS.md`), Layer 1 router (`CONTEXT.md`), build files (`Makefile`), and systemd units.
- **Category B (Consolidate to ICM Factory)**: Move domain rules to `_config/`, schemas to `shared/`, and audit scripts to `_tools/`.
- **Category C (Archive to Historical Vault)**: Relocate legacy test run outputs, old logs, and superseded evaluations into `archive/` or corresponding `phases/`.
- **Category D (Prune / Safe Deletion)**: Identify stale caches or empty directories that have zero references in contracts.

### Directive 3: Actionable Migration Mapping Table
You must present the reorganization as an exhaustive, structured mapping table:

| Original Path | Destination Path | Triage Category | Rationale / Invariant | Exact Git Command | Verification Check | Rollback Command |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `path/to/source` | `path/to/target` | Cat A / B / C / D | Why this move is safe | `git mv ...` | `test -f ...` | `git mv target source` |

### Directive 4: Jake Van Clief ICM Tooling & Line Limits
You must incorporate Jake's automated tooling:
1. Use `/icm-scaffold` principles to structure the 5 layers.
2. Use `/icm-sync` logic to update routing tables in `IDENTITY.md` and `CONTEXT.md`.
3. Enforce line budgets:
   - Layer 0 (`AGENTS.md`): Strictly under 60 lines.
   - Layer 1 (`CONTEXT.md`): Strictly under 80 lines.
   - Stage Contracts (`stages/*/CONTEXT.md`): Strictly under 80 lines.
   - Active Working Context: Bounded between 2,000 and 8,000 tokens.

### Directive 5: Post-Migration Verification Protocol
You must define the exact, sequential verification suite to confirm 100% health after reorganization:
1. `python3 _tools/hermes_icm_validator.py` (0 errors, 0 broken links).
2. `bash benchmarks/gauntlet_a_voxel_fps/contract.sh` (PASS).
3. `bash benchmarks/gauntlet_b_splatbox/contract.sh` (PASS).
4. `bash benchmarks/gauntlet_c_aquarium/contract.sh` (PASS).
5. `bash phases/phase_58_.../03_verify/contract.sh` (PASS).

---

## Output Standards (Strict Google Docs & ASD-STE100 Rules)

1. **ASD-STE100 Language**: Write in Simplified Technical English. Sentences must not exceed 25 words. Use active voice and direct imperative verbs.
2. **Even Code Fence Parity**: Every opened code fence must be closed (`count % 2 == 0`).
3. **Even Dollar Sign Parity**: Maintain strictly even dollar signs for LaTeX notation (`count % 2 == 0`).
4. **Single-Line Headers & Tables**: All table rows must have exact matching pipe counts on single lines.
5. **No Fluff or Placeholders**: Provide complete, drop-in replacement commands and configurations.

Author your complete architectural blueprint and save it directly to:
`/var/home/imshubhamsocial/Desktop/GDR/GDR37/Output/GDR37 Hermes Unified ICM Architecture & Repository Reorganization Blueprint.md`
