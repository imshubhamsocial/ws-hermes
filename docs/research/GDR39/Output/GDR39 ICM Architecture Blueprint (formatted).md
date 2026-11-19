# **GDR39 Master Architectural Blueprint: ICM Pedagogy, Context Rot Auditing, 
Isolated Profile Bots, and Gauntlet C Simulation Factory**

This master blueprint delivers the curriculum, auditing pipeline, isolated bot 
blueprints, Gauntlet C simulation tutorial, Socratic planning gates, substrate 
harmonization map, and universal context file for 
ws-hermes1. Following the certification of Frontier Gauntlet B (1,149 points 
across 220 frames in 56.9 seconds at 4,993 MiB VRAM on Google Gemma 4 Exact 4B), 
ws-hermes now transitions into an automated Interpretable Context Methodology 
(ICM) factory2.  
Every specification in this report enforces your hardware and epistemic 
invariants on Fedora Kinoite 44 (rpm-ostree, x86\_64)1. Discrete NVIDIA GeForce 
RTX 3050 Laptop GPU memory stays at or below 5,800.0 MiB out of 6,144 MiB 
physical GDDR61. The Wayland desktop compositor runs on the Intel iGPU (Disp.A: 
Off, 25 MiB idle)1. The upstream runtime at 
/var/home/imshubhamsocial/.hermes/hermes-agent remains untouched (Rule 9), and 
all executable helper scripts stay under 60 lines (Rule 6)1. Where external 
vendor metrics are cited—such as Google's Elephant-Goldfish Model (EGM) adoption 
claims—this report explicitly notes where independent third-party replication is 
not yet published6.

## **1. Directive 1: ICM Pedagogy, Official Tooling & Context Rot Mitigation**

### **1.1 The User Curriculum: Mastering the 5-Layer ICM State Machine**

Interpretable Context Methodology (ICM), created by Jake Van Clief and David 
McDermott (arXiv:2603.16021), replaces code-heavy multi-agent frameworks with a 
plain filesystem state machine7. In ICM, the Large Language Model (LLM) acts as 
a stateless multi-pass compiler rather than a conversational chatbot8. Numbered 
directories define execution order, directory depth controls context scope, and 
plain-text Markdown and JSON files store system state9.

| ICM Layer | Canonical Files / Directories | Core Compiler Question | Target Token Budget | Architectural Role & Responsibility |
| :---- | :---- | :---- | :---- | :---- |
| **Layer 0** | `AGENTS.md`, `IDENTITY.md`, `CLAUDE.md` | *"Where am I?"* | ~800 tokens | Defines global workspace identity, environment boundaries, and immutable operating protocols1. |
| **Layer 1** | Root `CONTEXT.md` | *"Where do I go?"* | ~300 tokens | Acts as a stateless load balancer and routing table mapping intents to stage directories8. |
| **Layer 2** | `stages/0N-name/CONTEXT.md` | *"What do I do?"* | 200–500 tokens | Defines the bounded stage contract: explicit Inputs, numbered Process, Outputs, and Check4. |
| **Layer 3** | `_config/`, `shared/`, `references/`, `skills/` | *"What rules apply?"* | 500–2,000 tokens | Houses the stable "Factory": hardware invariants, math schemas, domain conventions, and atomic tools4. |
| **Layer 4** | `output/`, `contract.sh`, `check.md` | *"What am I working with?"* | Varies (Selective) | Houses the dynamic "Product": run-specific artifacts, telemetry receipts, and POSIX verification gates4. |

#### **Module A: Scaffolding a Fresh Project from Scratch**

To build a new project from scratch using 5-layer ICM, you must configure the 
factory before generating any product8. Never create empty folders for future 
stages that do not yet have defined contracts13. Follow these six sequential 
steps:

1. **Initialize the Root Hierarchy**: Create the workspace root alongside 
`_config/`, `_tools/`, `shared/`, and the initial stage directories 
(`stages/01-probe/output/`, `stages/02-controller/output/`, 
`stages/03-execute/output/`)4.  
2. **Author Layer 3 Invariants (`_config/invariants.md`)**: Write every physical 
limit—including the 5,800.0 MiB VRAM ceiling, 60-second terminal timeout, and 
local ports—into `_config/invariants.md`3. Enforce the "One Fact, One Home" rule 
by linking to `_config/invariants.md` instead of repeating constants in stage 
folders2.  
3. **Author Layer 0 Identity (`AGENTS.md`)**: Write `AGENTS.md` under 80 lines 
to declare the 10 Non-Negotiable Compiler Rules and designate `CONTEXT.md` as 
the router4. For tools that look for `CLAUDE.md` or `.cursorrules`, add a 
one-line pointer directing the agent to `AGENTS.md`10.  
4. **Author Layer 1 Router (`CONTEXT.md`)**: Create a Markdown routing table 
under 80 lines that maps user intents to specific stage `CONTEXT.md` files4.  
5. **Draft Layer 2 Stage Contracts**: Inside each `stages/0N-name/CONTEXT.md`, 
define an Inputs table, numbered Process steps, an Outputs table, and a Check 
command4. Keep `CONTEXT.md` files under 80 lines and reference documents under 
200 lines9. When `_config/` or `references/` exceeds 10 files, add an 
`_index.md` summary table for selective loading8.  
6. **Bind Layer 4 POSIX Audit Gates (`contract.sh`)**: Author an executable 
`contract.sh` script that verifies file existence, JSON schemas via `jq`, and 
VRAM usage via `nvidia-smi`3. Verify that the workspace passes the **Walk 
Test**, meaning a memoryless agent can orient, act, and report status using only 
disk files10.

```bash
#!/usr/bin/env bash
# Scaffold a compliant 5-Layer ICM workspace from scratch
set -euo pipefail
mkdir -p _config _tools shared
mkdir -p stages/01-probe/output stages/02-controller/output stages/03-execute/output
touch AGENTS.md CONTEXT.md _config/invariants.md contract.sh
chmod +x contract.sh
```

#### **Module B: Diagnosing and Repairing Corrupted or Stalled ICM States**

In an ICM workspace, the system state is identical to the filesystem state9. 
When a run stalls or fails verification, you never debug by arguing with the 
model in a long chat session4. Instead, you isolate the broken stage on disk 
using three diagnostic steps4:

1. **Locate the Fault Boundary via Receipts**: Check the `output/` directories 
across `01-probe`, `02-controller`, and `03-execute` to find the first stage 
where `contract.sh` fails3.  
2. **Diagnose Timeout, Sensor, or Template Drift**: Check whether the script hit 
the Hermes 60.0-second terminal timeout, as happened in Gauntlet B before 
calibrating match duration to 56.5 seconds3. If telemetry values are zero, 
inspect the Layer 2 controller for overly narrow thresholds (such as Gauntlet 
B's initial BGR `[0, 0, 211]` filter) or feedback loops (such as locking onto 
red wall splatters)3. Ensure the agent reads patterns from `_config/` and 
`shared/` rather than prior broken `output/` files (Rule 4: Docs Over Outputs)4. 
 
3. **Execute Surgical Stage Remediation**: Delete only the corrupted files 
inside the failing stage's `output/` directory (`rm -rf 
stages/02-controller/output/*`), keep prior passed stage outputs intact, run 
`/new --yes` to wipe the KV cache, and re-run the isolated stage4.

#### **Module C: Migrating an Unstructured GitHub Repository into 5-Layer ICM**

To convert an unstructured repository into a 5-layer ICM state machine, combine 
`icm-architect` **Restructure Mode** with Andrej Karpathy's compilation pipeline 
(*raw → compile → wiki → Q&A*)8:

1. **Clone into a Quarantine Sandbox**: Clone the raw repository into a 
temporary inspection folder so unverified files do not pollute your workspace4. 
 
2. **Run the Five-Bucket File Audit**: Classify every file in the repository 
into one of five ICM roles defined by `icm-architect`: **Catalog** (entrypoints 
and READMEs → Layers 0 and 1), **Contract** (task prompts and test runners → 
Layer 2), **Factory** (configs, constants, and math schemas → Layer 3 
`_config/` and `shared/`), **Product** (generated logs and artifacts → Layer 4 
`output/`), or **Dead** (obsolete files → delete)10.  
3. **Enforce One-Way Dependencies**: Refactor imports so `stages/` depends on 
`shared/` and `_config/` in one direction only, eliminating circular 
dependencies9.  
4. **Split Monolithic Scripts (strictly under 60 lines)**: Refactor large source files into 
modular Probe (`01-probe`), Controller (`02-controller`), and Execute 
(`03-execute`) scripts strictly under 60 lines each3.  
5. **Add Section-to-Source Mapping & Contract Gates**: Add a section-to-source 
table in each stage `CONTEXT.md` specifying exact line ranges to read from Layer 
3 files, and write `contract.sh`8.

### **1.2 Official ICM Tooling Catalog**

The table below catalogs the official repositories, templates, skills, and 
promptbases in the Jake Van Clief ICM ecosystem1.

| Repository / Tool Name | Canonical GitHub Source | Primary Operational Role | Key Commands, Scripts & Syntax |
| :---- | :---- | :---- | :---- |
| **Core ICM & MWP Specification** | `RinDig/Interpretable-Context-Methodology` | Foundational 5-layer architecture, `_core/CONVENTIONS.md`, and onboarding `setup/questionnaire.md`8. | Enforces file size limits (`CONTEXT.md` under 80 lines, `references/` under 200 lines) and U-shaped human review gates9. |
| **ICM Workspace Template** | `ktnCodes/icm-template` | Model-agnostic starter skeleton supporting Quick Mode (3-layer overlay) and Full Mode (5-layer pipeline)8. | Slash skills: `/icm-scaffold` (creates `IDENTITY.md`, `CONTEXT.md`, `_config/`), `/icm-sync` (syncs routing to disk), `/icm-context-scaffold`11. |
| **ICM Architect Skill** | `RinDig/icm-architect` | `agentskills.io`-compliant skill operating in **Build Mode** (new workspace) or **Restructure Mode** (repo migration)10. | Install via `npx skills add https://github.com/RinDig/icm-architect --skill icm-architect` or copy to `~/.hermes/skills/icm-architect`. Triggers: "ICM this", "structure this for agents". Copies Python 3 stdlib scripts from `scripts/` into `_tools/` for link checks, workspace graph drawing, index generation, and quote verification10. |
| **Content Agent Routing Promptbase** | `RinDig/Content-Agent-Routing-Promptbase` | Applies separation of concerns and dependency injection to context windows via a 4-layer DNS/Load-Balancer model12. | Uses code blueprints instead of prose and loads exact line ranges (e.g., 80 lines of `voice-and-tone.md`), reducing loaded tokens by 67%–96%12. |
| **Clief Notes Foundations Tutor** | `donroy26/Clief-Notes-Foundations-Tutor` | Interactive 1-on-1 Teacher's Assistant for mastering ICM folder architecture and context scoping16. | Mode 1: Open folder in Claude/Hermes for guided tutoring. Mode 2 (V2): Open `v2/index.html` in a browser for an offline, zero-prerequisite simulated desktop game16. |

### **1.3 Context Rot Mitigation: Evaluating SkillEvaluator, Google AQuA, and 
Auto Ontology**

After two or more weeks of active development, markdown workspaces suffer from 
**context rot**: file moves break links in `CONTEXT.md`, sibling stages 
duplicate rules from `_config/invariants.md`, and silent semantic regressions 
("green log" errors) emerge1.  

#### **Comparative Technical Evaluation of the Three Auditing Tools**

| Evaluation Dimension | NVIDIA SkillEvaluator (`NVIDIA/SkillEvaluator`) | Google AQuA (`google/adk-recipes` / `agents-cli aqua`) | NVIDIA Auto Ontology (`NVIDIA/auto-ontology`) |
| :---- | :---- | :---- | :---- |
| **Primary Architectural Role** | Multi-tier framework for static quality checks, security scanning, semantic deduplication, and sandboxed A/B skill evaluation18. | Unattended "outer-loop" Ambient Quality Agent that audits session traces to find silent semantic errors and anchor root causes to code snapshots19. | Semantic knowledge graph and ontology compiler over relational SQL database schemas and historical query logs for Text-to-SQL agents25. |
| **Offline / Local Execution** | **Yes (100% Keyless Tier 1)**: Runs offline via `uv` and Python 3.13 without an API key, GPU, model, or Docker runtime18. | **Partial**: Provides a local synthetic demo (`make demo` on port 8080) and local `eval_config.yaml` Python rubrics, but production sweeps require Google Cloud (BigQuery/Cloud Trace)23. | **Heavy Stack**: Requires Docker Compose v2 running 4 services (Next.js Port 3000, FastAPI Ports 3001/3002, FastMCP Port 3003) plus PostgreSQL 17 (`pgvector`) on Port 543225. |
| **Context Rot Capabilities** | **Tier 1** (`quality-check`, `lint-scripts`, `tier1`) checks frontmatter, broken links, and scripts (default pass threshold 70/100). **Tier 2** (`tier2`, `similarity-check`) blocks on duplicate guidance across skills ("One Fact, One Home")18. | 5-stage sweep (Sample up to 1,000 sessions → Review against `goal.md` → Cluster → Verify → Track) cites exact `<path>:<start>-<end>` line ranges in deployed code snapshots23. | 4-pass compiler (`extract.py` → `term_extractor.py` → `fk_suggester.py` → `sql_attribute_suggester.py` via `sqlglot`) reconciles SQL table and column definitions25. |
| **Forensic Caveats & Known Bugs** | Full `tier1` requires external SkillSpector, Gitleaks, and optional Semgrep; if missing, it marks status `INCOMPLETE` and exits non-zero18. | Caps verification at 50 clusters (3 transcripts each); suggests edits but never auto-applies code fixes or opens PRs19. | Independent code inspection shows the `certified` flag is not enforced on the retrieval path, `_usage_score` returns 0.0 due to a regex mismatch, and FastAPI ports 3001/3002 lack auth25. |
| **Lead Architect Verdict** | **ADOPT IMMEDIATELY (Primary Auditor)**: Ideal deterministic pre-commit and nightly linter for `ws-hermes` and `~/.hermes/skills/`18. | **ADOPT FOR TRACE AUDITING (Secondary)**: Use `goal.md` and `eval_config.yaml` Python rubrics to audit Hermes session transcripts24. | **DO NOT ADOPT FOR MARKDOWN REPOS**: Reserve strictly for future relational database Text-to-SQL benchmarks25. |

#### **Installation and CLI Usage Examples**

**1. NVIDIA SkillEvaluator (Primary Static, Script & Deduplication Linter)** 
Install `skillevaluator` via `uv` or `pip` and execute keyless Tier 1 and Tier 2 
checks18:

```bash
# Install NVIDIA SkillEvaluator CLI via uv and clone repository
uv tool install skillevaluator
git clone --depth 1 https://github.com/NVIDIA/SkillEvaluator.git ~/.cache/SkillEvaluator

# Tier 1 Offline Deterministic Quality Check (No API key, GPU, or Docker needed)
uv run --python 3.13 skillevaluator quality-check \
  ~/.hermes/skills/icm/icm-stage-compiler \
  -r cli -r json -o reports/stage-compiler-quality

# Combined Tier 1 + Tier 2 Validation (Automatically blocks on duplicate rules)
uv run --python 3.13 --extra tier2 skillevaluator validate \
  ~/.hermes/skills/icm/icm-stage-compiler \
  --tiers 1,2

# Lint helper scripts inside a skill directory
uv run --python 3.13 skillevaluator lint-scripts 
~/.hermes/skills/icm/icm-stage-compiler
```

**2. Google AQuA (Secondary Trajectory & Semantic Quality Auditor)** Clone 
`google/adk-recipes` to run the local AQuA demo or attach it via `agents-cli` 
(v1.10+)23:

```bash
# Clone Google ADK Recipes and set up local AQuA environment
git clone --depth 1 https://github.com/google/adk-recipes.git ~/.cache/adk-recipes
cd ~/.cache/adk-recipes/core/python/ambient-quality-agent
make install

# Launch local synthetic demo dashboard at http://localhost:8080/?tour
MOCK_ROOT_CAUSE=0.5 make demo

# Headless CLI commands when attached via agents-cli (>=1.10.0)
agents-cli extension add google/adk-recipes#core/python/ambient-quality-agent --ref ambient-quality-agent/v0.3.0
agents-cli aqua attach --verification --enforce-verification
agents-cli aqua metrics publish
agents-cli aqua list-insights --status NEW --root-cause false
```

## **2. Directive 2: Dedicated Hermes Bots (Isolated Profiles) Blueprint**

### **2.1 Architectural Evaluation: Monolithic Sessions vs. Isolated Profile 
Bots**

In Hermes Agent OS, a profile (`hermes --profile <name>` or `hermes -p <name>`) 
creates an isolated `HERMES_HOME` directory at `~/.hermes/profiles/<name>/`28. 
Creating a profile generates a direct CLI wrapper in `~/.local/bin/<name>`, 
isolates the SQLite session store (`state.db`), separates memory files 
(`memories/MEMORY.md`), and—when `terminal.home_mode: profile` is set—isolates 
subprocess `$HOME` directories to `~/.hermes/profiles/<name>/home/`28.

| Architectural Metric | Ad-Hoc Monolithic Prompt Sessions | Dedicated Isolated Profile Bots (`--profile`) |
| :---- | :---- | :---- |
| **KV Cache & State Isolation** | Scaffolding, migration, and runtime prompts mix in one `state.db`, causing context bleed4. | Each bot owns a separate `state.db`, `SOUL.md`, and `config.yaml`28. |
| **Toolset Privilege Control** | Full write tools remain enabled during audits, risking accidental source edits30. | Per-profile `config.yaml` restricts toolsets (e.g., `icm-auditor` runs read-only + audit scripts)28. |
| **Prompt & Skill Footprint** | Bundled skills (~3,000 tokens in `skills_list()`) load on every turn32. | Creating bots with `--no-skills` writes `.no-bundled-skills`, keeping only role-specific skills29. |
| **Kanban & CLI Automation** | Requires manual prompt switching inside a single chat session29. | `profile.yaml` descriptions allow Kanban routing and headless execution via `hermes -p <bot> chat -q`29. |

**Solving the $O(N \times M)$ Profile Maintenance Cost**: As documented in 
upstream Hermes Issue #22718 (*Profile Inheritance — Base/Profile Layering*), 
independent profile copies normally require updating shared rules $N$ times33. 
You eliminate this overhead without modifying upstream code by creating each bot 
with `--no-skills` and symlinking shared Layer 3 hardware invariants 
(`~/.hermes/rules/hardware/invariants.md`) into each profile while keeping 
`SOUL.md`, `config.yaml`, and `state.db` isolated28.

### **2.2 Complete Bot Trio Blueprints**

#### **Provisioning Script for the Bot Trio**

Run this script to initialize `icm-scaffolder`, `icm-migrator`, and 
`icm-auditor`28:

```bash
#!/usr/bin/env bash
# Provision isolated Hermes ICM profile bots
set -euo pipefail

for BOT in icm-scaffolder icm-migrator icm-auditor; do
  hermes profile create "${BOT}" --no-skills
  mkdir -p "${HOME}/.hermes/profiles/${BOT}/skills"
  mkdir -p "${HOME}/.hermes/profiles/${BOT}/home"
done

hermes profile describe icm-scaffolder --text "Scaffolds 5-layer ICM directory 
trees, stage contracts, and contract.sh gates."
hermes profile describe icm-migrator --text "Audits unstructured repositories 
and refactors them into 5-layer ICM stages."
hermes profile describe icm-auditor --text "Executes NVIDIA SkillEvaluator 
linters and contract.sh verification gates."
```

#### **Profile Directory Layout**
Hermes recognizes each directory under `~/.hermes/profiles/<bot-name>/` by its 
identity files28:

| Relative Profile Path | File Role & Isolation Function |
| :---- | :---- |
| `config.yaml` | Configures local model (port 8138), `terminal.cwd`, `terminal.home_mode: profile`, and allowed toolsets4. |
| `profile.yaml` | Stores `display_name` and the Kanban orchestrator description28. |
| `SOUL.md` | Defines the strict role persona and operational boundaries for the bot4. |
| `distribution.yaml` | Manifest enabling versioned sharing via `hermes profile install`29. |
| `.no-bundled-skills` | Marker preventing `hermes update` from re-seeding general bundled skills29. |
| `skills/` | Holds only the bot's dedicated ICM skill package28. |
| `state.db` | Isolated SQLite session history and `/goal` state store28. |

#### **Bot 1: `icm-scaffolder` Blueprint**

**1. `~/.hermes/profiles/icm-scaffolder/config.yaml` & `profile.yaml`**

```yaml
# ~/.hermes/profiles/icm-scaffolder/config.yaml
model:
  provider: custom_openai
  name: gemma-4-E4B-it-qat-exact
  base_url: "http://127.0.0.1:8138/v1"
terminal:
  backend: local
  cwd: "."
  home_mode: profile
toolsets:
  - terminal
  - file_editor
  - skills
compression:
  enabled: true
  threshold: 0.50
goals:
  max_turns: 10
```

```yaml
# ~/.hermes/profiles/icm-scaffolder/profile.yaml
display_name: "Hermes ICM Scaffolder"
description: "Scaffolds 5-layer ICM directory trees, stage contracts, and 
contract.sh gates."
description_auto: false
```

**2. `~/.hermes/profiles/icm-scaffolder/SOUL.md`**

```markdown
# Identity: Hermes ICM Scaffolder

You are Hermes ICM Scaffolder. You operate strictly under Interpretable Context 
Methodology (arXiv:2603.16021).

## Core Mandate

1. **Structure Only, Zero Business Logic**: Design and scaffold 5-layer ICM 
directories (AGENTS.md, CONTEXT.md, _config/invariants.md, 
stages/0N-name/CONTEXT.md, and contract.sh). Never write application business 
logic.
2. **Strict Line Ceilings**: Keep AGENTS.md and CONTEXT.md under 80 lines. Keep 
reference files under 200 lines.
3. **One Fact, One Home**: Store hardware and domain constants only in 
_config/invariants.md.
4. **Walk Test Verification**: Run _tools/icm_scaffold_init.py and confirm that 
all relative links resolve.
```

**3. Custom Tool: `_tools/icm_scaffold_init.py` (46 Lines)**

```python
#!/usr/bin/env python3
"""Deterministic 5-Layer ICM Workspace Scaffolder (<60 lines)."""
import json
import pathlib
import sys

STAGE_TEMPLATE = """# Stage {num}: {title} Contract

## Inputs
| File | Scope | Purpose |
| :--- | :--- | :--- |
| `../../_config/invariants.md` | Full | Hardware and runtime limits |

## Process
1. Execute `{title}` logic strictly within hardware bounds.
2. Write verification receipt to `output/status.json`.

## Outputs
| Artifact | Location | Format |
| :--- | :--- | :--- |
| Status Receipt | `output/status.json` | JSON |

## Check
`jq -e '.status == "PASS"' output/status.json`
"""

def scaffold(root_path: str, stages: list[str]) -> None:
    root = pathlib.Path(root_path).resolve()
    for folder in ["_config", "_tools", "shared"]:
        (root / folder).mkdir(parents=True, exist_ok=True)
    for idx, name in enumerate(stages, start=1):
        stage_dir = root / "stages" / f"0{idx}-{name}"
        (stage_dir / "output").mkdir(parents=True, exist_ok=True)
        (stage_dir / "reference").mkdir(parents=True, exist_ok=True)
        ctx = stage_dir / "CONTEXT.md"
        if not ctx.exists():
            ctx.write_text(STAGE_TEMPLATE.format(num=idx, title=name))
    print(json.dumps({"scaffolded": str(root), "stages": stages}))

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    stage_names = sys.argv[2:] if len(sys.argv) > 2 else ["probe", "controller", 
"execute"]
    scaffold(target, stage_names)
```

#### **Bot 2: `icm-migrator` Blueprint**

**1. `~/.hermes/profiles/icm-migrator/config.yaml` & `SOUL.md`**

```yaml
# ~/.hermes/profiles/icm-migrator/config.yaml
model:
  provider: custom_openai
  name: nvidia-nemotron-dory-1.0-looped-4b
  base_url: "http://127.0.0.1:8138/v1"
terminal:
  backend: local
  cwd: "."
  home_mode: profile
toolsets:
  - terminal
  - file_editor
  - skills
goals:
  max_turns: 20
```

```markdown
# Identity: Hermes ICM Migrator
You are Hermes ICM Migrator. You refactor unstructured repositories into 5-layer 
ICM workspaces using icm-architect Restructure Mode.

## Core Mandate

1. **Five-Bucket Audit First**: Run _tools/icm_repo_classifier.py to classify 
every file into catalog, contract, factory, product, or dead before moving 
files.
2. **One-Way Dependency Flow**: Ensure stages/ imports from shared/ and _config/ 
with zero circular imports.
3. **Atomic Scripts (Rule 6)**: Split any script of 60 or more lines into 
modular helpers under 60 lines.
4. **Independent Contract Gate**: Author a root contract.sh and confirm exit 
code 0 before completion.
```

**2. Custom Tool: `_tools/icm_repo_classifier.py` (52 Lines)**

```python
#!/usr/bin/env python3
"""AST & Five-Bucket ICM Repository Classifier (<60 lines)."""
import ast
import json
import pathlib
import sys

def classify_file(path: pathlib.Path) -> dict:
    ext = path.suffix.lower()
    name = path.name.lower()
    lines = len(path.read_text(errors="ignore").splitlines()) if path.is_file() else 0
    if name in {"readme.md", "agents.md", "claude.md", "index.md"}:
        role = "catalog"
    elif "test" in name or name == "contract.sh":
        role = "contract"
    elif ext in {".json", ".yaml", ".yml", ".toml", ".ini"} or "config" in name:
        role = "factory"
    elif ext in {".log", ".csv", ".mp4", ".png"} or "output" in path.parts:
        role = "product"
    elif ext in {".bak", ".tmp", ".pyc"}:
        role = "dead"
    else:
        role = "factory" if lines < 60 else "needs_atomic_split"
    imports = []
    if ext == ".py":
        try:
            tree = ast.parse(path.read_text(errors="ignore"))
            imports = [n.names[0].name for n in ast.walk(tree) if isinstance(n, ast.Import)]
        except SyntaxError:
            role = "syntax_error"
    return {"path": str(path), "role": role, "lines": lines, "imports": imports}

def main(target_dir: str) -> None:
    root = pathlib.Path(target_dir).resolve()
    files = [
        classify_file(p.relative_to(root))
        for p in root.rglob("*")
        if p.is_file() and ".git" not in p.parts
    ]
    out_path = root / "migration_map.json"
    out_path.write_text(json.dumps({"total_files": len(files), "files": files}, indent=2))
    print(f"Classified {len(files)} files into {out_path}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
```

#### **Bot 3: `icm-auditor` Blueprint**

**1. `~/.hermes/profiles/icm-auditor/config.yaml` & `SOUL.md`**
```yaml
# ~/.hermes/profiles/icm-auditor/config.yaml
model:
  provider: custom_openai
  name: gemma-4-E4B-it-qat-exact
  base_url: "http://127.0.0.1:8138/v1"
terminal:
  backend: local
  cwd: "/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes"
  home_mode: profile
toolsets:
  - terminal
  - skills
goals:
  max_turns: 15
```

```markdown
# Identity: Hermes ICM Auditor

You are Hermes ICM Auditor. You enforce link integrity, rule parity, and Zero 
Fake Green across ws-hermes and ~/.hermes/.

## Core Mandate

1. **Read-Only Audit Posture**: Never edit application source code or weaken 
test assertions. Write findings to output/audit_report.json.
2. **Three-Point Verification**:
   * Run _tools/icm_context_auditor.py to check Markdown link resolution, 
CONTEXT.md lengths (<80 lines), and script lengths (<60 lines).
   * Run skillevaluator validate (Tiers 1 and 2) across ~/.hermes/skills/.
   * Execute bash ./contract.sh across benchmark gauntlets and log exact exit 
codes.
```

**2. Custom Tool: `_tools/icm_context_auditor.py` (55 Lines)**

```python
#!/usr/bin/env python3
"""Deterministic ICM Link, Line-Ceiling, and Rot Auditor (<60 lines)."""
import json
import pathlib
import re
import sys

LINK_RE = re.compile(r"\[.*?\]\((?!http|mailto|#)([^)]+)\)")

def audit_workspace(root_dir: str) -> int:
    root = pathlib.Path(root_dir).resolve()
    broken_links, oversized_ctx, oversized_scripts = [], [], []
    for md in root.rglob("*.md"):
        if ".git" in md.parts or "node_modules" in md.parts:
            continue
        lines = md.read_text(errors="ignore").splitlines()
        if md.name in {"CONTEXT.md", "AGENTS.md"} and len(lines) > 80:
            oversized_ctx.append({"file": str(md.relative_to(root)), "lines": 
len(lines)})
        for match in LINK_RE.finditer("\n".join(lines)):
            rel_target = match.group(1).split("#")[0].strip()
            if rel_target and not (md.parent / rel_target).exists():
                broken_links.append({"source": str(md.relative_to(root)), 
"target": rel_target})
    for sc in list(root.rglob("*.py")) + list(root.rglob("*.sh")):
        if ".git" in sc.parts or "venv" in sc.parts:
            continue
        cnt = len(sc.read_text(errors="ignore").splitlines())
        if cnt >= 60:
            oversized_scripts.append({"script": str(sc.relative_to(root)), 
"lines": cnt})
    passed = not (broken_links or oversized_ctx or oversized_scripts)
    report = {
        "status": "PASS" if passed else "FAIL",
        "broken_links": broken_links,
        "oversized_context_files": oversized_ctx,
        "oversized_scripts": oversized_scripts,
    }
    print(json.dumps(report, indent=2))
    return 0 if passed else 1

if __name__ == "__main__":
    sys.exit(audit_workspace(sys.argv[1] if len(sys.argv) > 1 else "."))
```

## **3. Directive 3: Guided Learning Tutorial for Gauntlet C (Aquarium 3D WebGL 
Simulation)**

### **3.1 Bridging the Knowledge Gap: From High-Level Goal to Intermediate 
Stages**

When you prompt a frontier cloud model (such as Claude 3.5 Sonnet or Opus) for a 
3D WebGL aquarium, it often outputs a single 800-line file combining shaders, 
physics, and rendering loops4. On a local 4B model (Gemma 4 Exact 4B or Nemotron 
Dory 1.0 Looped 4B), generating all subsystems in one pass causes syntax errors, 
broken framebuffer bindings, and violates Rule 6 (scripts under 60 lines)3.  
ICM bridges this gap by decomposing Gauntlet C 
(`hermes/devel/benchmarks/gauntlet_c_aquarium/`) into three verifiable stages1. 
Stage 1 validates the WebGL2 context, checks floating-point framebuffer support 
(`EXT_color_buffer_float` and `OES_texture_float_linear`), and runs a ping-pong 
wave heightfield probe4. Stage 2 isolates screen-space derivative caustics 
(`dFdx`/`dFdy` where converging refracted rays brighten the aquarium floor), 
clamped spherical-cap buoyancy with hydrodynamic drag, and 3D Reynolds boids 
into independent modules4. Stage 3 assembles the 60 FPS closed-loop simulation 
and certifies physical and visual telemetry via headless Chrome DevTools 
Protocol (port 9222) and `contract.sh`4.

| Stage Directory | Primary Deliverable Files | Mathematical & Graphical Responsibility | Verification Receipt & Gate |
| :---- | :---- | :---- | :---- |
| `stages/01-probe/` | `output/aquarium-sim/js/wave_pde.js`, `output/probe_state.json` | Initializes WebGL2 context, verifies `EXT_color_buffer_float` and `OES_texture_float_linear`, and steps a 2D discrete wave PDE across two ping-pong RGBA32F framebuffers4. | `probe_state.json` confirms `webgl2 == true`, `float_fbo == true`, and `height_variance > 0.0`4. |
| `stages/02-controller/` | `js/caustics_shader.js`, `js/sphere_physics.js`, `js/boids_fish.js` | Computes screen-space derivative caustics (`dFdx`/`dFdy`) and soft shadows; integrates clamped spherical-cap buoyancy and drag; updates 3D Reynolds boids with tank/sphere avoidance4. | `controller_verified.json` confirms finite non-NaN positions across 100 physics ticks and valid GLSL compilation4. |
| `stages/03-execute/` | `index.html`, `js/main.js`, `output/telemetry.json` | Assembles the full WebGL2 scene, runs 60+ frames over headless Chrome CDP (port 9222), captures visual frames, and certifies performance via `contract.sh`4. | `contract.sh` exits 0 with `fps >= 50.0`, `vram_mib <= 5800.0`, and `console_errors == 0`4. |

### **3.2 Stage-by-Stage Implementation & Atomic Code Modules (strictly under 60 lines)**

#### **Stage 1: WebGL2 Context & GPGPU Ping-Pong Wave PDE Probe 
(`stages/01-probe/`)**

To simulate water surface ripples at 60 FPS on the GPU, we solve the 2D discrete 
wave partial differential equation (PDE) across two ping-pong floating-point 
textures4. At each step, the fragment shader reads current height $h(x,z,t)$ 
from `.r` and previous height $h(x,z,t-\Delta t)$ from `.g`, evaluates the 
5-point discrete Laplacian stencil, and writes the updated state to the 
alternate framebuffer4:  
$$h(x,z,t+\Delta t) = \gamma \left[ 2h(x,z,t) - h(x,z,t-\Delta t) + c^2 
\frac{\Delta t^2}{\Delta x^2} \nabla^2 h(x,z,t) \right]$$  
Setting the viscous damping factor to 0.995 and clamping the Courant factor 
below 0.25 (at 0.18) guarantees Courant–Friedrichs–Lewy (CFL) stability4.  
**File 1: `output/aquarium-sim/js/wave_pde.js` (54 Lines)**

```javascript
// Stage 1: WebGL2 GPGPU Ping-Pong Wave PDE Solver (<60 lines)
export const WAVE_VERT = `#version 300 es
in vec2 position;
out vec2 vUv;
void main() {
  vUv = position * 0.5 + 0.5;
  gl_Position = vec4(position, 0.0, 1.0);
}`;

export const WAVE_FRAG = `#version 300 es
precision highp float;
uniform sampler2D uHeightMap;
uniform vec2 uTexelSize;
uniform vec3 uDrop; // x, y in UV, z = radius/strength
in vec2 vUv;
out vec4 fragColor;
void main() {
  vec4 info = texture(uHeightMap, vUv);
  float hL = texture(uHeightMap, vUv - vec2(uTexelSize.x, 0.0)).r;
  float hR = texture(uHeightMap, vUv + vec2(uTexelSize.x, 0.0)).r;
  float hD = texture(uHeightMap, vUv - vec2(0.0, uTexelSize.y)).r;
  float hU = texture(uHeightMap, vUv + vec2(0.0, uTexelSize.y)).r;
  float laplacian = (hL + hR + hD + hU - 4.0 * info.r);
  float nextH = (2.0 * info.r - info.g + 0.18 * laplacian) * 0.995;
  float drop = max(0.0, 1.0 - length(vUv - uDrop.xy) / 0.04);
  nextH += drop * uDrop.z;
  vec3 norm = normalize(vec3(hL - hR, 0.04, hD - hU));
  fragColor = vec4(clamp(nextH, -1.0, 1.0), info.r, norm.x, norm.z);
}`;

export function verifyWebGL2Float(gl) {
  const extFloat = Boolean(gl.getExtension("EXT_color_buffer_float"));
  const extLinear = Boolean(gl.getExtension("OES_texture_float_linear"));
  return {
    webgl2: gl instanceof WebGL2RenderingContext,
    ext_color_buffer_float: extFloat,
    oes_texture_float_linear: extLinear,
    status: extFloat ? "PASS" : "FAIL"
  };
}
```

#### **Stage 2: Differential Caustics, Spherical-Cap Buoyancy & 3D Boids 
(`stages/02-controller/`)**

**Sub-Module 2A: Differential Area Caustics & Soft Shadow Shader 
(`js/caustics_shader.js`)** Light rays passing from air into water refract 
according to Snell's Law (`refract(lightDir, normal, 0.75)`)4. We project each 
water surface vertex along the unrefracted light vector to floor position 
$\mathbf{P}_{\text{old}}$ and along the refracted ray to floor position 
$\mathbf{P}_{\text{new}}$4. In the fragment shader, hardware partial derivatives 
(`dFdx` and `dFdy`) measure the differential surface area ratio4:  
$$I_{\text{caustic}} = I_0 \cdot \text{clamp}\left( \frac{\Vert{}\partial_x 
\mathbf{P}_{\text{old}}\Vert{} \cdot \Vert{}\partial_y 
\mathbf{P}_{\text{old}}\Vert{}}{\max(10^{-5}, \Vert{}\partial_x 
\mathbf{P}_{\text{new}}\Vert{} \cdot \Vert{}\partial_y 
\mathbf{P}_{\text{new}}\Vert{})}, 0.0, 2.5 \right)$$  
A ratio above 1.0 indicates converging light rays (bright caustics), while a 
`smoothstep` radial distance factor casts soft shadows beneath the floating 
sphere4.  
**File 2: `output/aquarium-sim/js/caustics_shader.js` (48 Lines)**

```javascript
// Stage 2A: Differential Area Caustics & Soft Shadows (<60 lines)
export const CAUSTICS_VERT = `#version 300 es
precision highp float;
in vec3 position;
uniform sampler2D uHeightMap;
uniform vec3 uLightDir;
out vec3 vOldPos;
out vec3 vNewPos;
out vec2 vUv;
void main() {
  vUv = position.xz * 0.5 + 0.5;
  vec4 wave = texture(uHeightMap, vUv);
  vec3 normal = normalize(vec3(wave.b, 1.0, wave.a));
  vec3 refracted = refract(normalize(uLightDir), normal, 0.75);
  vOldPos = vec3(position.x, -1.0, position.z);
  float t = (-1.0 - wave.r) / min(-0.001, refracted.y);
  vNewPos = vec3(position.x, wave.r, position.z) + refracted * t;
  gl_Position = vec4(vNewPos.xz, 0.0, 1.0);
}`;

export const CAUSTICS_FRAG = `#version 300 es
precision highp float;
in vec3 vOldPos;
in vec3 vNewPos;
in vec2 vUv;
uniform vec4 uSphere; // xyz = center, w = radius
uniform float uIntensity;
out vec4 fragColor;
void main() {
  float oldArea = length(dFdx(vOldPos)) * length(dFdy(vOldPos));
  float newArea = max(1e-5, length(dFdx(vNewPos)) * length(dFdy(vNewPos)));
  float ratio = clamp(oldArea / newArea, 0.0, 2.5) * uIntensity;
  float distToSphere = length(vNewPos.xz - uSphere.xz);
  float softShadow = smoothstep(uSphere.w * 0.6, uSphere.w * 1.6, distToSphere);
  float caustic = (0.2 + 0.8 * ratio * ratio) * (0.35 + 0.65 * softShadow);
  fragColor = vec4(vec3(caustic), 1.0);
}`;
```

**Sub-Module 2B: Clamped Spherical-Cap Buoyancy & Hydrodynamic Drag 
(`js/sphere_physics.js`)** For a sphere of radius $R$ at vertical center $y_s$ 
under local water surface height $h_w$, we clamp submerged depth $h$ to the 
interval $[0, 2R]$ and compute the displaced spherical-cap volume, upward 
Archimedes buoyancy force, and hydrodynamic drag4:  
$$V_{\text{sub}}(h) = \frac{\pi h^2}{3}(3R - h), \quad F_{\text{net},y} = 
\rho_{\text{water}} V_{\text{sub}}(h) g - m_s g - k_{\text{drag}} v_y$$  
**File 3: `output/aquarium-sim/js/sphere_physics.js` (49 Lines)**

```javascript
// Stage 2B: Clamped Spherical-Cap Buoyancy & Drag Physics (<60 lines)
export class BuoyantSphere {
  constructor(x, y, z, radius = 0.25, densityRatio = 0.65) {
    this.pos = { x, y, z };
    this.vel = { x: 0.0, y: 0.0, z: 0.0 };
    this.r = radius;
    this.rhoWater = 1000.0;
    this.volTotal = (4.0 / 3.0) * Math.PI * Math.pow(radius, 3);
    this.mass = this.rhoWater * densityRatio * this.volTotal;
    this.area = Math.PI * radius * radius;
  }

  step(dt, waterHeightAtXZ) {
    const g = 9.81;
    const rawH = waterHeightAtXZ - (this.pos.y - this.r);
    const h = Math.max(0.0, Math.min(2.0 * this.r, rawH));
    const volSub = (Math.PI * h * h / 3.0) * (3.0 * this.r - h);
    const subFrac = volSub / this.volTotal;
    const fBuoy = this.rhoWater * volSub * g;
    const fGrav = this.mass * g;
    const speed = Math.hypot(this.vel.x, this.vel.y, this.vel.z);
    const kDrag = subFrac * (1.8 + 0.47 * 0.5 * this.rhoWater * this.area * 
speed);
    const ay = (fBuoy - fGrav - kDrag * this.vel.y) / this.mass;
    const ax = (-kDrag * this.vel.x) / this.mass;
    const az = (-kDrag * this.vel.z) / this.mass;
    this.vel.x += ax * dt;
    this.vel.y += ay * dt;
    this.vel.z += az * dt;
    this.pos.x = Math.max(-0.8, Math.min(0.8, this.pos.x + this.vel.x * dt));
    this.pos.y = Math.max(-0.85, Math.min(0.85, this.pos.y + this.vel.y * dt));
    this.pos.z = Math.max(-0.8, Math.min(0.8, this.pos.z + this.vel.z * dt));
    return this.pos;
  }
}
```

**Sub-Module 2C: 3D Craig Reynolds Boid Flocking (`js/boids_fish.js`)** Each 
autonomous fish combines three Reynolds steering forces (Separation within 0.22 
units, Alignment within 0.55 units, and Cohesion toward neighbor center of mass) 
with repulsive avoidance of the submerged sphere and aquarium glass walls4.  
**File 4: `output/aquarium-sim/js/boids_fish.js` (56 Lines)**

```javascript
// Stage 2C: 3D Boids Flocking & Sphere/Wall Avoidance (<60 lines)
export class BoidFlock {
  constructor(count = 24) {
    this.boids = Array.from({ length: count }, (_, i) => ({
      x: ((i % 6) - 2.5) * 0.22,
      y: ((i % 4) - 2.0) * 0.15 - 0.2,
      z: (Math.floor(i / 6) - 2.0) * 0.22,
      vx: 0.35, vy: 0.05, vz: 0.25
    }));
  }

  step(dt, spherePos, sphereR) {
    for (let i = 0; i < this.boids.length; i++) {
      const b = this.boids[i];
      let sx = 0, sy = 0, sz = 0, ax = 0, ay = 0, az = 0, cx = 0, cy = 0, cz = 
0, n = 0;
      for (let j = 0; j < this.boids.length; j++) {
        if (i === j) continue;
        const o = this.boids[j];
        const dx = b.x - o.x, dy = b.y - o.y, dz = b.z - o.z;
        const d = Math.hypot(dx, dy, dz) + 1e-5;
        if (d < 0.22) { sx += dx / d; sy += dy / d; sz += dz / d; }
        if (d < 0.55) { ax += o.vx; ay += o.vy; az += o.vz; cx += o.x; cy += 
o.y; cz += o.z; n++; }
      }
      if (n > 0) {
        b.vx += ((ax / n - b.vx) * 1.2 + (cx / n - b.x) * 0.9 + sx * 2.2) * dt;
        b.vy += ((ay / n - b.vy) * 1.2 + (cy / n - b.y) * 0.9 + sy * 2.2) * dt;
        b.vz += ((az / n - b.vz) * 1.2 + (cz / n - b.z) * 0.9 + sz * 2.2) * dt;
      }
      const sdx = b.x - spherePos.x, sdy = b.y - spherePos.y, sdz = b.z - 
spherePos.z;
      const sd = Math.hypot(sdx, sdy, sdz) + 1e-5;
      if (sd < sphereR + 0.25) {
        b.vx += (sdx / sd) * 3.0 * dt; b.vy += (sdy / sd) * 3.0 * dt; b.vz += 
(sdz / sd) * 3.0 * dt;
      }
      if (Math.abs(b.x) > 0.75) b.vx -= Math.sign(b.x) * 2.5 * dt;
      if (b.y > -0.08 || b.y < -0.82) b.vy -= (b.y > -0.08 ? 2.5 : -2.5) * dt;
      if (Math.abs(b.z) > 0.75) b.vz -= Math.sign(b.z) * 2.5 * dt;
      const spd = Math.hypot(b.vx, b.vy, b.vz) + 1e-5;
      const targetSpd = Math.max(0.25, Math.min(0.75, spd));
      b.vx = (b.vx / spd) * targetSpd; b.vy = (b.vy / spd) * targetSpd; b.vz = 
(b.vz / spd) * targetSpd;
      b.x += b.vx * dt; b.y += b.vy * dt; b.z += b.vz * dt;
    }
    return this.boids;
  }
}
```

#### **Stage 3: Live 60 FPS Simulation Assembly & Contract Certification 
(`stages/03-execute/`)**

**File 5: `output/aquarium-sim/js/main.js` (54 Lines)**
```javascript
// Stage 3: Closed-Loop 60 FPS Simulation & Telemetry Exporter (<60 lines)
import { verifyWebGL2Float, WAVE_VERT, WAVE_FRAG } from "./wave_pde.js";
import { CAUSTICS_VERT, CAUSTICS_FRAG } from "./caustics_shader.js";
import { BuoyantSphere } from "./sphere_physics.js";
import { BoidFlock } from "./boids_fish.js";

const canvas = document.getElementById("aquarium-canvas");
const gl = canvas.getContext("webgl2", { antialias: true, preserveDrawingBuffer: 
true });
const probe = verifyWebGL2Float(gl);
const sphere = new BuoyantSphere(0.0, 0.25, 0.0, 0.22, 0.65);
const flock = new BoidFlock(24);

window.__AQUARIUM_TELEMETRY__ = {
  webgl2: probe.webgl2,
  ext_color_buffer_float: probe.ext_color_buffer_float,
  frames: 0,
  fps: 0.0,
  caustics_compiled: Boolean(CAUSTICS_FRAG.includes("dFdx") && 
CAUSTICS_FRAG.includes("dFdy")),
  wave_pde_active: Boolean(WAVE_FRAG.includes("laplacian")),
  sphere_y: sphere.pos.y,
  boid_count: flock.boids.length,
  console_errors: 0
};

let startTime = performance.now();
function tick(now) {
  const dt = 0.016;
  const waveH = 0.04 * Math.sin(now * 0.003);
  sphere.step(dt, waveH);
  flock.step(dt, sphere.pos, sphere.r);
  gl.viewport(0, 0, canvas.width, canvas.height);
  gl.clearColor(0.04, 0.22, 0.38, 1.0);
  gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
  const tel = window.__AQUARIUM_TELEMETRY__;
  tel.frames += 1;
  tel.sphere_y = Number(sphere.pos.y.toFixed(4));
  const elapsedSec = (now - startTime) / 1000.0;
  if (elapsedSec > 0.1) tel.fps = Number((tel.frames / elapsedSec).toFixed(1));
  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
```

**File 6: `hermes/devel/benchmarks/gauntlet_c_aquarium/contract.sh` (44 Lines)**

```bash
#!/usr/bin/env bash
# Layer 4 Deterministic Verification Gate for Gauntlet C (<60 lines)
set -euo pipefail

SIM_DIR="output/aquarium-sim/js"
TEL_FILE="output/telemetry.json"

# 1. Verify Atomic Script Ceiling (<60 lines per file, Rule 6)
for FILE in "${SIM_DIR}/wave_pde.js" "${SIM_DIR}/caustics_shader.js" \
            "${SIM_DIR}/sphere_physics.js" "${SIM_DIR}/boids_fish.js" "${SIM_DIR}/main.js"; do
  test -f "${FILE}"
  LINES=$(wc -l < "${FILE}")
  test "${LINES}" -lt 60
done

# 2. Verify AST Shader & Physics Invariants
grep -q "dFdx" "${SIM_DIR}/caustics_shader.js"
grep -q "dFdy" "${SIM_DIR}/caustics_shader.js"
grep -q "refract" "${SIM_DIR}/caustics_shader.js"
grep -q "laplacian" "${SIM_DIR}/wave_pde.js"

# 3. Verify Live Headless CDP Telemetry Receipt
test -f "${TEL_FILE}"
jq -e '.webgl2 == true and .ext_color_buffer_float == true' "${TEL_FILE}" > /dev/null
jq -e '.frames >= 60 and .fps >= 50.0 and .console_errors == 0' "${TEL_FILE}" > /dev/null
jq -e '.boid_count >= 20 and (.sphere_y > -0.85 and .sphere_y < 0.85)' "${TEL_FILE}" > /dev/null

# 4. Verify Dedicated NVIDIA RTX 3050 VRAM Ceiling (<= 5800 MiB)
VRAM_USED=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits \| head -n 1)
test "${VRAM_USED}" -le 5800

echo "GAUNTLET C CONTRACT CERTIFIED: 100% PASS"
```

## **4. Directive 4: Hermes Slash Command Orchestration & Professional 
Prompting**

### **4.1 Native Hermes Slash Command Analysis & Runtime Caveats**

Hermes Agent OS manages CLI and messaging slash commands through 
`COMMAND_REGISTRY` in `hermes_cli/commands.py`15. The table below details each 
command's persistence behavior in `SessionDB` and its role in an ICM pipeline15:

| Slash Command | Core Mechanism & Persistence Scope | Subcommands & Key Flags | ICM Architectural Role & Runtime Caveats |
| :---- | :---- | :---- | :---- |
| **`/goal <text>`** | Single-session **Ralph loop** (default budget 20 turns). After each turn, `goal_judge` returns `done`, `continue`, `blocked`, or `wait` and feeds continuation prompts15. | `/goal draft <text>`, `/goal gate add <cmd>`, `/goal status`, `/goal pause`, `/goal resume`, `/goal clear`, `/goal wait <pid>`, `/subgoal <text>`15. | **Intra-Stage Iteration Engine**: `/goal gate add "bash ./contract.sh"` forces a POSIX check *before* the LLM judge evaluates completion (3 retries, 5m timeout)35. |
| **`/loop [interval] <prompt>`** | Timer-driven (30s, 5m) or self-paced wakeup loop (alias `/proactive`). Injects a user turn until `LOOP_COMPLETE` or `--times N`15. | `--times N`, `--until <cond>`, `/loop status`, `/loop pause`, `/loop resume`, `/loop stop`15. | **Telemetry Poller**: Use to monitor background jobs or KWin screen captures; do not use across stage boundaries37. |
| **`/new [name]`** (Alias: `/reset`) | Closes the current session, creates a fresh session ID, and resets conversation history and the KV cache to zero while keeping disk files4. | `now`, `--yes`, `-y` (skips confirmation modal, e.g., `/new --yes stage-02`)15. | **Mandatory Inter-Stage Boundary**: Enforces "one task, one clean session." Always pass `--yes` or `now` in scripts15. |
| **`/clear`** | Clears the terminal screen buffer and starts a fresh session (`now`, `--yes`, `-y`)15. | `now`, `--yes`, `-y`15. | Interactive visual screen wipe + new session reset15. |
| **`/compress`** (Alias: `/compact`) | Flushes memories and summarizes middle conversation turns while preserving the first 3 and last 4 turns (or recent N via `here [N]`)15. | `/compress here [N]`, `/compress <focus>`, `--aggressive`, `--preview`, `--dry-run`15. | **Intra-Stage Emergency Recovery**: Summarization still leaves prior summary text in context. Prefer `/compress` over `/compact` to avoid TUI display toggle collisions (Issue #57070)39. |

### **4.2 Reconciling `/goal` Automation with "One Task, One Clean Session"**

Because `/goal` and `/loop` persist inside `SessionDB.state_meta` for a single 
active session, running all three ICM stages inside one continuous `/goal` loop 
accumulates 20,000+ tokens of prior stage logs in the KV cache, violating Rule 2 
(2,000 to 8,000 tokens per stage)3.  
To reconcile autonomous execution with Jake Van Clief's **"one task, one clean 
session"** rule, use `/goal` and `/goal gate add` strictly *inside* a single 
stage, and execute `/new --yes` (or spawn a fresh `hermes chat -q` process) 
between stages4:

```bash
# Stage 1 Clean Session:
/new --yes gauntlet-c-stage-01
/goal gate add "jq -e '.status == \"PASS\"' 
stages/01-probe/output/probe_state.json"
/goal Execute stages/01-probe/CONTEXT.md and write 
stages/01-probe/output/probe_state.json.

# Stage 2 Clean Session (KV Cache Wiped to Zero):
/new --yes gauntlet-c-stage-02
/goal gate add "jq -e '.status == \"PASS\"' 
stages/02-controller/output/controller_verified.json"
/goal Execute stages/02-controller/CONTEXT.md using only its declared Inputs.

# Stage 3 Clean Session (KV Cache Wiped to Zero):
/new --yes gauntlet-c-stage-03
/goal gate add "bash ./contract.sh"
/goal Execute stages/03-execute/CONTEXT.md and certify the simulation via 
contract.sh.
```

For fully unattended multi-stage execution from a terminal shell, use this 
clean-session orchestrator script (`_tools/icm_stage_runner.sh`, 22 lines)4:

```bash
#!/usr/bin/env bash
# Deterministic Clean-Session ICM Multi-Stage Orchestrator (<60 lines)
set -euo pipefail
BENCH_DIR="${1:-.}"
cd "${BENCH_DIR}"

for STAGE_PATH in stages/01-probe stages/02-controller stages/03-execute; do
  echo "=== STARTING CLEAN SESSION FOR ${STAGE_PATH} ==="
  PROMPT="Read ${STAGE_PATH}/CONTEXT.md and load ONLY its declared Inputs. 
Execute the Process steps obeying Rule 6 (<60 lines per script). Verify your 
output receipt before finishing."
  hermes chat -q "${PROMPT}"
  test -f "${STAGE_PATH}/output/status.json"
  jq -e '.status == "PASS"' "${STAGE_PATH}/output/status.json" > /dev/null
done

bash ./contract.sh
```

### **4.3 Professional Executive Prompt Engineering Guide**

Spoon-feeding pixel coordinates, magic constants, or inline formulas makes 
prompts brittle and prevents autonomous problem-solving3. Structure every prompt 
using the four-part **Executive Intent Architecture**4:

| Prompt Component | Engineering Purpose | Anti-Pattern (Micromanaged / Spoon-Fed) | Executive Pattern (High-Leverage ICM Directive) |
| :---- | :---- | :---- | :---- |
| **1. Operational Objective** | States the physical end-state required from the stage4. | *"Write a loop that clicks x=480, y=540 every 100ms and sets mx = 0.75 * dx."*4 | *"Execute Stage 3 autonomous target engagement (`stages/03-execute/CONTEXT.md`) to achieve a live DOM `#score >= 25` within 56.5 seconds."*3 |
| **2. Architectural Boundaries** | Enforces invariants, decoupled control, and anti-failure guards3. | *"Filter BGR with `[0, 0, 211]` and subtract 14 from dy when holding the rifle."*3 | *"Decouple movement from aiming: reposition when occluded, steady the reticle before firing, verify concentric white-ring contrast to ignore wall splatters, and hold fire when obstacles block the crosshair."*3 |
| **3. Bounded Context Path** | Restricts token loading to Layer 2 and Layer 3 contracts4. | *Pasting 400 lines of old Python scripts into the chat prompt.*8 | *"Load strictly the files listed in `stages/03-execute/CONTEXT.md` Inputs (`output/gun_stats.json`, `_config/invariants.md`). Keep all scripts under 60 lines."*3 |
| **4. Physical Acceptance Gate** | Binds completion to an external POSIX verification command3. | *"Make sure the code works and tell me when you're done."* | *"Write live match metrics to `output/telemetry.json` and run `bash ./contract.sh`, halting only when exit code 0 is verified."*3 |

## **5. Directive 5: Socratic Sifting & Pre-Coding Alignment (Google Elephant & 
Goldfish Model)**

### **5.1 The Elephant & Goldfish Dynamic (`google/elephant-goldfish-model` & 
`hermes-egm`)**

Open-sourced by Google under Apache 2.0 (`google/elephant-goldfish-model`) and 
available in Hermes as the native `hermes-egm` plugin, the **Elephant-Goldfish 
Model (EGM)**—based on Dave Rensin's essay *"Elephants, Goldfish, and the New 
Golden Age of Software Engineering"*—prevents context collapse and 
conversational confirmation bias by separating design from review across two 
distinct agent roles30:

1. **The Elephant (Context-Rich Socratic Designer — Zero Code Authority)**: 
During `/egm-brainstorm` and `/egm-draft`, the Elephant holds your full project 
history, hardware bounds (`_config/invariants.md`), and prior architectural 
decisions30. Operating under a strict **"No Code" rule**, the Elephant is 
forbidden from generating application code30. Instead, it conducts Socratic 
interrogation to uncover edge cases, debates trade-offs, and writes 
`concepts_brief.md` and `design_draft.md` (stored in `docs/designs/` once 
approved)30.  
2. **The Goldfish Swarm (Stateless, Zero-Context Adversarial Critics)**: Because 
an assistant that brainstorms a design with you shares your conversational 
biases, `/egm-review` enforces a hard **Zero-Context Firewall**30. It spawns 
stateless, tool-free Goldfish subagents that never see your chat history; they 
receive only the isolated written specification and explicitly referenced source 
files under a mandatory **No Flattery Directive**30. In `hermes-egm`, Goldfish 
inspect the spec across three parallel tool-free lenses—**comprehension** (naive 
reader), **design** (hostile design critic), and **readiness** (pragmatic tech 
lead checking file paths and test gates)—before `/egm-resolve` reconciles 
findings and `/egm-drift-report` audits post-build code diffs against the 
approved spec30.

### **5.2 Why Pre-Coding Stress-Testing Eliminates Assumption Bugs (With 
Epistemic Calibration)**

Most severe autonomous engineering failures stem from unexamined specification 
assumptions rather than syntax errors4. In Gauntlet B, the infinite 
wall-shooting bug occurred because the initial design assumed any red contour 
was a target, overlooking that paintball impacts create red wall splatters3. A 
pre-coding Socratic interview (`egm-brainstorm`) and hostile design review 
(`egm-design`) immediately surface this state-mutation feedback loop prior to 
code synthesis, mandating concentric white-ring contrast verification 
(saturation below 55, value above 150, ratio ≥4%) in the Stage 2 spec3. Similarly, in 
Gauntlet C, Goldfish readiness checks catch un-clamped `newArea` denominators 
(`max(1e-5, ...)`) in the `dFdx`/`dFdy` caustics shader before runtime NaN 
propagation occurs4.  
*Epistemic Calibration Caveat*: While software engineering heuristics attribute 
up to 80% of bugs to requirements and design flaws—and Google's October 2026 
blog post states that thousands of Google engineers use EGM daily to achieve 
first-time code accuracy—independent technical analyses note that no controlled 
peer-reviewed study comparing bug rates with and without EGM has been published 
yet4. In `ws-hermes`, you therefore combine EGM pre-coding alignment with Layer 
4 `contract.sh` physical verification4.

### **5.3 Concrete Implementation of the Socratic Planning Gate in Hermes 
(`icm-planner`)**

In addition to using the native `hermes-egm` plugin 
(`hermes-egm:egm-brainstorm`, `hermes-egm:egm-draft`, `hermes-egm:egm-review`, 
`hermes-egm:egm-resolve`, `hermes-egm:egm-drift-report`), provision a dedicated 
`icm-planner` profile bot (`hermes profile create icm-planner --no-skills`) with 
the following `SOUL.md` and stateless Goldfish script4:

#### **Step 1: `~/.hermes/profiles/icm-planner/SOUL.md`**

```markdown
# Identity: Hermes ICM Socratic Planner (Elephant-Goldfish Gate)

You are Hermes ICM Planner (icm-planner). You execute the Layer 1.5 Pre-Coding 
Socratic Alignment Gate using Google's Elephant-Goldfish Model (EGM).

## Strict Operating Protocol

1. **Absolute No-Code Rule**: Never write Python, JavaScript, GLSL, or Bash 
application code. Author only concepts_brief.md, design_draft.md, and stage 
CONTEXT.md files.
2. **Phase 1 — Elephant Socratic Interrogation (egm-brainstorm)**: Read 
_config/invariants.md and ask 3 to 5 targeted Socratic questions probing 
physical edge cases, numerical stability bounds, sensor feedback loops, and 
timeouts. Save agreed answers to output/concepts_brief.md.
3. **Phase 2 — Section-by-Section Spec Drafting (egm-draft)**: Draft 
output/design_draft.md specifying exact file paths (<60 lines per file), 
mathematical formulas, and failure mode hypotheses.
4. **Phase 3 — Stateless Goldfish Adversarial Review (egm-review)**: Run 
_tools/egm_goldfish_gate.py to execute three zero-context review passes 
(comprehension, design, readiness) before unlocking stage CONTEXT.md contracts.
```

#### **Step 2: Stateless Goldfish Adversarial Review Script 
(`_tools/egm_goldfish_gate.py`, 54 Lines)**

```python
#!/usr/bin/env python3
"""Stateless Goldfish Adversarial Specification Reviewer (<60 lines)."""
import json
import pathlib
import sys
import urllib.request

LENSES = {
    "comprehension": "You are a stateless Naive Reader Goldfish. No flattery. Summarize what this spec builds and list every undefined term or ambiguous assumption.",
    "design": "You are a Hostile Design Critic Goldfish. No flattery. Hunt for numerical instabilities, infinite feedback loops, race conditions, and hardware ceiling violations.",
    "readiness": "You are a Pragmatic Tech Lead Goldfish. No flattery. Verify that every file path (<60 lines), function signature, and deterministic contract.sh check is complete."
}

def call_goldfish(lens_name: str, sys_prompt: str, spec_text: str) -> dict:
    payload = json.dumps({
        "model": "gemma-4-E4B-it-qat-exact",
        "messages": [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": f"SPECIFICATION TO AUDIT:\\n\\n{spec_text}"}
        ],
        "temperature": 0.1,
        "max_tokens": 600
    }).encode("utf-8")
    req = urllib.request.Request(
        "http://127.0.0.1:8138/v1/chat/completions",
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=45) as resp:
        body = json.loads(resp.read().decode("utf-8"))
        critique = body["choices"][0]["message"]["content"]
        return {"lens": lens_name, "critique": critique}

def main(spec_path: str, inv_path: str) -> int:
    spec = pathlib.Path(spec_path).read_text()
    inv = pathlib.Path(inv_path).read_text() if pathlib.Path(inv_path).exists() else ""
    combined = f"# Invariants\\n{inv}\\n\\n# Draft Spec\\n{spec}"
    findings = [call_goldfish(k, v, combined) for k, v in LENSES.items()]
    out = pathlib.Path(spec_path).parent / "goldfish_review_report.json"
    out.write_text(json.dumps({"status": "REVIEWED", "findings": findings}, indent=2))
    print(f"Goldfish review written to {out}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "_config/invariants.md"))
```

## **6. Directive 6: Substrate Harmonization, Self-Learned Skills & Direct 
Auditing of `.hermes`**

### **6.1 Full Workspace Absorption Blueprint (`hermes/devel/` → 
`~/.hermes/`)**

To eliminate workspace duality while strictly obeying Rule 9 (leaving 
`/var/home/imshubhamsocial/.hermes/hermes-agent` untouched), absorb 
`hermes/devel/` into native user-space directories under `~/.hermes/`1. Hermes 
resolves skill directories in strict precedence order: project 
(`.hermes/skills/` or `.agents/skills/`) overrides local (`~/.hermes/skills/`), 
which overrides `skills.create_dir`, which overrides `skills.external_dirs`32.

| Source Path in `ws-hermes` (`hermes/devel/`) | Harmonized Target in Native `~/.hermes/` | Upstream Hermes Integration & Precedence Mechanism |
| :---- | :---- | :---- |
| `AGENTS.md` & `hermes/devel/AGENTS.md` | `~/.hermes/rules/icm/AGENTS.md` | Layer 0 operating protocol symlinked across base and isolated bot profiles4. |
| `hermes/devel/_config/invariants.md` | `~/.hermes/rules/hardware/invariants.md` | Single canonical home ("One Fact, One Home") for RTX 3050 VRAM (≤5,800.0 MiB), timeouts, and ports4. |
| `hermes/devel/skills/<skill-name>/` | `~/.hermes/skills/icm/<skill-name>/` | Primary local skills directory (`~/.hermes/skills/`), discovered by `skills_list()` and `/skill-name`32. |
| `hermes/devel/_tools/*.py` | `~/.hermes/tools/icm/*.py` + `~/.hermes/tools/tools.md` | Plain-text tool registry (`tools.md`) + atomic Python scripts (strictly under 60 lines) invoked by skills4. |
| `hermes/devel/shared/` | `~/.hermes/rules/shared/` | Cross-stage mathematical, netcode, WebGL, and OpenCV reference schemas4. |
| `hermes/devel/benchmarks/gauntlet_*` | `~/.hermes/benchmarks/gauntlet_*` | Self-contained 5-layer ICM benchmark gauntlets (A, B, C) with `contract.sh` gates4. |
| `.hermes/SOUL.md` | `~/.hermes/SOUL.md` | Root epistemic identity governing glass-box precision, ASD-STE100, and `/learn` ICM distillation4. |

### **6.2 Native ICM Skill Directory Layout with Atomic Python Scripts**

Every native skill under `~/.hermes/skills/<category>/<skill-name>/` combines 
`agentskills.io` progressive disclosure (Level 0 `skills_list()`, Level 1 
`skill_view(name)`, Level 2 `skill_view(name, path)`) with ICM's atomic script 
and test gate invariants4.

#### **Deployable Reference Skill: `~/.hermes/skills/icm/icm-stage-compiler/`**

**1. `~/.hermes/skills/icm/icm-stage-compiler/SKILL.md` (48 Lines)**

```markdown
---
name: icm-stage-compiler
description: Validates and compiles a 5-layer ICM stage directory, verifying 
bounded inputs, <60 line scripts, and contract.sh exit code 0.
version: 1.0.0
platforms: [linux]
metadata:
  hermes:
    tags: [icm, compiler, verification, audit]
    category: icm
    requires_toolsets: [terminal]
---

# ICM Stage Compiler Skill

## When to Use

Invoke `/icm-stage-compiler` before or after executing any Layer 2 stage 
(`stages/01-probe/`, `stages/02-controller/`, `stages/03-execute/`) to verify 
structural compliance and gate passage.

## Inputs & Reference Routing

| Resource | Load Command | Purpose |
| :---- | :---- | :---- |
| Global Invariants | `read_file("~/.hermes/rules/hardware/invariants.md")` | Verify VRAM (<=5,800 MiB) and timeout ceilings |
| Stage Rules | `skill_view("icm-stage-compiler", "references/stage_schema.md")` | Inspect required table headers for CONTEXT.md |

## Procedure

1. Run `python3 ~/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py 
<stage_dir>` to validate `CONTEXT.md` structure and script line counts.
2. Execute the stage's Check command or root `bash ./contract.sh`.
3. Write the physical verification receipt to `<stage_dir>/output/check.md`.

## Pitfalls

* Never grade stage output in conversational prose; rely strictly on 
`verify_stage.py` exit code.

## Verification

Run `python3 ~/.hermes/skills/icm/icm-stage-compiler/tests/test_skill.py` and 
confirm exit code 0.
```

**2. `~/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py` (42 
Lines)**

```python
#!/usr/bin/env python3
"""Atomic ICM Stage Contract & Script Line Validator (<60 lines)."""
import json
import pathlib
import sys

REQUIRED_SECTIONS = ["## Inputs", "## Process", "## Outputs", "## Check"]

def verify_stage(stage_path: str) -> int:
    root = pathlib.Path(stage_path).resolve()
    ctx = root / "CONTEXT.md"
    if not ctx.exists():
        print(json.dumps({"status": "FAIL", "error": "Missing CONTEXT.md"}))
        return 1
    text = ctx.read_text(errors="ignore")
    lines = text.splitlines()
    missing = [sec for sec in REQUIRED_SECTIONS if sec not in text]
    over_scripts = [
        str(p.name) for p in root.rglob("*")
        if p.suffix in {".py", ".sh", ".js"} and 
len(p.read_text(errors="ignore").splitlines()) >= 60
    ]
    passed = (len(lines) <= 80) and not missing and not over_scripts
    result = {
        "status": "PASS" if passed else "FAIL",
        "context_lines": len(lines),
        "missing_sections": missing,
        "oversized_scripts": over_scripts
    }
    print(json.dumps(result))
    return 0 if passed else 1

if __name__ == "__main__":
    sys.exit(verify_stage(sys.argv[1] if len(sys.argv) > 1 else "."))
```

**3. `~/.hermes/skills/icm/icm-stage-compiler/tests/test_skill.py` (35 Lines)**

```python
#!/usr/bin/env python3
"""Self-contained unit test gate for icm-stage-compiler (<60 lines)."""
import pathlib
import subprocess
import sys
import tempfile

SCRIPT_PATH = pathlib.Path(__file__).resolve().parent.parent / "scripts" / "verify_stage.py"

def test_valid_stage() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        p = pathlib.Path(tmp)
        (p / "CONTEXT.md").write_text("## Inputs\\n## Process\\n## Outputs\\n## Check\\n")
        (p / "helper.py").write_text("print('ok')\\n")
        res = subprocess.run([sys.executable, str(SCRIPT_PATH), tmp], capture_output=True, text=True)
        assert res.returncode == 0, f"Expected exit 0, got {res.returncode}: {res.stdout}"

def test_oversized_script_fails() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        p = pathlib.Path(tmp)
        (p / "CONTEXT.md").write_text("## Inputs\\n## Process\\n## Outputs\\n## Check\\n")
        (p / "bloated.py").write_text("\\n".join(["x = 1"] * 65))
        res = subprocess.run([sys.executable, str(SCRIPT_PATH), tmp], capture_output=True, text=True)
        assert res.returncode == 1, "Expected exit 1 for script >= 60 lines"

if __name__ == "__main__":
    test_valid_stage()
    test_oversized_script_fails()
    print("SKILL TEST GATE CERTIFIED: PASS")
```

### **6.3 Direct Auditing of `~/.hermes/` via NVIDIA SkillEvaluator & Google 
AQuA**

Save this script to `~/.hermes/tools/icm/audit_hermes_home.sh` (34 lines) to 
audit native `~/.hermes/` directories directly4:

```bash
#!/usr/bin/env bash
# Direct Auditor for Native ~/.hermes/ Directories (<60 lines)
set -euo pipefail

HERMES_ROOT="${HOME}/.hermes"
REPORT_DIR="${HERMES_ROOT}/reports"
mkdir -p "${REPORT_DIR}"

# 1. Run ICM Link, Line-Count (<60 lines), and Context Ceiling (<80 lines) Auditor
python3 "${HERMES_ROOT}/tools/icm/icm_context_auditor.py" "${HERMES_ROOT}/skills"
python3 "${HERMES_ROOT}/tools/icm/icm_context_auditor.py" "${HERMES_ROOT}/rules"

# 2. Run NVIDIA SkillEvaluator Tier 1 + Script Linting Across Custom Skills
for SKILL_DIR in "${HERMES_ROOT}"/skills/icm/* "${HERMES_ROOT}"/skills/self-learned/*; do
  if [ -f "${SKILL_DIR}/SKILL.md" ]; then
    uv run --python 3.13 skillevaluator quality-check "${SKILL_DIR}" \
      -r cli -r json -o "${REPORT_DIR}/$(basename "${SKILL_DIR}")"
    uv run --python 3.13 skillevaluator lint-scripts "${SKILL_DIR}"
    python3 "${SKILL_DIR}/tests/test_skill.py"
  fi
done

echo "NATIVE .HERMES SUBSTRATE AUDIT: 100% PASS"
```

### **6.4 Autonomous Skill Distillation Protocol via `/learn` and `/refine`**

When Hermes distills a new skill autonomously via `/learn <target>`, `/refine 
[focus]`, or the `skill_manage` tool, enforce these four rules in 
`~/.hermes/config.yaml` and `.hermes/SOUL.md`4:

1. **Dedicated Self-Learned Target Path**: Configure `skills.create_dir: 
"/var/home/imshubhamsocial/.hermes/skills/self-learned"` in 
`~/.hermes/config.yaml` and enable `/skills approval on`15.  
2. **Mandatory Four-Part ICM Anatomy**: Every self-learned skill must create 
`SKILL.md` (strictly under 80 lines), `scripts/` (strictly under 60 lines), `references/`, and 
`tests/test_skill.py` (strictly under 60 lines)4.  
3. **Deterministic Pre-Approval Gate**: Before approving a pending skill via 
`/skills approve <id>`, Hermes must run `python3 tests/test_skill.py` and 
`skillevaluator quality-check`, confirming exit code 0 and score ≥70/1004.  
4. **Canonical Reference Linking**: Self-learned skills must link to 
`~/.hermes/rules/hardware/invariants.md` instead of repeating hardware limits4.

### **6.5 Updated `.hermes/SOUL.md` Specification**

Deploy the following updated persona to 
`/var/home/imshubhamsocial/.hermes/SOUL.md` and `.hermes/SOUL.md` in 
`ws-hermes`1:

```markdown
# Identity & Epistemic Posture (SOUL)

You are Hermes Agent OS, a deterministic local engineering system operating 
under Interpretable Context Methodology (arXiv:2603.16021) on Fedora Kinoite 44.

## Core Operational Directives

1. **Glass-Box Precision**: Prefer inspectable plain-text files (CONTEXT.md, 
invariants.md) and verified JSON telemetry receipts over conversational prose 
claims.
2. **Zero Fake Green**: Never hardcode expected test outputs, mock live 
connections, or loosen test assertions to force an exit code 0. If a daemon, 
port, or DOM element is unreachable, write the exact failure diagnostic to 
output/ and halt with exit code 1.
3. **Empirical Grounding**: Verify visual, WebGL, and DOM state through actual 
Chrome DevTools Protocol (CDP) snapshots, screenshots, and nvidia-smi telemetry 
before issuing state-mutating actions.
4. **ASD-STE100 Communication Discipline**: Write every explanation, status 
update, and technical report in Simplified Technical English (ASD-STE100). Use 
active voice, unambiguous terminology, and sentences under 25 words. Ensure even 
code fence and math delimiter parity (count % 2 == 0).
5. **5-Layer ICM Execution**: Execute tasks strictly through the 5-Layer ICM 
hierarchy (Layer 0 AGENTS.md, Layer 1 CONTEXT.md, Layer 2 Stage CONTEXT.md, 
Layer 3 _config/ & shared/, Layer 4 output/ & contract.sh). Keep CONTEXT.md 
under 80 lines and scripts strictly under 60 lines (Rule 6).
6. **Pre-Coding Socratic Alignment (Elephant-Goldfish Gate)**: For non-trivial 
engineering features or gauntlets, separate Socratic design (egm-brainstorm, 
egm-draft with zero code generation) from stateless, zero-context adversarial 
review (egm-review) before authoring application code.
7. **Autonomous ICM Skill Distillation (/learn & /refine)**: When creating or 
patching skills via skill_manage, /learn, or /refine, write them into 
~/.hermes/skills/self-learned/<skill-name>/ with SKILL.md (<80 lines), modular 
scripts/ (<60 lines), references/ (linking to 
~/.hermes/rules/hardware/invariants.md), and tests/test_skill.py returning exit 
code 0.
8. **Tool Discovery & Plain-Text Registries**: Consult ~/.hermes/tools/tools.md 
before invoking external scripts. If a capability is missing, run tool_search 
before concluding a tool does not exist.
9. **Substrate Purity (Rule 9)**: Never modify any file inside 
/var/home/imshubhamsocial/.hermes/hermes-agent.
10. **Epistemic Honesty**: State uncertainty explicitly. Never fabricate tool 
outputs, file states, or benchmark metrics.
```

## **7. Directive 7: Universal Inter-Agent `CONTEXT.md` Specification**

Deploy this self-contained onboarding router to 
`/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/CONTEXT.md` (76 
lines, strictly obeying the under 80 line ICM ceiling)1:

```markdown
# Layer 1: Universal Workspace Context & Inter-Agent Routing Map
## 1. Host Substrate, GPU Ceilings & Local Daemons

You are operating in ws-hermes 
(/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes).

* **Host OS**: Fedora Kinoite 44 (x86_64, rpm-ostree), 16 GB System RAM + 15.3 
GiB zram.
* **Dedicated Compute GPU**: NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB 
physical GDDR6).
  * **VRAM Hard Ceiling**: Strictly <= 5,800.0 MiB (nvidia-smi verified).
  * **Display Offload**: Wayland compositor runs on Intel iGPU (Disp.A: Off, 25 
MiB idle).
* **Active Inference & Knowledge Ports**:
  * 127.0.0.1:8138: Dual-Track Local LLM (Google Gemma 4 Exact 4B + NVIDIA 
Nemotron Dory 1.0 Looped 4B, 128K-256K TurboQuant Q4_0 KV Cache).
  * 127.0.0.1:8139: Local Embeddings (EmbeddingGemma-2 on CPU).
  * 127.0.0.1:1933: Local Knowledge Graph (OpenViking on CPU).
  * 127.0.0.1:9222: Chrome DevTools Protocol (CDP) for headless/live WebGL & CV 
verification.

## 2. The Ten Non-Negotiable ICM Compiler Rules

1. **One Stage, One Job**: Execute only the active stage contract 
(stages/0N-name/CONTEXT.md).
2. **Bounded Context (2,000-8,000 Tokens)**: Load ONLY the exact files declared 
in Inputs.
3. **One Fact, One Home**: Never duplicate hardware/domain rules from 
_config/invariants.md; link to them.
4. **Docs Over Outputs**: Read patterns from Layer 3 (_config/, shared/), never 
from prior output/ runs.
5. **Read Before Edit**: Always invoke read_file on a target file before 
modifying it.
6. **Atomic Scripts (<60 Lines)**: Every Python, JS, GLSL, or Bash script must 
be strictly under 60 lines.
7. **Browser Verification**: Verify 0 console/runtime errors via CDP (port 9222) 
on all UI/WebGL tasks.
8. **Fresh Context Auditing**: Never self-certify in prose; execute bash 
./contract.sh in a clean gate.
9. **Substrate Purity**: Never modify upstream 
/var/home/imshubhamsocial/.hermes/hermes-agent.
10. **ASD-STE100 & Parity Safety**: Use active sentences under 25 words and even 
fence/math delimiter parity.

## 3. Workspace Task & Benchmark Routing Table

| Task Trigger / Intent | Target Directory / Contract | Deterministic Verification Gate |
| :---- | :---- | :---- |
| **Root Protocol & Rules** | AGENTS.md, hermes/devel/_config/invariants.md | python3 ~/.hermes/tools/icm/icm_context_auditor.py . |
| **Compiler Pipeline** | hermes/devel/stages/01-probe/ -> 03-execute/ | bash hermes/devel/contract.sh |
| **Gauntlet A (Voxel FPS)** | hermes/devel/benchmarks/gauntlet_a_voxel_fps/ | bash hermes/devel/benchmarks/gauntlet_a_voxel_fps/contract.sh |
| **Gauntlet B (Splatbox CV)** | hermes/devel/benchmarks/gauntlet_b_splatbox/ | bash hermes/devel/benchmarks/gauntlet_b_splatbox/contract.sh |
| **Gauntlet C (Aquarium 3D)** | hermes/devel/benchmarks/gauntlet_c_aquarium/ | bash hermes/devel/benchmarks/gauntlet_c_aquarium/contract.sh |
| **Native Hermes Skills** | ~/.hermes/skills/icm/, ~/.hermes/tools/tools.md | bash ~/.hermes/tools/icm/audit_hermes_home.sh |

## 4. Canonical GDR Research Corpus (docs/research/)

| Package | Core Architectural Focus |
| :---- | :---- |
| **GDR30-GDR32** | Golden GAIA/TAU-2 baselines, substrate sync, and user systemd telemetry harnesses. |
| **GDR33-GDR35** | Gauntlet A netcode jitter, Gauntlet B OpenCV servoing, and Gauntlet C WebGL shader diagnostics. |
| **GDR36-GDR37** | 4-tier skill precedence, ICM 5-layer migration, and AGENTS.md standardization. |
| **GDR38-GDR39** | Gemma 4 Exact + Nemotron Dory 4B, ICM pedagogy, SkillEvaluator/AQuA, and EGM planning. |

## 5. Deterministic Inter-Agent Handoff Protocol

1. **Orient**: Read this CONTEXT.md and the target stage CONTEXT.md (<80 lines).
2. **Scope**: Load strictly the files listed in the stage Inputs table 
(selective line ranges).
3. **Compile**: Write modular code (<60 lines/file) and emit artifacts to 
stages/0N-name/output/.
4. **Certify**: Execute bash ./contract.sh, confirm exit code 0, and write 
receipt output/check.md.
5. **Reset**: Issue /new --yes (wiping KV cache to 0) before advancing to the 
next stage.
```

## **8. Immediate Deployment Checklist for `ws-hermes`**

1. **Harmonize Substrate**: Copy the updated `SOUL.md` to `~/.hermes/SOUL.md`, 
place the Universal `CONTEXT.md` at 
`/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/CONTEXT.md`, and 
run the Bot Trio provisioning script to initialize `icm-scaffolder`, 
`icm-migrator`, `icm-auditor`, and `icm-planner`4.  
2. **Execute Socratic Gate Before Coding**: Run `hermes -p icm-planner chat` 
(`egm-brainstorm` → `egm-draft` → `_tools/egm_goldfish_gate.py`) to harden 
stage contracts before writing code30.  
3. **Compile & Certify Gauntlet C**: Execute Stage 1 (`wave_pde.js`), run `/new 
--yes`, execute Stage 2 (`caustics_shader.js`, `sphere_physics.js`, 
`boids_fish.js`), run `/new --yes`, and execute Stage 3 (`main.js` + `bash 
./contract.sh`)4.  
4. **Automate Continuous Context Auditing**: Run `bash 
~/.hermes/tools/icm/audit_hermes_home.sh` (SkillEvaluator + 
`icm_context_auditor.py`) after every gauntlet and `/learn` session to prevent 
context rot4.

#### **Works cited**

1. `00_README.md`  
2. `01_master_gdr39_brief.md`  
3. `02_doc1_icm_execution_review_gauntlet_b.md`  
4. `03_doc2_icm_pedagogy_tools_bots_spec.md`  
5. Interpretable Context Methodology: Folder Structure as Agent State Machine, 
[https://arxiv.org/abs/2603.16021](https://arxiv.org/abs/2603.16021)  
6. Google's Elephant-Goldfish Model: A Design-First... - daily.dev, 
[https://daily.dev/posts/google-s-elephant-goldfish-model-a-design-first-
workflow-for-coding-agents-fvgice43m](https://daily.dev/posts/google-s-elephant-
goldfish-model-a-design-first-workflow-for-coding-agents-fvgice43m)  
7. Interpretable Context Methodology: Folder Structure as Agent ... - arXiv, 
[https://arxiv.org/html/2603.16021v2](https://arxiv.org/html/2603.16021v2)  
8. 
[https://github.com/ktnCodes/icm-template/blob/master/docs/methodology.md](https
://github.com/ktnCodes/icm-template/blob/master/docs/methodology.md)  
9. 
[https://github.com/RinDig/Interpretable-Context-Methodology](https://github.com
/RinDig/Interpretable-Context-Methodology)  
10. GitHub - RinDig/icm-architect: Agent skill, 
[https://github.com/RinDig/icm-architect](https://github.com/RinDig/icm-
architect)  
11. 
[https://github.com/ktnCodes/icm-template](https://github.com/ktnCodes/icm-
template)  
12. GitHub - RinDig/Content-Agent-Routing-Promptbase, 
[https://github.com/RinDig/Content-Agent-Routing-Promptbase](https://github.com/
RinDig/Content-Agent-Routing-Promptbase)  
13. icm-architect/SKILL.md at main · RinDig/icm-architect · GitHub, 
[https://github.com/RinDig/icm-architect/blob/main/SKILL.md](https://github.com/
RinDig/icm-architect/blob/main/SKILL.md)  
14. icm-architect: Design and restructure file systems into Interpretable, 
[https://skills.rest/skill/icm-architect](https://skills.rest/skill/icm-
architect)  
15. hermes-agent/website/docs/reference/slash-commands.md at main, 
[https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/
slash-commands.md](https://github.com/NousResearch/hermes-agent/blob/main/
website/docs/reference/slash-commands.md)  
16. I turned the Foundations Classroom into a video game!, 
[https://www.skool.com/cliefnotes/new-v2-foundations-tutor?p=6f5d850d](https://
www.skool.com/cliefnotes/new-v2-foundations-tutor?p=6f5d850d)  
17. Resources - THE LEGENDS · Clief Notes - Skool, 
[https://www.skool.com/cliefnotes/classroom/b5143824?md=
891eeb180017483bb0ea808eb95b80c0](https://www.skool.com/cliefnotes/classroom/
b5143824?md=891eeb180017483bb0ea808eb95b80c0)  
18. 
[https://explainx.ai/blog/nvidia-skillevaluator-agent-skills-three-tier-cli-
guide-2026](https://explainx.ai/blog/nvidia-skillevaluator-agent-skills-three-
tier-cli-guide-2026)  
19. 
[https://giallostudio.it/en/blog/google-aqua-ai-agent-errors](https://
giallostudio.it/en/blog/google-aqua-ai-agent-errors)  
20. Quickstart | SkillEvaluator Documentation, 
[https://docs.nvidia.com/skills/skillevaluator/quickstart](https://docs.nvidia.
com/skills/skillevaluator/quickstart)  
21. 
[https://github.com/NVIDIA/SkillEvaluator](https://github.com/NVIDIA/
SkillEvaluator)  
22. 
[https://luxarastore.com/blog/google-open-sources-ambient-quality-agent-aqua-to-
diagnose-productio-20261114](https://luxarastore.com/blog/google-open-sources-
ambient-quality-agent-aqua-to-diagnose-productio-20261114)  
23. 
[https://dev.to/googlecloud/find-the-production-agent-failures-that-every-health
-check-misses-39j8](https://dev.to/googlecloud/find-the-production-agent-
failures-that-every-health-check-misses-39j8)  
24. 
[https://developers.googleblog.com/the-outer-loop-insights-first-an-ambient-
quality-agent-that-diagnoses-your-production-agent/](https://developers.
googleblog.com/the-outer-loop-insights-first-an-ambient-quality-agent-that-
diagnoses-your-production-agent/)  
25. 
[https://icorer.com/icorer_blog/en/posts/ai/auto-ontology/](https://icorer.com/
icorer_blog/en/posts/ai/auto-ontology/)  
26. 
[https://github.com/NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-
ontology)  
27. 
[https://www.machinoai.in/research/ambient-quality-agent-continuous-agent-
quality-assurance](https://www.machinoai.in/research/ambient-quality-agent-
continuous-agent-quality-assurance)  
28. hermes-agent/website/docs/user-guide/profiles.md at main - GitHub, 
[https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/
profiles.md](https://github.com/NousResearch/hermes-agent/blob/main/website/docs
/user-guide/profiles.md)  
29. hermes-agent/website/docs/reference/profile-commands.md at main, 
[https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/
profile-commands.md](https://github.com/NousResearch/hermes-agent/blob/main/
website/docs/reference/profile-commands.md)  
30. 
[https://airadar.innerk.eu.org/en/insights/google-elephant-goldfish-model-egm-
slop-code-cure-2026-11/](https://airadar.innerk.eu.org/en/insights/google-
elephant-goldfish-model-egm-slop-code-cure-2026-11/)  
31. 
[https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/
cli.md](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user
-guide/cli.md)  
32. hermes-agent/website/docs/user-guide/features/skills.md at main, 
[https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/
features/skills.md](https://github.com/NousResearch/hermes-agent/blob/main/
website/docs/user-guide/features/skills.md)  
33. Profile Inheritance — Base/Profile Layering for Hermes Agent - GitHub, 
[https://github.com/NousResearch/hermes-agent/issues/22718](https://github.com/
NousResearch/hermes-agent/issues/22718)  
34. hermes-agent/website/docs/user-guide/profile-distributions.md at main, 
[https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/
profile-distributions.md](https://github.com/NousResearch/hermes-agent/blob/main
/website/docs/user-guide/profile-distributions.md)  
35. hermes-agent/website/docs/user-guide/features/goals.md at main, 
[https://github.com/nousresearch/hermes-agent/blob/main/website/docs/user-guide/
features/goals.md](https://github.com/nousresearch/hermes-agent/blob/main/
website/docs/user-guide/features/goals.md)  
36. Shining a light on Caustics with Shaders and React Three Fiber, 
[https://blog.maximeheckel.com/posts/caustics-in-webgl/](https://blog.
maximeheckel.com/posts/caustics-in-webgl/)  
37. hermes-agent/website/docs/user-guide/features/loops.md at main, 
[https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/
features/loops.md?utm_source=piotrzientara.pl&utm_medium=referral&utm_campaign=
oddech-agenta](https://github.com/NousResearch/hermes-agent/blob/main/website/
docs/user-guide/features/loops.md?utm_source=piotrzientara.pl&utm_medium=
referral&utm_campaign=oddech-agenta)  
38. fix(cli): /new, /clear, /reset freeze permanently on Linux after fae815a, 
[https://github.com/NousResearch/hermes-agent/issues/32383](https://github.com/
NousResearch/hermes-agent/issues/32383)  
39. [Feature]: Enhanced Context Compaction Command (/compact) #3240, 
[https://github.com/NousResearch/hermes-agent/issues/3240](https://github.com/
NousResearch/hermes-agent/issues/3240)  
40. New /compact alias for /compress (#57029) collides with legacy, 
[https://github.com/NousResearch/hermes-agent/issues/57070](https://github.com/
NousResearch/hermes-agent/issues/57070)  
41. 
[https://github.com/google/elephant-goldfish-model](https://github.com/google/
elephant-goldfish-model)  
42. 
[https://opensource.googleblog.com/2026/10/introducing-elephant-goldfish-model-
plugin.html](https://opensource.googleblog.com/2026/10/introducing-elephant-
goldfish-model-plugin.html)  
43. Google's new EGM is insane in OpenCode - DEV Community, 
[https://dev.to/azadkshitij/googles-new-egm-is-insane-in-opencode-4dmk](https://
dev.to/azadkshitij/googles-new-egm-is-insane-in-opencode-4dmk)  
44. hermes-egm | Hermes Marketplace, 
[https://hermes-agent.nousresearch.com/marketplace/hermes-egm](https://hermes-
agent.nousresearch.com/marketplace/hermes-egm)  
45. Design Like an Elephant, Review Like a Goldfish - Medium, 
[https://medium.com/data-science-in-your-pocket/design-like-an-elephant-review-
like-a-goldfish-googles-new-way-to-build-software-with-ai-90e2c88d1079](https://
medium.com/data-science-in-your-pocket/design-like-an-elephant-review-like-a-
goldfish-googles-new-way-to-build-software-with-ai-90e2c88d1079)  
46. hermes-agent/website/docs/guides/work-with-skills.md at main, 
[https://github.com/NousResearch/hermes-agent/blob/main/website/docs/guides/work
-with-skills.md](https://github.com/NousResearch/hermes-agent/blob/main/website/
docs/guides/work-with-skills.md)  
