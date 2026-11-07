# Document 02: Jake Van Clief ICM Tooling & Workspace Reorganization Specifications

> **Standard**: ASD-STE100 (Simplified Technical English)  
> **Release Package**: GDR37  
> **Theoretical Foundation**: Jake Van Clief & David McDermott (arXiv:2603.16021)  
> **Tool Sources**: `ktncodes/icm-template` and `RinDig/icm-architect`  
> **Status**: Architectural Specification  

---

## 1. Executive Summary

This document specifies the tooling and organizational principles of Interpretable Context Methodology (ICM).
It explains how to apply Jake Van Clief's automated setup and synchronization commands.
It provides the foundation to reorganize the `ws-hermes` workspace into a clean, unified architecture.
It defines strict safety rules to guarantee that cleanup actions do not break runtime systems.

---

## 2. Core ICM Principles

1. **One Stage, One Job**:
   - Each folder executes a single, bounded contract.
   - A stage that inspects state does not write code.
   - A stage that calculates math does not dispatch actions.

2. **Plain Text as Universal Interface**:
   - Stages communicate exclusively through markdown and JSON files.
   - There are zero proprietary binary formats or closed databases between stages.

3. **Layered Context Loading**:
   - Agents read downward through five layers and stop when they have what they need.
   - Layer 0: Where am I? (< 60 lines, ~800 tokens).
   - Layer 1: Where do I go? (< 80 lines, ~300 tokens).
   - Layer 2: What do I do? (< 80 lines, 200-500 tokens).
   - Layer 3: What rules apply? (500-2,000 tokens).
   - Layer 4: What am I working with? (Working deliverables).

4. **Every Output is an Edit Surface**:
   - Humans can inspect, modify, and save any intermediate file before the next stage runs.

5. **Configure the Factory, Not the Product**:
   - Layer 3 rules and conventions stay constant across runs.
   - Each execution produces clean Layer 4 deliverables using the existing factory.

---

## 3. Automated ICM Skills & Commands

The `ktncodes/icm-template` repository provides three primary agent skills:

| Command / Skill | Execution Purpose | Operating Behavior |
| :--- | :--- | :--- |
| `/icm-scaffold` | Initial Workspace Setup | Analyzes workspace. Generates `IDENTITY.md`, `CONTEXT.md`, and `_config/`. Supports **Quick Mode** (3 layers, zero restructuring) and **Full Mode** (5 layers with stage folders). |
| `/icm-sync` | Routing Synchronization | Scans disk changes. Updates the routing tables in `IDENTITY.md` and `CONTEXT.md` to match physical folders. |
| `/icm-context-scaffold` | Gap Remediation | Scans the directory tree. Generates missing stage `CONTEXT.md` files with canonical contracts. |

---

## 4. ICM Architect Tooling Scripts

The `RinDig/icm-architect` skill contains deterministic Python validators:

- **`scripts/index.py`**: Builds the hierarchical context map across all layers.
- **`scripts/links.py`**: Verifies every relative Markdown file link across stages.
- **`scripts/quotes.py`**: Verifies citation parity and ensures quotes match source text.
- **`scripts/viz.py`**: Generates Mermaid sequence and flowchart diagrams of the pipeline.

---

## 5. Unified Workspace Organization Model

To eliminate clutter and enforce **One Fact, One Home**, the repository must be organized into four logical zones:

### Zone 1: Orchestration & Factory Core (Layers 0, 1, 3)
- `AGENTS.md` (canonical Layer 0)
- `CONTEXT.md` (canonical Layer 1 router)
- `_config/` (invariants, conventions, hardware limits, glossary)
- `_templates/` (contract and checkpoint templates)
- `_tools/` (deterministic validators and test scripts)
- `shared/` (mathematical, vision, netcode, and shader schemas)

### Zone 2: Sequential Execution Stages (Layers 2, 4)
- `stages/`
  - `01-probe/`: Reconnaissance and environment inspection.
  - `02-controller/`: Math, OpenCV calibration, and controller logic.
  - `03-execute/`: Autonomous execution, CDP actions, and performance tracking.

### Zone 3: Benchmarks & Historical Verification (Layer 4)
- `benchmarks/`
  - `gauntlet_a_voxel_fps/`: 20 Hz multiplayer FPS gauntlet.
  - `gauntlet_b_splatbox/`: OpenCV centroid tracking gauntlet.
  - `gauntlet_c_aquarium/`: Three.js shader aquarium gauntlet.
- `phases/`: Sealed verification registry (Phases 1 through 58).
- `phases/status_ledger.json`: Master receipt database.

### Zone 4: Research, Memory, & Substrate Layer
- `references/`: Upstream manuals and theoretical papers.
- `skills/`: Agent skills directory (`icm-architect`, `icm-stage-compiler`).
- `.config/`: Systemd services (`hermes-llama-server.service`, `hermes-openviking.service`).
- `.local/bin/`: Daemon binaries and launch scripts.
- `.hermes/`: Substrate configuration (`config.yaml`, rules, memories, and skills).

---

## 6. Non-Breaking Migration & Cleanup Safety Architecture

Reorganizing a production repository requires strict safety boundaries.
We establish these non-negotiable rules to ensure zero regressions:

### 6.1 The Immutable Keep-Out Inventory (Do Not Delete or Move)

These components are essential for system operation and must remain in their established locations:

| System Component | Established Path | Invariant Reason |
| :--- | :--- | :--- |
| **Inference Daemon Service** | `.config/systemd/user/hermes-llama-server.service` | Bound to systemd user manager. Required for local Port 8138 inference. |
| **Memory Daemon Service** | `.config/systemd/user/hermes-openviking.service` | Bound to systemd user manager. Required for local Port 1933 memory. |
| **Inference Daemon Binary** | `.local/bin/llama-server` | Configured with exact CPU affinity (cores 0-5), 128K context, and MTP drafter. |
| **Agent Configuration** | `.hermes/config.yaml` | Canonical upstream configuration version 46. |
| **Upstream Submodule** | `.hermes/hermes-agent` | Enforces Rule 9 (Substrate Purity). Must contain 0 modified files. |
| **Layer 0 Map** | `AGENTS.md` | Primary Layer 0 operating protocol (< 60 lines). |
| **Layer 1 Router** | `CONTEXT.md` | Root task router (< 80 lines). |
| **Verification Ledger** | `phases/status_ledger.json` | Master cryptographic receipt database for Phases 1 to 58. |
| **Phase Verification Gates** | `phases/phase_*/03_verify/contract.sh` | Deterministic verification contracts for all 58 sealed phases. |
| **Active Gauntlets** | `benchmarks/gauntlet_a_voxel_fps/`<br>`benchmarks/gauntlet_b_splatbox/`<br>`benchmarks/gauntlet_c_aquarium/` | Certified testbeds for netcode, computer vision, and WebGL shaders. |

### 6.2 The Four-Category Triage Framework

Every file in the repository must be assigned to one of four triage categories:

1. **Category A: Retain In Place (Critical Substrate Core)**
   - Components from the Keep-Out Inventory.
   - Core root configuration: `Makefile`, `.gitignore`, `pyproject.toml`, `package.json`.

2. **Category B: Consolidate to ICM Factory (Layer 3 Architecture)**
   - Scattered documentation moved into `_config/` or `shared/`.
   - Ad-hoc scripts moved into `_tools/`.
   - Example: Move domain invariants to `_config/invariants.md`.

3. **Category C: Archive to Historical Vault (Zero Context Clutter)**
   - Completed evaluation dumps, old test artifacts, and legacy benchmark reports.
   - Relocated into `archive/` or retained inside corresponding `phases/`.
   - Leaves the workspace root clean and readable.

4. **Category D: Prune / Safe Deletion**
   - Stale build caches, empty temporary directories, and duplicate backups.
   - Pruning occurs only after confirming zero references in contracts or scripts.

### 6.3 Phased Verification Protocol

Every relocation must follow a five-step execution cycle:
1. **Pre-Flight Check**: Verify that `python3 _tools/hermes_icm_validator.py` and `git status` pass.
2. **Atomic Git Move**: Use `git mv <source> <destination>` to preserve commit history.
3. **Compatibility Bridge**: When scripts expect a legacy path, deploy a relative symlink.
4. **Post-Move Gate Verification**: Execute `bash phases/phase_58_.../03_verify/contract.sh` to confirm zero broken dependencies.
5. **Rollback Assurance**: Every relocation must have a defined reverse command (`git mv <destination> <source>`).
