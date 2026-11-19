# Hermes ICM Operations and Self-Learning Manual

**Document Version**: 2.0.0  
**Language Standard**: ASD-STE100 (Simplified Technical English)  
**Target Platform**: Fedora Kinoite 44 (x86_64) | ws-hermes Distrobox  
**Canonical File Location**: [LEARNING.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/research/GDR40/Output/LEARNING.md)

---

## 1. Architectural Foundation: Profiles Over Raw Commands

Raw terminal commands bypass agent reasoning. They fail to generate auditable execution traces.  
Running planning, scaffolding, migration, and auditing in one shared session causes context pollution.

Hermes Agent OS solves this problem with isolated profiles in [~/.hermes/profiles/](file:///var/home/imshubhamsocial/.hermes/profiles/).  
Each profile enforces the Single Responsibility Principle:

| Profile Name | Model Assigned | Parameters (Google Defaults) | Persona Document | Operational Role |
| :--- | :--- | :--- | :--- | :--- |
| **`icm-planner`** | `gemma-4-E4B-it-qat-exact` | Default Google Values (`temperature: 0.7`) | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-planner/SOUL.md) | Socratic spec interviewer and Goldfish review controller. |
| **`icm-scaffolder`** | `gemma-4-E4B-it-qat-exact` | Default Google Values (`temperature: 0.7`) | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-scaffolder/SOUL.md) | Greenfield 5-layer workspace generator and contract compiler. |
| **`icm-migrator`** | `gemma-4-E4B-it-qat-exact` | Default Google Values (`temperature: 0.7`) | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-migrator/SOUL.md) | Brownfield AST 5-bucket classifier and module refactorer. |
| **`icm-auditor`** | `gemma-4-E4B-it-qat-exact` | Default Google Values (`temperature: 0.7`, Read-Only) | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-auditor/SOUL.md) | Deterministic token, line-ceiling, and substrate auditor. |

> [!NOTE]
> All profile bots standardize on the Google Gemma 4 Exact model (`gemma-4-E4B-it-qat-exact`) with native Google generation parameters (`temperature: 0.7`). Standard Google values maintain creative, natural, and expressive reasoning across all tasks, while deterministic ICM shell gates (`contract.sh`, `hermes_icm_validator.py`, `egm_goldfish_gate.py`) enforce strict architectural invariants.

Hermes provides two execution surfaces:
1. **Direct CLI Mode**: Run isolated commands with `hermes -p <profile>`.
2. **Inside-Hermes Mode**: Use slash commands, `@bot` messaging mentions, `delegate_task`, or `/kanban`.

---

## 2. Task 1: Greenfield Setup (Create Fresh ICM Repository)

This workflow transforms a project concept into a verified 5-layer ICM workspace.

### A. Directory Structure Before Scaffolding

The target directory begins completely empty:

```text
target_workspace/
└── (empty: 0 directories, 0 files)
```

### B. Live Command Execution & Hermes Agent Output

#### Step 1: Conduct Socratic Interview and Compile Specification
Run the `icm-planner` profile to author `stages/01-spec/CONTEXT.md`:
```bash
hermes -p icm-planner chat -q "Read CONTEXT.md. Interview me for project 'aquarium-sim' and author stages/01-spec/CONTEXT.md." --oneshot -Q
```

Live Hermes Agent response:
```text
I am icm-planner, the deep-context Socratic specification architect for the ICM pipeline.
I will read CONTEXT.md, review your domain constraints, and compile stages/01-spec/CONTEXT.md.
```

#### Step 2: Subject the Specification to the Goldfish Gate
Execute the stateless Goldfish comprehension review:
```bash
python3 ~/.hermes/tools/icm/egm_goldfish_gate.py stages/01-spec/CONTEXT.md
```

Deterministic gate output (`stages/01-spec/output/goldfish_review_report.json`):
```json
{
  "spec_file": "stages/01-spec/CONTEXT.md",
  "status": "PASS",
  "missing_sections": [],
  "lens_reviews": [
    {"lens": "comprehension", "blocker": false, "findings": "Spec defines all inputs, process steps, and outputs clearly."},
    {"lens": "design_critic", "blocker": false, "findings": "Math PDEs and VRAM limits (<=5800 MiB) audited with 0 blockers."},
    {"lens": "readiness", "blocker": false, "findings": "Exact file paths and POSIX contract gates verified."}
  ]
}
```

#### Step 3: Scaffold the 5-Layer Hierarchy
Run the `icm-scaffolder` profile to generate the filesystem layout:
```bash
hermes -p icm-scaffolder chat -q "Explain how you scaffold a fresh 5-layer ICM repository from an approved Stage 01 specification." --oneshot -Q
```

Live Hermes Agent response:
```text
As the icm-scaffolder, I follow a strict four-step execution procedure:
1. Specification Verification: Verify that stages/01-spec/output/goldfish_review_report.json equals PASS.
2. Core Scaffolding Execution: Run ~/.hermes/tools/icm/icm_scaffolder.py against the target workspace root.
3. Layer Population: Generate Layer 0 (IDENTITY.md), Layer 1 (CONTEXT.md), and Layer 2 stage contracts.
4. Tooling and Verification Wiring: Wire deterministic POSIX verification scripts into _tools/.
```

Execute the deterministic scaffolding tool directly:
```bash
python3 ~/.hermes/tools/icm/icm_scaffolder.py .
```

#### Step 4: Verify Scaffolding Contracts
Run the deterministic validator:
```bash
python3 ~/.hermes/tools/icm/hermes_icm_validator.py .
```

Deterministic tool JSON output:
```json
{
  "walk_test_passed": true,
  "error_count": 0,
  "errors": []
}
```

### C. Directory Structure After Scaffolding

The scaffolder builds a 19-directory, 9-file 5-layer hierarchy:

```text
target_workspace/
├── _config/
│   ├── conventions.md             # Layer 3: conventions & 60-line rule
│   ├── glossary.md                # Layer 3: domain & architecture glossary
│   └── hardware_ceilings.md       # Layer 3: RTX 3050 <= 5800 MiB ceiling
├── CONTEXT.md                     # Layer 1: universal task router
├── IDENTITY.md                    # Layer 0: spatial orientation map
├── setup/                         # Layer 3: environment setup manifests
├── shared/                        # Layer 3: cross-stage schemas and math
├── skills/                        # Layer 3: project-scoped domain skills
├── stages/                        # Layer 2: numbered stage contracts
│   ├── 01-spec/
│   │   ├── CONTEXT.md             # Stage 01 contract
│   │   ├── output/                # Stage 01 deliverable folder
│   │   └── references/            # Stage 01 reference docs
│   ├── 02-scaffold/
│   │   ├── CONTEXT.md             # Stage 02 contract
│   │   ├── output/                # Stage 02 deliverable folder
│   │   └── references/            # Stage 02 reference docs
│   ├── 03-implement/
│   │   ├── CONTEXT.md             # Stage 03 contract
│   │   ├── output/                # Stage 03 deliverable folder
│   │   └── references/            # Stage 03 reference docs
│   └── 04-verify/
│       ├── CONTEXT.md             # Stage 04 contract
│       ├── output/                # Stage 04 deliverable folder
│       └── references/            # Stage 04 reference docs
└── _tools/                        # Layer 3: deterministic test runners

19 directories, 9 files
```

### D. Inside-Hermes Mode (In-Chat Slash Commands & Bot Routing)

#### Option 1: Interactive Slash Command Sequence
```bash
# 1. Clean session wipe for planning
/new --yes setup-spec

# 2. Attach the deterministic Goldfish review quality gate
/goal gate add python3 ~/.hermes/tools/icm/egm_goldfish_gate.py stages/01-spec/CONTEXT.md

# 3. Launch bounded Socratic interview loop (max 8 turns)
/goal Conduct Socratic interview for my project, resolve all edge cases, and compile stages/01-spec/CONTEXT.md.

# 4. Clean up goal state upon PASS
/goal clear

# 5. Clean session wipe for scaffolding
/new --yes setup-scaffold

# 6. Attach deterministic ICM validator gate
/goal gate add python3 ~/.hermes/tools/icm/hermes_icm_validator.py .

# 7. Execute scaffolding
/goal Execute python3 ~/.hermes/tools/icm/icm_scaffolder.py . and verify all 5 layers exist.

# 8. Clean up goal state
/goal clear
```

#### Option 2: Messaging Gateway Routing (`@bot` mentions)
```text
@icm-planner Please interview me on architecture requirements and generate stages/01-spec/CONTEXT.md.
```
Once approved:
```text
@icm-scaffolder The spec report passed. Scaffold the 5-layer ICM structure in this directory.
```

#### Option 3: Multi-Profile Kanban Collaboration (`/kanban`)
```bash
/kanban create "Stage 01 Architecture Specification" --assignee icm-planner
/kanban create "Stage 02 Workspace Scaffolding" --assignee icm-scaffolder --parents t_spec01
```

---

## 3. Task 2: Brownfield Migration (Migrate Existing Messy Repository)

This workflow audits an unstructured codebase, classifies all files into 5 buckets, and decomposes monolithic files.

### A. Directory Structure Before Migration

The legacy codebase lacks layer separation and contains monolithic scripts:

```text
legacy_repository/
├── app_overview.md                # Unclassified architectural note
├── broken_syntax.py               # Syntax error file
├── dist/
│   └── bundle.js                  # Build product
├── legacy_backup.py.bak           # Obsolete backup file
├── math_utils.py                  # Utility module (7 lines)
├── monolithic_solver.py           # Large solver script (71 lines >= 60 lines)
├── output/
│   └── run_log.txt                # Prior execution log
├── README.md                      # Unstructured project readme
├── temp_scratch.tmp               # Temporary scratch file
└── test_solver.py                 # Unit test script (8 lines)

3 directories, 10 files
```

### B. Live Command Execution & Hermes Agent Output

#### Step 1: Execute AST Classification
Run `icm_repo_migrator.py` to classify files into the 5 ICM buckets:
```bash
python3 ~/.hermes/tools/icm/icm_repo_migrator.py .
```

Tool stdout trace:
```text
MIGRATION_MAP_READY: 10 files classified -> ./migration_map.json
```

Generated `migration_map.json`:
```json
{
  "root": "/path/to/legacy_repository",
  "classified": [
    {
      "bucket": "catalog",
      "reason": "index_router",
      "path": "legacy_repository/README.md",
      "lines": 2,
      "needs_split": false
    },
    {
      "bucket": "factory",
      "reason": "reference_or_source",
      "path": "legacy_repository/app_overview.md",
      "lines": 2,
      "needs_split": false
    },
    {
      "bucket": "dead",
      "reason": "syntax_error",
      "imports": [],
      "defs": 0,
      "path": "legacy_repository/broken_syntax.py",
      "lines": 2,
      "needs_split": false
    },
    {
      "bucket": "product",
      "reason": "run_artifact",
      "path": "legacy_repository/dist/bundle.js",
      "lines": 1,
      "needs_split": false
    },
    {
      "bucket": "dead",
      "reason": "obsolete_backup",
      "path": "legacy_repository/legacy_backup.py.bak",
      "lines": 1,
      "needs_split": false
    },
    {
      "bucket": "factory",
      "reason": "executable_module",
      "imports": ["math"],
      "defs": 2,
      "path": "legacy_repository/math_utils.py",
      "lines": 7,
      "needs_split": false
    },
    {
      "bucket": "factory",
      "reason": "executable_module",
      "imports": ["math"],
      "defs": 1,
      "path": "legacy_repository/monolithic_solver.py",
      "lines": 71,
      "needs_split": true
    },
    {
      "bucket": "product",
      "reason": "run_artifact",
      "path": "legacy_repository/output/run_log.txt",
      "lines": 1,
      "needs_split": false
    },
    {
      "bucket": "dead",
      "reason": "obsolete_backup",
      "path": "legacy_repository/temp_scratch.tmp",
      "lines": 1,
      "needs_split": false
    },
    {
      "bucket": "contract",
      "reason": "verification_gate",
      "imports": ["unittest"],
      "defs": 1,
      "path": "legacy_repository/test_solver.py",
      "lines": 8,
      "needs_split": false
    }
  ]
}
```

#### Step 2: Query the `icm-migrator` Profile
```bash
hermes -p icm-migrator chat -q "Explain how you classify an unstructured codebase into the 5 ICM buckets and handle files with needs_split=true." --oneshot -Q
```

Live Hermes Agent response:
```text
As the icm-migrator (Brownfield AST Repository Refactorer), I execute this procedure:
1. Run AST Classification: Execute ~/.hermes/tools/icm/icm_repo_migrator.py to generate migration_map.json.
2. Present Map for Human Approval: Present the 5 buckets (catalog, contract, factory, product, dead) to the engineer.
3. Decompose Monolithic Files: Decompose all source files with needs_split=true (>=60 lines) into atomic modules under 60 lines.
4. Relocate Assets: Move approved files to their canonical ICM destinations.
```

### C. Directory Structure After Migration

After migration and decomposition, the repository adheres to the 5-layer ICM structure:

```text
migrated_repository/
├── _config/
│   ├── conventions.md             # Rule 6 (<60 lines) and conventions
│   └── hardware_ceilings.md       # Hardware bounds
├── CONTEXT.md                     # Layer 1 router (migrated from README.md)
├── IDENTITY.md                    # Layer 0 spatial identity map
├── migration_map.json             # Certified AST classification audit
├── _quarantine/                   # Quarantined dead assets awaiting deletion
│   ├── broken_syntax.py           # Quarantined: syntax error
│   ├── legacy_backup.py.bak       # Quarantined: backup file
│   └── temp_scratch.tmp           # Quarantined: temporary scratch
├── shared/                        # Layer 3 factory code
│   ├── math_utils.py              # Atomic math utilities (7 lines)
│   ├── solver_core.py             # Decomposed solver module 1 (35 lines)
│   └── solver_step.py             # Decomposed solver module 2 (36 lines)
├── stages/
│   ├── 01-spec/
│   │   ├── CONTEXT.md
│   │   └── references/
│   │       └── app_overview.md    # Migrated from factory documentation
│   └── 04-verify/
│       ├── CONTEXT.md
│       └── test_solver.py         # Verification contract gate (8 lines)
└── output/                        # Layer 4 run products
    ├── dist/
    │   └── bundle.js
    └── run_log.txt
```

### D. Inside-Hermes Mode (In-Chat Slash Commands & Bot Routing)

#### Option 1: Interactive Slash Command Sequence
```bash
# 1. Clean session wipe for migration
/new --yes repo-migration

# 2. Attach verify-only AST quality gate
/goal gate add python3 ~/.hermes/tools/icm/icm_repo_migrator.py .

# 3. Launch migration goal
/goal Run AST repository classifier, produce migration_map.json, and decompose scripts over 59 lines.

# 4. View status of gate and turns
/goal status

# 5. Clear goal when completed
/goal clear
```

#### Option 2: Messaging Gateway Routing (`@bot` mentions)
```text
@icm-migrator Analyze current repository. Classify files into the 5 ICM buckets and present migration_map.json.
```
After review:
```text
@icm-migrator Approved. Decompose all scripts over 59 lines into atomic modules under 60 lines.
```

---

## 4. Task 3: Audit and Remediation (Fix Existing ICM Repositories)

Use this workflow to detect and fix broken invariants, line-ceiling violations ($\ge 60$ lines), missing headers, or substrate contamination.

### A. Live Command Execution & Hermes Agent Output

#### Step 1: Query the `icm-auditor` Profile
```bash
hermes -p icm-auditor chat -q "Explain how you audit a workspace and what blocking criteria you enforce." --oneshot -Q
```

Live Hermes Agent response:
```text
As the icm-auditor (Deterministic Read-Only Substrate Auditor), my function is strictly verification:
1. Layer Token Budget Verification: Execute ~/.hermes/tools/icm/icm_context_auditor.py.
2. Substrate Purity Check: Execute ~/.hermes/tools/icm/audit_hermes_home.sh to enforce Rule 9.
3. Code Line Length Enforcement: Verify every script is strictly under 60 lines.
4. Static Analysis: Run SkillEvaluator Tier 1 static checks across ~/.hermes/skills/icm/.
Blocking Criteria: VRAM > 5800.0 MiB, dirty files in ~/.hermes/hermes-agent, or failed gates.
```

#### Step 2: Run Gate 1 — Substrate Hygiene & Upstream Purity
```bash
bash ~/.hermes/tools/icm/audit_hermes_home.sh
```

Live audit execution trace:
```text
[AUDIT 1/4] Verifying Rule 9 Upstream Substrate Purity...
[AUDIT 2/4] Verifying Isolated Profile Fleet (.no-bundled-skills)...
[AUDIT 3/4] Enforcing <60 Line Atomic Ceiling on Custom ICM Scripts...
[AUDIT 4/4] Running Custom ICM Skill Unit Tests...
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```

#### Step 3: Run Gate 2 — Hardware VRAM Ceiling Check
```bash
python3 ~/.hermes/tools/icm/check_vram_limit.py --mode active
```

Live VRAM telemetry JSON output:
```json
{
  "mode": "active",
  "vram_used_mib": 5074.0,
  "vram_total_mib": 6144.0,
  "ceiling_mib": 5800.0,
  "headroom_mib": 726.0,
  "temperature_c": 61.41,
  "power_w": 15.81,
  "passed": true
}
```

#### Step 4: Run Gate 3 — Workspace Contracts and Walk Test
```bash
python3 ~/.hermes/tools/icm/hermes_icm_validator.py .
```

Live validator JSON output:
```json
{
  "walk_test_passed": true,
  "error_count": 0,
  "errors": []
}
```

### B. Directory State Before and After Remediation

#### Before Remediation: Line Ceiling Violation ($\ge 60$ lines)
A developer created a utility script exceeding the 59-line ceiling:
```text
tools/
└── data_processor.py              # 74 lines (VIOLATION: Rule 6 requires < 60 lines)
```

#### Remediation Execution
Run the `icm-migrator` profile to refactor the file:
```bash
hermes -p icm-migrator chat -q "Decompose tools/data_processor.py (74 lines) into atomic modules under 60 lines." --oneshot -Q
```

#### After Remediation: All Scripts Pass the Ceiling Gate
```text
tools/
├── data_cleaner.py                # 36 lines (< 60 lines: PASS)
└── data_transformer.py            # 38 lines (< 60 lines: PASS)
```

### C. Inside-Hermes Mode (In-Chat Slash Commands & Bot Routing)

```bash
# 1. Clean session wipe for remediation
/new --yes repo-remediation

# 2. Gate 1: Check substrate purity and line ceilings
/goal gate add bash ~/.hermes/tools/icm/audit_hermes_home.sh

# 3. Gate 2: Check ICM workspace contracts and headers
/goal gate add python3 ~/.hermes/tools/icm/hermes_icm_validator.py .

# 4. Gate 3: Check VRAM ceiling (< 5,800.0 MiB)
/goal gate add python3 ~/.hermes/tools/icm/check_vram_limit.py --mode active

# 5. Launch remediation goal
/goal Refactor all files violating line limits or missing headers until all quality gates pass.

# 6. Clear goal upon verification
/goal clear
```

---

## 5. Task 4: End-to-End Multi-Stage Execution & Bot Handoff

This workflow runs numbered stages sequentially while wiping the KV cache at every stage boundary.

### A. Directory Structure Before Execution

Before running the stage compiler, only stage contracts and inputs exist:

```text
stages/
├── 01-spec/
│   ├── CONTEXT.md                 # Stage 01 contract
│   └── output/                    # (empty)
├── 02-scaffold/
│   ├── CONTEXT.md                 # Stage 02 contract
│   └── output/                    # (empty)
├── 03-implement/
│   ├── CONTEXT.md                 # Stage 03 contract
│   └── output/                    # (empty)
└── 04-verify/
    ├── CONTEXT.md                 # Stage 04 contract
    ├── contract.sh                # Stage 04 verification gate
    └── output/                    # (empty)
```

### B. Live Command Execution & Autonomous Runner Output

#### Step 1: Run Multi-Stage Execution
Run `run_multi_stage.sh` or the autonomous stage runner:
```bash
python3 ~/.hermes/tools/icm/hermes_stage_runner.py --stage-dir stages/01-spec --verify-only
```

Stage runner telemetry output:
```json
{"stage": "01-spec", "verdict": "PASS", "checkpoint": "AUTO_APPROVED_BY_CONTRACT", "kv_erased": true}
```

The runner:
1. Erases the llama-server KV slot via `POST http://127.0.0.1:8138/slots/0?action=erase`.
2. Executes the bounded stage prompt.
3. Runs the stage `contract.sh`.
4. Emits `output/check.md` and `output/checkpoint.md`.
5. Wipes context again before advancing to Stage 02.

### C. Directory Structure After Multi-Stage Execution

After execution, all stage deliverables, check records, and production modules exist:

```text
stages/
├── 01-spec/
│   ├── CONTEXT.md
│   └── output/
│       ├── check.md               # Audit: PASS, contract_exit_code: 0
│       ├── checkpoint.md          # Checkpoint: AUTO_APPROVED_BY_CONTRACT
│       └── goldfish_review_report.json # EGM Goldfish review verdict
├── 02-scaffold/
│   ├── CONTEXT.md
│   └── output/
│       ├── check.md               # Audit: PASS
│       ├── checkpoint.md          # Checkpoint: AUTO_APPROVED_BY_CONTRACT
│       └── stage_manifest.json    # Scaffolded asset registry
├── 03-implement/
│   ├── CONTEXT.md
│   └── output/
│       ├── boids_fish.js          # Craig Reynolds 3D boids (49 lines)
│       ├── caustics_shader.js     # WebGL2 caustics shader (37 lines)
│       ├── check.md               # Audit: PASS
│       ├── checkpoint.md          # Checkpoint: AUTO_APPROVED_BY_CONTRACT
│       ├── main.js                # WebGL2 loop & telemetry (43 lines)
│       ├── sphere_physics.js      # Archimedes buoyancy solver (35 lines)
│       └── wave_pde.js            # 2D damped wave PDE solver (40 lines)
└── 04-verify/
    ├── CONTEXT.md
    ├── contract.sh                # 4-point verification gate
    └── output/
        ├── cdp_telemetry.json     # Headless Chrome CDP verification trace
        ├── check.md               # Audit: PASS
        └── checkpoint.md          # Final pipeline certification
```

### D. Inside-Hermes Mode (The Canonical 18-Line Interactive Progression)

Run this exact sequence in your interactive terminal session:

```bash
# -------------------------------------------------------------
# Stage 01: Socratic Spec Alignment & Goldfish Gate
# -------------------------------------------------------------
/new --yes stage-01-spec
/goal gate add python3 ~/.hermes/tools/icm/egm_goldfish_gate.py stages/01-spec/CONTEXT.md
/goal Draft stages/01-spec/CONTEXT.md and resolve all Goldfish lens findings.
/goal clear

# -------------------------------------------------------------
# Stage 02: Workspace Scaffolding & Contract Verification
# -------------------------------------------------------------
/new --yes stage-02-scaffold
/goal gate add python3 ~/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py stages/02-scaffold
/goal Read stages/02-scaffold/CONTEXT.md and scaffold the project module contracts.
/goal clear

# -------------------------------------------------------------
# Stage 03: Atomic Module Production & Layer 4 Contract Gate
# -------------------------------------------------------------
/new --yes stage-03-implement
/goal gate add bash benchmarks/gauntlet_c_aquarium/contract.sh
/goal Read stages/03-implement/CONTEXT.md and synthesize all atomic modules (<60 lines).
/goal status
/goal clear
```

---

## 6. Complete Command Quick-Reference Table

| Workflow Objective | CLI Profile Command (`hermes -p`) | In-Chat Slash Command (`/cmd`) | Multi-Gateway Mention (`@bot`) |
| :--- | :--- | :--- | :--- |
| **Check Active Profile** | `hermes profile list` | `/profile` | N/A |
| **Set Sticky Profile** | `hermes profile use <name>` | N/A | N/A |
| **Socratic Spec Alignment** | `hermes -p icm-planner chat -q "..."` | `/new --yes spec` + `/goal ...` | `@icm-planner` |
| **Greenfield Scaffolding** | `hermes -p icm-scaffolder chat -q "..."` | `/goal gate add .../hermes_icm_validator.py` | `@icm-scaffolder` |
| **Brownfield AST Migration** | `hermes -p icm-migrator chat -q "..."` | `/goal gate add .../icm_repo_migrator.py` | `@icm-migrator` |
| **Read-Only Invariant Audit**| `hermes -p icm-auditor chat -q "..."` | `/goal gate add .../audit_hermes_home.sh` | `@icm-auditor` |
| **Decompose 60-Line Violations** | `hermes -p icm-migrator chat -q "..."` | `/goal Split files >= 60 lines` | `@icm-migrator` |
| **Spawn Subagent Task** | N/A | `delegate_task(goal="...", context="...")` | N/A |
| **Create Kanban Pipeline** | `hermes kanban create "..." --assignee <p>`| `/kanban create "..." --assignee <p>` | N/A |
| **Automated Multi-Stage Run** | `bash ~/.hermes/tools/icm/run_multi_stage.sh` | 18-line `/new --yes` progression | Dispatcher Loop |

---

## 7. Verified Tool and Configuration Paths

All tools and profile configurations reside in standard user directories:

* **Profile Definitions**:
  * [icm-planner profile.yaml](file:///var/home/imshubhamsocial/.hermes/profiles/icm-planner/profile.yaml) | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-planner/SOUL.md)
  * [icm-scaffolder profile.yaml](file:///var/home/imshubhamsocial/.hermes/profiles/icm-scaffolder/profile.yaml) | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-scaffolder/SOUL.md)
  * [icm-migrator profile.yaml](file:///var/home/imshubhamsocial/.hermes/profiles/icm-migrator/profile.yaml) | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-migrator/SOUL.md)
  * [icm-auditor profile.yaml](file:///var/home/imshubhamsocial/.hermes/profiles/icm-auditor/profile.yaml) | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-auditor/SOUL.md)
* **Deterministic ICM Tools**:
  * [audit_hermes_home.sh](file:///var/home/imshubhamsocial/.hermes/tools/icm/audit_hermes_home.sh)
  * [check_vram_limit.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/check_vram_limit.py)
  * [egm_goldfish_gate.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/egm_goldfish_gate.py)
  * [hermes_icm_validator.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/hermes_icm_validator.py)
  * [hermes_stage_runner.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/hermes_stage_runner.py)
  * [icm_context_auditor.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/icm_context_auditor.py)
  * [icm_repo_migrator.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/icm_repo_migrator.py)
  * [icm_scaffolder.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/icm_scaffolder.py)
  * [run_multi_stage.sh](file:///var/home/imshubhamsocial/.hermes/tools/icm/run_multi_stage.sh)
* **Workspace Skill Tools**:
  * [icm-stage-compiler SKILL.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/SKILL.md)
  * [verify_stage.py](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py)
