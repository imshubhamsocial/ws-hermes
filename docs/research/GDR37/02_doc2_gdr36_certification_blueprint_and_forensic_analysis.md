# Document 02: GDR36 Certification Blueprint & Forensic Analysis

> **Standard**: ASD-STE100 (Simplified Technical English)  
> **Release Package**: GDR37  
> **Source Documents**: `GDR36 Hermes Architecture & Certification.md` and `GDR36_ANALYSIS.md`  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44  
> **Hardware Status**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB GDDR6)  
> **Status**: Verified Historical Blueprint  

---

## 1. Executive Summary

This document presents the complete findings from GDR36.
GDR36 established the autonomous 5-layer Interpretable Context Methodology (ICM) architecture.
It resolved the gap between passing static audits and failing visual runtimes.
It sealed Phase 58 in the project status ledger.

---

## 2. The 5-Layer ICM Operating Architecture

| Layer | Primary File | Core Question | Line / Token Budget | Content Scope |
| :--- | :--- | :--- | :--- | :--- |
| **Layer 0** | `AGENTS.md` | Where am I? | < 60 lines (~800 tokens) | Operating protocol, workspace map, 10 compiler rules. |
| **Layer 1** | Root `CONTEXT.md` | Where do I go? | < 80 lines (~300 tokens) | Task router mapping intents to stages. |
| **Layer 2** | Stage `CONTEXT.md` | What do I do? | < 80 lines (200-500 tokens) | Single stage contract with explicit Inputs, Process, and Outputs. |
| **Layer 3** | `_config/`, `shared/` | What rules apply? | Bounded (500-2,000 tokens) | Invariants, schemas, mathematical conventions. |
| **Layer 4** | `output/`, `phases/` | What am I working with? | Working artifacts | Concrete deliverables produced during execution. |

---

## 3. The Ten Non-Negotiable Compiler Rules

1. **One Stage, One Job**: Execute only the contract inside the target folder's `CONTEXT.md`.
2. **Bounded Context (2,000-8,000 Tokens)**: Load only the exact file paths and sections listed in Inputs.
3. **One Fact, One Home**: Never duplicate rules from `_config/invariants.md`. Link to them.
4. **Docs Over Outputs**: Learn patterns from Layer 3 (`_config/`, `shared/`, `references/`), never from prior outputs.
5. **Read Before Edit**: Always call `read_file` on a target file in the current session before editing it.
6. **Atomic Scripts**: Author modular Python and shell scripts strictly under 60 lines.
7. **Browser Verification**: Use Playwright (`connect_over_cdp` or headless Chromium) to verify 0 runtime errors.
8. **Fresh Context Auditing**: Never grade your own output in the generating context; use `_tools/` check gates.
9. **Substrate Purity**: Never modify files inside `/var/home/imshubhamsocial/.hermes/hermes-agent`.
10. **Mandatory ASD-STE100 & Google Docs Safety**: Use Simplified Technical English and even fence/dollar parity.

---

## 4. Four-Tier Skill Precedence Hierarchy

Hermes searches and loads skills using this strict precedence order:
1. **Tier 1 (Project Workspace)**: `./skills/` inside the current workspace. Highest priority.
2. **Tier 2 (User Local Directory)**: `~/.hermes/skills/` in the user home environment.
3. **Tier 3 (Skills Create Directory)**: The directory defined by `skills.create_dir` in `config.yaml`.
4. **Tier 4 (External Directories)**: Folders configured under `skills.external_dirs` (e.g. `~/.agents/skills`).

---

## 5. Security Scanning and Quarantine Trajectory

1. Upstream `hermes skills install` executes an AST security scanner before activating any skill.
2. Cloned skills containing system modification logic trigger the `agent_config_mod` security flag.
3. In `references/system-map.md` (line 61), dangerous skills are quarantined to prevent prompt injection.
4. To ensure substrate safety, clone skills manually and enforce read-only filesystem permissions:
   ```bash
   chmod -R a-w ~/.agents/skills/icm-architect
   ```

---

## 6. The "Green Audit, Broken Runtime" Gap: Five Failure Modes

1. **Static Syntax Pass with Broken WebGL Shaders**: Python linting passes, but Three.js shader materials crash in the browser.
2. **CDP Port Binds with Zero-Pixel Canvas**: Chrome CDP endpoint responds on port 9222, but the target canvas has dimensions of 0x0 pixels.
3. **Network Socket Connects with Desynchronized Protocol**: WebSocket connects, but the packet payload does not match the 20 Hz synchronization tick.
4. **Mock Script Returns Fake Exit 0**: A test script prints `PASS` without verifying actual browser frames.
5. **Context Window Exceeds VRAM Ceiling**: Token budget expands beyond hardware limits, causing CUDA out-of-memory errors.

---

## 7. The U-Shaped Human Curve

Empirical data across 30 of 33 practitioners demonstrates that human intervention is not uniform:
- **Stage 1 (Reconnaissance / Probe)**: 92% human intervention. Humans must define the environment and goals.
- **Stage 2 (Calibration / Controller)**: 30% human intervention. Deterministic mathematical routines run autonomously.
- **Stage 3 (Production / Execute)**: 78% human intervention. Humans review final deliverables and certify quality.

---

## 8. The Eight-Point Walk Test

Every stage and release must pass the 8-Point Walk Test:
1. **Layer 0 Integrity**: `AGENTS.md` exists and contains fewer than 60 lines.
2. **Layer 1 Routing**: Root `CONTEXT.md` contains keyword triggers and fewer than 80 lines.
3. **Layer 2 Contract Conformity**: Stage `CONTEXT.md` defines clear Inputs, Process, Outputs, and Check sections.
4. **VRAM Quiescence**: Live GPU memory usage stays below 5,120 MiB during idle state.
5. **Substrate Purity**: `git status` on `.hermes/hermes-agent` returns 0 modified files.
6. **Browser Runtime Verification**: Playwright headless audit completes with 0 console errors.
7. **Atomic Script Limit**: Every authored Python and POSIX script stays strictly under 60 lines.
8. **Status Ledger Receipt**: `phases/status_ledger.json` records clean verification hashes.
