# Hermes ICM Operations and Self-Learning Manual

**Document Version**: 1.0.0  
**Language Standard**: ASD-STE100 (Simplified Technical English)  
**Target Platform**: Fedora Kinoite 44 (x86_64) | ws-hermes Distrobox  
**Canonical File Location**: [LEARNING.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/research/GDR40/Output/LEARNING.md)

---

## 1. Architectural Foundation: Profiles Over Raw Commands

Raw terminal commands bypass agent reasoning. They fail to generate auditable execution traces.  
Running planning, scaffolding, migration, and auditing in one shared session causes context pollution.

Hermes Agent OS solves this problem with isolated profiles in [~/.hermes/profiles/](file:///var/home/imshubhamsocial/.hermes/profiles/).  
Each profile enforces the Single Responsibility Principle:

| Profile Name | Model Assigned | Temperature | Persona Document | Operational Role |
| :--- | :--- | :--- | :--- | :--- |
| **`icm-planner`** | `nemotron-dory-1.0-looped-4b` | 0.2 | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-planner/SOUL.md) | Socratic spec interviewer and Goldfish review controller. |
| **`icm-scaffolder`** | `gemma-4-exact-4b` | 0.1 | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-scaffolder/SOUL.md) | Greenfield 5-layer workspace generator and contract compiler. |
| **`icm-migrator`** | `nemotron-dory-1.0-looped-4b` | 0.0 | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-migrator/SOUL.md) | Brownfield AST 5-bucket classifier and module refactorer. |
| **`icm-auditor`** | `gemma-4-exact-4b` | 0.0 (Read-Only) | [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-auditor/SOUL.md) | Deterministic token, line-ceiling, and substrate auditor. |

Hermes provides two execution surfaces:
1. **Direct CLI Mode**: Run isolated commands with `hermes -p <profile>`.
2. **Inside-Hermes Mode**: Use slash commands, `@bot` messaging mentions, `delegate_task`, or `/kanban`.

---

## 2. Task 1: Greenfield Setup (Create Fresh ICM Repository)

This workflow transforms a project concept into a verified 5-layer ICM workspace.

### A. Direct CLI Mode (`hermes -p`)

#### Step 1: Conduct Socratic Interview and Compile Specification
Run the `icm-planner` profile to interview you and author `stages/01-spec/CONTEXT.md`:
```bash
hermes -p icm-planner chat -q "Read CONTEXT.md. Interview me for project 'my-new-app' and author stages/01-spec/CONTEXT.md."
```

#### Step 2: Subject the Specification to the Goldfish Gate
Execute the stateless Goldfish comprehension review:
```bash
python3 ~/.hermes/tools/icm/egm_goldfish_gate.py stages/01-spec/CONTEXT.md
```

#### Step 3: Scaffold the 5-Layer Hierarchy
Run the `icm-scaffolder` profile to generate the filesystem layout and stage contracts:
```bash
hermes -p icm-scaffolder chat -q "Read stages/01-spec/output/goldfish_review_report.json. Execute python3 ~/.hermes/tools/icm/icm_scaffolder.py . to scaffold the workspace."
```

#### Step 4: Verify Scaffolding Contracts
Run the deterministic validator:
```bash
python3 ~/.hermes/tools/icm/hermes_icm_validator.py
```

---

### B. Inside-Hermes Mode (In-Chat Slash Commands & Bot Routing)

#### Option 1: Interactive Slash Command Sequence
Execute this sequence inside any active Hermes chat session:
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
/goal gate add python3 ~/.hermes/tools/icm/hermes_icm_validator.py

# 7. Execute scaffolding
/goal Execute python3 ~/.hermes/tools/icm/icm_scaffolder.py . and verify all 5 layers exist.

# 8. Clean up goal state
/goal clear
```

#### Option 2: Messaging Gateway Routing (`@bot` mentions)
In Telegram, Discord, or Slack groups where Hermes gateways operate:
```text
@icm-planner Please interview me on architecture requirements and generate stages/01-spec/CONTEXT.md.
```
Once approved:
```text
@icm-scaffolder The spec report passed. Scaffold the 5-layer ICM structure in this directory.
```

#### Option 3: Multi-Profile Kanban Collaboration (`/kanban`)
Create linked task cards on the durable task board:
```bash
# Create specification task assigned to planner
/kanban create "Stage 01 Architecture Specification" --assignee icm-planner

# Create scaffolding task dependent on Stage 01
/kanban create "Stage 02 Workspace Scaffolding" --assignee icm-scaffolder --parents t_spec01
```

---

## 3. Task 2: Brownfield Migration (Migrate Existing Messy Repository)

This workflow audits an unstructured codebase, classifies all files into 5 buckets, and decomposes monolithic files.

### A. Direct CLI Mode (`hermes -p`)

#### Step 1: Execute AST Classification and Emit Migration Plan
Run the `icm-migrator` profile to analyze the codebase:
```bash
hermes -p icm-migrator chat -q "Execute python3 ~/.hermes/tools/icm/icm_repo_migrator.py . to classify all files and emit migration_map.json."
```

#### Step 2: Inspect and Approve the Classification
View the classification map:
```bash
cat migration_map.json | grep -E "catalog|contract|factory|product|dead"
```

#### Step 3: Execute Decomposition and Relocation
Run the migrator to refactor files and enforce the line ceiling (under 60 lines):
```bash
hermes -p icm-migrator chat -q "Apply migration_map.json. Split monolithic source files exceeding 59 lines into atomic modules under 60 lines."
```

---

### B. Inside-Hermes Mode (In-Chat Slash Commands & Bot Routing)

#### Option 1: Interactive Slash Command Sequence
Execute this sequence inside Hermes chat:
```bash
# 1. Clean session wipe for migration
/new --yes repo-migration

# 2. Attach verify-only AST quality gate
/goal gate add python3 ~/.hermes/tools/icm/icm_repo_migrator.py . --verify-only

# 3. Launch migration goal
/goal Run AST repository classifier, produce migration_map.json, and decompose scripts over 59 lines.

# 4. View status of gate and turns
/goal status

# 5. Clear goal when completed
/goal clear
```

#### Option 2: Messaging Gateway Routing (`@bot` mentions)
In messaging platforms:
```text
@icm-migrator Analyze current repository. Classify files into the 5 ICM buckets and present migration_map.json.
```
After review:
```text
@icm-migrator Approved. Decompose all scripts over 59 lines into atomic modules under 60 lines.
```

#### Option 3: Subagent Delegation via `delegate_task`
If working inside a coordinator chat session, invoke the migrator through delegation:
```python
delegate_task(
    goal="Classify legacy repository into 5 ICM buckets and produce migration_map.json",
    context="Path: /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes"
)
```

---

## 4. Task 3: Audit and Remediation (Fix Existing ICM Repositories)

Use this workflow to detect and fix broken invariants, line-ceiling violations ($\ge 60$ lines), missing headers, or substrate contamination.

### A. Direct CLI Mode (`hermes -p`)

#### Step 1: Run Read-Only Deterministic Audits
Execute the `icm-auditor` profile to scan context budgets, line ceilings, and substrate purity:
```bash
hermes -p icm-auditor chat -q "Execute bash ~/.hermes/tools/icm/audit_hermes_home.sh and python3 ~/.hermes/tools/icm/check_vram_limit.py."
```

#### Step 2: Run Workspace Validation Audit
Validate workspace structure and stage contracts:
```bash
hermes -p icm-auditor chat -q "Execute python3 ~/.hermes/tools/icm/hermes_icm_validator.py."
```

#### Step 3: Trigger Targeted Remediation
Run the `icm-migrator` to decompose flagged files:
```bash
hermes -p icm-migrator chat -q "Decompose all Python and Bash files flagged with line count >= 60 in audit output. Keep all modules under 60 lines."
```

---

### B. Inside-Hermes Mode (In-Chat Slash Commands & Bot Routing)

#### Option 1: Interactive Slash Command Sequence with Dual Quality Gates
Bind multiple deterministic verification scripts as pre-judge gates:
```bash
# 1. Clean session wipe for remediation
/new --yes repo-remediation

# 2. Gate 1: Check substrate purity and line ceilings
/goal gate add bash ~/.hermes/tools/icm/audit_hermes_home.sh

# 3. Gate 2: Check ICM workspace contracts and headers
/goal gate add python3 ~/.hermes/tools/icm/hermes_icm_validator.py

# 4. Gate 3: Check VRAM ceiling (< 5,800.0 MiB)
/goal gate add python3 ~/.hermes/tools/icm/check_vram_limit.py

# 5. Launch remediation goal
/goal Refactor all files violating line limits or missing headers until all quality gates pass.

# 6. Clear goal upon verification
/goal clear
```

#### Option 2: Messaging Gateway Routing (`@bot` mentions)
```text
@icm-auditor Audit current workspace for Rule 6 (60-line ceiling) and Rule 9 (substrate purity) violations.
```
Then send remediation request:
```text
@icm-migrator Decompose the flagged files from icm-auditor's report. Ensure all scripts remain strictly under 60 lines.
```

---

## 5. Task 4: End-to-End Multi-Stage Execution & Bot Handoff

This workflow runs numbered stages sequentially while wiping the KV cache at every stage boundary.

### A. Direct CLI Mode (`run_multi_stage.sh`)

Run the automated headless runner. It executes each stage in a stateless subshell with `--no-session-persistence`:
```bash
bash ~/.hermes/tools/icm/run_multi_stage.sh .
```

To run individual stages manually via CLI:
```bash
# Execute Stage 01
hermes -p icm-planner chat --no-session-persistence -q "Execute stage contract stages/01-spec/CONTEXT.md."

# Execute Stage 02
hermes -p icm-scaffolder chat --no-session-persistence -q "Execute stage contract stages/02-scaffold/CONTEXT.md."

# Execute Stage 03
hermes chat --no-session-persistence -q "Execute stage contract stages/03-implement/CONTEXT.md."

# Audit Stage Outputs
hermes -p icm-auditor chat --no-session-persistence -q "Audit outputs in stages/03-implement/output/."
```

---

### B. Inside-Hermes Mode (The Canonical 18-Line Interactive Progression)

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
/goal gate add bash stages/03-implement/contract.sh
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
