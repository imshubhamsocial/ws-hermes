# Document 04: Hermes Workspace ICM Architecture Plan

> **Standard**: ASD-STE100 (Simplified Technical English)  
> **Release Package**: GDR36  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44  
> **Workspace Root**: `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes`  
> **Upstream Directory**: `/var/home/imshubhamsocial/.hermes`  

---

## 1. Core Architectural Determination: Upstream Substrate Purity

This section answers the primary architectural question:
Do we reorganize the `.hermes/` directory into an ICM structure?
Or do we keep the `.hermes/` directory in its original upstream form?

### 1.1 The Decision

We must keep the `.hermes/` directory 100 percent in its original upstream form.
We must NOT reorganize the internal files of `~/.hermes/`.
We must organize the entire external workspace (`ws-hermes`) as an Interpretable Context Methodology (ICM) filesystem state machine.
We must connect the workspace to Hermes Agent by using official upstream commands and official configuration options.

### 1.2 Technical Reasons for this Decision

1. **Substrate Purity**:
   `~/.hermes/hermes-agent` is an upstream git submodule.
   If we change files in `.hermes/`, future git pulls will fail.
   Upstream updates will cause merge conflicts.
   The software must remain pure.

2. **Official Extension Mechanisms**:
   Upstream Hermes Agent provides native configuration fields for external resources:
   - `skills.external_dirs`: This setting in `config.yaml` tells Hermes to read skills from external directories.
   - `hermes skills install <url>`: This official CLI command installs community skills safely.
   - Current Working Directory `AGENTS.md`: Hermes Agent reads `AGENTS.md` from the current directory automatically when you start a session.

3. **Separation of Engine and Factory**:
   `~/.hermes/` is the agent engine.
   `ws-hermes` is the project workspace and product factory.
   ICM Rule 5 states: Configure the factory, not the product.
   Do not mix engine configuration with project workspace contracts.

---

## 2. Upstream Configuration Specifications

To link the pristine upstream Hermes engine to our ICM workspace, edit `~/.hermes/config.yaml`.
Use the official configuration schema shown below:

```yaml
# ~/.hermes/config.yaml - Canonical Upstream Hermes Configuration
_config_version: 45
model:
  provider: local-llama
  default: gemma-4-E4B-it-qat
  base_url: http://127.0.0.1:8138/v1
  context_length: 131072

providers:
  local-llama:
    api: http://127.0.0.1:8138/v1

skills:
  auto_install: false
  external_dirs:
    - /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/skills
    - /var/home/imshubhamsocial/.agents/skills

terminal:
  shell: /bin/bash
  interactive: true
```

### 2.1 Upstream Command Workflow

Run all interactive sessions with the modern Hermes TUI command:

```bash
# Launch interactive session inside the project workspace
cd /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes
hermes --tui
```

Install community skills with the upstream command:

```bash
# Install upstream skill into ~/.hermes/skills
hermes skills install https://github.com/RinDig/icm-architect
```

---

## 3. Complete Workspace Directory Map

The entire `ws-hermes` workspace must follow this five-layer directory structure:

```
/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/
├── AGENTS.md                   # Layer 0: Primary compiler entry point (<60 lines)
├── IDENTITY.md                 # Layer 0: System identity, ports, and agent rules
├── CONTEXT.md                  # Layer 1: Workspace task router (<80 lines)
├── Makefile                    # Deterministic build, eval, and test automation
├── _config/                    # Layer 3: Persistent system-wide invariants
│   ├── invariants.md           # 60% system-wide invariants (hardware, ports, formats)
│   ├── conventions.md          # 15 ICM conventions from _core/CONVENTIONS.md
│   ├── glossary.md             # Standard technical vocabulary (ASD-STE100)
│   └── hardware_limits.md      # VRAM ceiling (5,800.0 MiB), display rules
├── _templates/                 # Layer 3: Reusable templates for stages and checks
│   ├── stage-CONTEXT.md        # Canonical stage contract template
│   ├── contract.sh             # Template deterministic test script
│   └── check.md                # Template verification output file
├── _tools/                     # Layer 3: Deterministic verification scripts
│   ├── hermes_icm_validator.py # Static linter for links and tables
│   └── check_vram_limit.py     # NVML memory verification tool
├── shared/                     # Layer 3: Cross-stage technical references
│   ├── netcode_protocol.md     # Protocol specification for Gauntlet A
│   ├── shader_conventions.md   # Three.js ShaderMaterial rules for Gauntlet C
│   └── vision_schemas.md       # Centroid detection schemas for Gauntlet B
├── skills/                     # Layer 3: Bundled domain knowledge skills
│   ├── icm-architect/          # Workspace design and migration skill
│   ├── icm-stage-compiler/     # Single-pass stage compilation execution skill
│   └── ast-grep-auditor/       # AST pattern search and verification skill
├── stages/                     # Layer 2: Core development pipeline stages
│   ├── 01-probe/               # Stage 1: Environment and runtime probing
│   │   ├── CONTEXT.md          # Stage contract (Inputs, Process, Outputs, Check)
│   │   ├── references/         # Stage-specific reference guides
│   │   └── output/             # Working artifacts (probe_state.json)
│   ├── 02-controller/          # Stage 2: Logic and math calculation
│   │   ├── CONTEXT.md
│   │   ├── references/
│   │   └── output/             # Working artifacts (aim_controller.py)
│   └── 03-execute/             # Stage 3: Execution and telemetry collection
│       ├── CONTEXT.md
│       ├── references/
│       └── output/             # Working artifacts (telemetry.json, check.md)
├── benchmarks/                 # Layer 4: Frontier gauntlet benchmarks and testbeds
│   ├── gauntlet_a_voxel_fps/   # 3D Voxel FPS Netcode Benchmark
│   │   ├── CONTEXT.md
│   │   ├── contract.sh
│   │   ├── references/
│   │   └── output/
│   ├── gauntlet_b_splatbox/    # 3D Paintball Targeting Benchmark
│   │   ├── CONTEXT.md
│   │   ├── contract.sh
│   │   ├── references/
│   │   └── output/
│   └── gauntlet_c_aquarium/    # 3D WebGL Aquarium GPGPU Benchmark
│       ├── CONTEXT.md
│       ├── contract.sh
│       ├── references/
│       └── output/
├── phases/                     # Layer 4: Historical phase ledger and sealed contracts
│   ├── status_ledger.json      # Canonical ledger of sealed phases (Phases 1 to 57)
│   ├── phase_55_production/
│   ├── phase_56_gauntlets/
│   └── phase_57_128k_realism/
└── logs/                       # Layer 4: Benchmark execution logs and trajectory traces
```

---

## 4. Layer File Specifications and Contracts

### 4.1 Layer 0: Root Entry File (`AGENTS.md`)

Location: `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/AGENTS.md`  
Purpose: Orient the agent in under 60 lines.

```markdown
# Layer 0: Hermes ICM Compiler Operating Protocol

## 1. The Compiler Mindset
You are a single-pass stage compiler operating inside an ICM filesystem state machine.
You do not hold multi-turn conversations.
You read the active stage CONTEXT.md.
You load only the exact sections listed in its Inputs table.
You execute the Process.
You write artifacts to output/.
You run the verification audit.

## 2. Operating Rules
1. One Stage, One Job: Execute only the work assigned to the current stage folder.
2. One Fact, One Home: Reference _config/invariants.md. Do not duplicate rules.
3. Docs Over Outputs: Read Layer 3 reference guides to learn code patterns.
4. Atomic Script Size: Write modular Python scripts under 60 lines.
5. CLI & Library First: Use Playwright connect_over_cdp for browser automation.
6. Subagent Restraint: Compile stages directly in the primary context window.
7. Mandatory ASD-STE100 Format: Write all user output in Simplified Technical English.
8. Mandatory Hermes TUI: Run benchmarks and interactive sessions using hermes --tui.
```

### 4.2 Layer 1: Workspace Router (`CONTEXT.md`)

Location: `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/CONTEXT.md`  
Purpose: Route the incoming task to the correct stage folder in under 80 lines.

```markdown
# Layer 1: Workspace Task Routing Map

## Task Routing Table
| User Task Description | Target Directory | Active Contract |
| :--- | :--- | :--- |
| Run or audit Splatbox 3D Paintball | `benchmarks/gauntlet_b_splatbox/` | `contract.sh` |
| Run or audit 3D Voxel FPS Netcode | `benchmarks/gauntlet_a_voxel_fps/` | `contract.sh` |
| Run or audit 3D WebGL Aquarium | `benchmarks/gauntlet_c_aquarium/` | `contract.sh` |
| Execute Gauntlet B Stage 1 (Probe) | `stages/01-probe/` | `CONTEXT.md` |
| Execute Gauntlet B Stage 2 (Aim) | `stages/02-controller/` | `CONTEXT.md` |
| Execute Gauntlet B Stage 3 (Action) | `stages/03-execute/` | `CONTEXT.md` |
| Inspect sealed phase receipts | `phases/` | `status_ledger.json` |
| Verify system invariants | `_config/` | `invariants.md` |
```

### 4.3 Layer 2: Stage Contract (`stages/01-probe/CONTEXT.md`)

Location: `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/stages/01-probe/CONTEXT.md`  
Purpose: Define the exact contract for Stage 1.

```markdown
# 01-probe - Browser and Canvas State Discovery

One job: Probe the browser canvas and write target metadata to output/probe_state.json.

## Inputs
| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| System Invariants | `../../_config/invariants.md` | Browser & CDP Ports | Port 9222 connection |
| Vision Schemas | `../../shared/vision_schemas.md` | Canvas Extraction | Coordinate normalization |

Do NOT load: `../02-controller/`, `../03-execute/`, or `benchmarks/`.

## Process
1. Connect to Chrome CDP on Port 9222 using Playwright.
2. Locate the Splatbox HTML5 canvas element (`#gameCanvas`).
3. Capture a 1280x720 screenshot of the canvas.
4. Extract canvas CSS bounding box dimensions.
5. Save metadata to `output/probe_state.json`.

## Outputs
| Artifact | Location | Format |
| :--- | :--- | :--- |
| Probe State | `output/probe_state.json` | JSON schema with canvas rect |

## Check
Run `python -m json.tool output/probe_state.json`. Must contain width and height keys.
```

---

## 5. Step-by-Step Procedural Migration Guide

Follow these procedural steps to migrate and maintain the workspace:

### Step 1: Verify Substrate Purity
Run git status inside the upstream submodule:
```bash
cd /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/hermes-agent
git status
```
Confirm that zero modified files exist.

### Step 2: Configure External Skills Directory
Open `/var/home/imshubhamsocial/.hermes/config.yaml`.
Add the `skills.external_dirs` entry pointing to `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/skills`.
Save the file.

### Step 3: Scaffold Workspace Directories
Create the standard ICM directories:
```bash
cd /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes
mkdir -p _config _templates _tools shared skills stages phases logs
```

### Step 4: Populate Invariants and System Rules
Copy or link system invariants into `_config/invariants.md`.
Include hardware limits: NVIDIA RTX 3050 VRAM ceiling at 5,800.0 MiB.
Include active network ports: 8138 (Inference), 8642 (Gateway), 1933 (Memory), 9222 (CDP).

### Step 5: Install Upstream ICM Architect Skill
Clone or install the skill into the local skills folder:
```bash
cd /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/skills
git clone https://github.com/RinDig/icm-architect.git
```

### Step 6: Validate Workspace with Static Linter
Execute the static audit tool to confirm link resolution:
```bash
python _tools/hermes_icm_validator.py
```
Confirm that all relative links resolve cleanly.
Confirm that all stage contract tables follow the canonical three-section schema.
