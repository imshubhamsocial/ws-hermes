# Deterministic ICM Tool Suite Reference Manual

**Substrate**: Interpretable Context Methodology (ICM) Layer 3 Tools  
**Primary Locations**: `~/.hermes/tools/icm/` and `.hermes/tools/icm/`  
**Language Standard**: ASD-STE100  
**Parent Index**: [docs/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/README.md)

---

## 1. Tool Suite Overview

Layer 3 provides deterministic Python and Bash verification tools.  
These tools enforce contracts, line ceilings, substrate purity, and VRAM ceilings.  
All tools are atomic scripts containing strictly fewer than 60 lines.

---

## 2. Tool Reference Catalog

### 1. [audit_hermes_home.sh](file:///var/home/imshubhamsocial/.hermes/tools/icm/audit_hermes_home.sh)
* **Function**: Enforces Rule 9 (Substrate Purity) and Rule 6 (60-line ceiling).
* **Checks**:
  1. Checks `~/.hermes/hermes-agent` for zero git modifications (`git status --porcelain`).
  2. Scans custom scripts in `profiles/`, `tools/`, and `skills/` for lines $\ge 60$.
* **Exit Codes**: `0` on clean pass; `1` on dirty git status or line violations.
* **Line Count**: 36 lines.

### 2. [check_vram_limit.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/check_vram_limit.py)
* **Function**: Enforces GPU VRAM ceiling ($5,800.0$ MiB max).
* **Method**: Queries `nvidia-smi` across active GPU processes.
* **Exit Codes**: `0` if VRAM $\le 5,800.0$ MiB; `1` if VRAM exceeds ceiling.
* **Line Count**: 42 lines.

### 3. [egm_goldfish_gate.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/egm_goldfish_gate.py)
* **Function**: Stateless Goldfish specification review gate.
* **Lenses**: Evaluates specification against Comprehension, Design, and Readiness rubrics.
* **Output**: Generates `goldfish_review_report.json` with PASS/FAIL verdict.
* **Line Count**: 58 lines.

### 4. [hermes_icm_validator.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/hermes_icm_validator.py)
* **Function**: Validates root workspace structure, line ceilings, and required section headers.
* **Checks**:
  1. Core files: `AGENTS.md`, `CONTEXT.md`, `Makefile`.
  2. Script line counts ($\le 59$ lines).
  3. Header presence: Identity, Directory Locations, 10 Compiler Rules.
* **Exit Codes**: `0` on full compliance; `1` if any check fails.
* **Line Count**: 57 lines.

### 5. [hermes_stage_runner.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/hermes_stage_runner.py)
* **Function**: Deterministic test runner for single-pass stages.
* **Execution**: Locates verification scripts inside target stage and runs them in a clean subshell.
* **Line Count**: 57 lines.

### 6. [icm_context_auditor.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/icm_context_auditor.py)
* **Function**: Audits token budgets across ICM layers.
* **Budgets**: Layer 0 ($\le 800$ tokens), Layer 1 ($\le 300$ tokens), Layer 2 ($\le 500$ tokens).
* **Line Count**: 55 lines.

### 7. [icm_repo_migrator.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/icm_repo_migrator.py)
* **Function**: AST-based repository classifier for brownfield migrations.
* **Output**: Emits `migration_map.json` classifying files into catalog, contract, factory, product, or dead.
* **Line Count**: 58 lines.

### 8. [icm_scaffolder.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/icm_scaffolder.py)
* **Function**: Generates the 5-layer ICM directory hierarchy for greenfield repositories.
* **Line Count**: 54 lines.

### 9. [run_multi_stage.sh](file:///var/home/imshubhamsocial/.hermes/tools/icm/run_multi_stage.sh)
* **Function**: Headless clean-session runner executing stages sequentially with `--no-session-persistence`.
* **Line Count**: 26 lines.

### 10. [verify_stage.py](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py)
* **Function**: Verifies a single stage folder contract, inputs, and outputs.
* **Line Count**: 39 lines.

---

## 3. Automation Make Targets

All primary verification tools are wired directly into the root [Makefile](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/Makefile):

```bash
make walk-test      # Runs hermes_icm_validator.py
make check-vram     # Runs check_vram_limit.py
make audit-home     # Runs audit_hermes_home.sh
make gauntlets      # Runs all Gauntlet verification suites
make all            # Executes all audits and verification targets
```
