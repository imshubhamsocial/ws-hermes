# Document 02: ICM Pedagogy, Auditing Tools, Isolated Bots & Gauntlet C Specification

> **Document Number**: GDR39-DOC-02  
> **Release Package**: GDR39  
> **Date**: November 15, 2026  
> **Substrate Target**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Engine**: Google Gemma 4 Exact 4B + NVIDIA Nemotron Dory 1.0 Looped 4B  
> **Focus**: 5 Golden Directives — ICM Self-Learning Curriculum, Context Rot Mitigation, Isolated Profile Bots, Gauntlet C Simulation Factory, and Pre-Coding Socratic Alignment  

---

## 1. Golden Directive 1: ICM Pedagogy, Official Tooling & Context Rot Mitigation ("TEACH ME")

### 1.1. The User Learning Framework: Mastering ICM Independently
Interpretable Context Methodology (ICM) replaces chaotic, monolithic prompt chains with a **deterministic, glass-box state machine**. To master ICM, the user must understand software development not as writing code, but as **designing sequential, auditable execution contracts**.

```text
5-Layer ICM Architecture Map
├── Layer 0: System Invariants & Substrate Rules   (AGENTS.md)
├── Layer 1: Task Routing & Stage Decomposition    (CONTEXT.md)
├── Layer 2: Stage Contracts & Local Pipelines      (stages/01-probe/, 02-controller/, 03-execute/)
├── Layer 3: Shared Schemas, Math & Hardware Bounds (_config/, shared/, skills/)
└── Layer 4: Deterministic Audit Gates             (contract.sh, check.md)
```

#### The Four-Phase ICM Execution Protocol for Any Repository:
1. **Phase 1: Invariant & Hardware Scaffolding (Layers 0 & 3)**:
   - Identify hardware limits: VRAM ceiling ($\le 5,800.0\text{ MiB}$), CPU thread allocation, and timeout ceilings.
   - Write `_config/invariants.md`. Never repeat these invariants in subfolders.
2. **Phase 2: Sequential Stage Decomposition (Layers 1 & 2)**:
   - Break any complex problem into sequential stages:
     - *Stage 1 (Probe)*: Test connectivity, daemon health, and raw interface inputs without writing business logic.
     - *Stage 2 (Controller)*: Implement data transformations, mathematical models, calibrations, or unit algorithms.
     - *Stage 3 (Execute)*: Run the end-to-end workload, generate visual or telemetry outputs, and certify against requirements.
3. **Phase 3: Bounded Stage Contracts (Layer 2 `CONTEXT.md`)**:
   - Each stage folder must contain a `CONTEXT.md` strictly declaring:
     - `Inputs`: Exact file paths required.
     - `Process`: Step-by-step POSIX/Python execution instructions.
     - `Outputs`: Generated artifacts (`output/status.json`, `output/data.csv`).
     - `Check`: Deterministic command to verify completion.
4. **Phase 4: Independent Verification Gate (Layer 4 `contract.sh`)**:
   - Write a standalone shell script that inspects physical file existence, JSON schemas, telemetry thresholds, and hardware memory without LLM intervention.
   - Enforce **Zero Fake Green**: If assertions fail, exit with code 1.

#### How to Handle Standard Scenarios:
* **Starting a Fresh Project**: Scaffold Layers 0 to 4 using starter templates. Keep initial stages empty until Probe contract passes.
* **Diagnosing a Corrupted/Stalled Setup**: Audit stage outputs against contracts. If Stage 2 fails, wipe `stages/02-controller/output/` and re-run Stage 2 in isolation without touching Stage 1.
* **Migrating a Raw Third-Party Repo**: Ingest the codebase, identify existing entrypoints and tests, extract shared constants to `_config/`, and partition the codebase into sequential stages with deterministic contracts.

---

### 1.2. Catalog of Official ICM Tooling & References
Lead Architect Argon must consult and catalog the canonical ICM ecosystem:
1. **Jake Van Clief's Core ICM Repository (`Interpretable-Context-Methodology`)**:
   - Raw Base: `https://raw.githubusercontent.com/RinDig/Interpretable-Context-Methodology/main/`
   - Primary reference for the 5-layer folder hierarchy, context pruning algorithms, and bounded attention mechanics.
2. **ICM Starter Template Repository (`icm-template`)**:
   - Raw Base: `https://raw.githubusercontent.com/ktncodes/icm-template/main/`
   - Canonical directory skeleton providing pre-configured `AGENTS.md`, `CONTEXT.md`, and stage runner scripts.
3. **ICM Architect Skill (`icm-architect`)**:
   - Raw Base: `https://raw.githubusercontent.com/RinDig/icm-architect/main/`
   - Specialized agent skill for automatically analyzing project scopes and drafting compliant stage contracts.
4. **Content Agent Routing Promptbase (`Content-Agent-Routing-Promptbase`)**:
   - Raw Base: `https://raw.githubusercontent.com/RinDig/Content-Agent-Routing-Promptbase/main/`
   - Collection of routing prompts for dispatching multi-stage tasks cleanly across subagents.
5. **Clief Notes Foundations Tutor (`Clief-Notes-Foundations-Tutor`)**:
   - Raw Base: `https://raw.githubusercontent.com/donroy26/Clief-Notes-Foundations-Tutor/main/`
   - Pedagogical guide explaining the cognitive science of bounded context windows and attention degradation.

---

### 1.3. Context Rot Mitigation (NVIDIA SkillEvaluator, Google AQUA, NVIDIA Auto Ontology)
As projects evolve over 2 to 4 weeks, markdown files and folder structures suffer from **context rot**:
* Links point to moved or deleted files.
* Rules and instructions are duplicated across sibling folders, violating the "One Fact, One Home" invariant.
* Stale historical assumptions accumulate, bloating the model's KV cache with obsolete directives.

Lead Architect Argon must evaluate the following three tools to automate context auditing:

#### 1. NVIDIA SkillEvaluator
* **Function**: Automated static analysis and AST validation for agent skills and context trees.
* **Capabilities**:
  - Detects broken file references and non-existent markdown links across workspace hierarchies.
  - Identifies duplicate or contradictory instructions between `AGENTS.md` and stage `CONTEXT.md` files.
  - Measures token density and warns when stage inputs exceed bounded context ceilings ($> 8,000$ tokens).
* **Research Objective**: Detail installation, CLI flags, and integration into a pre-commit POSIX hook or Hermes audit loop.

#### 2. Google AQUA (Automated Quality / Verification Analysis)
* **Function**: Multi-modal consistency and quality verification for autonomous software agents.
* **Capabilities**:
  - Validates semantic alignment between high-level project goals and executed stage outputs.
  - Analyzes code and documentation quality against strict technical criteria (ASD-STE100, AST correctness).
* **Research Objective**: Evaluate whether AQUA can be executed locally or via API to grade ICM contract integrity.

#### 3. NVIDIA Auto Ontology
* **Function**: Knowledge graph and taxonomy extraction for unstructured codebases.
* **Capabilities**:
  - Automatically parses large codebases and maps architectural relationships into structured schemas.
  - Prevents semantic drift by formalizing domain entities, boundaries, and data flows.
* **Research Objective**: Assess how Auto Ontology can accelerate migrating raw, random repositories into 5-layer ICM structures.

---

## 2. Golden Directive 2: Dedicated Hermes Bots (Isolated Profiles) Blueprint

Hermes Agent OS natively supports isolated user profiles via the `--profile <name>` CLI parameter. Each profile maintains its own isolated configuration, memory store, skill set, and active state.

Lead Architect Argon must evaluate whether establishing dedicated Hermes bots for ICM lifecycle tasks is superior to running ad-hoc sessions.

### 2.1. Recommended Bot Trio Architecture

```text
~/.hermes/profiles/
├── icm-scaffolder/   -> Profile for scaffolding new ICM projects & stages
├── icm-migrator/     -> Profile for refactoring raw repos into 5-layer ICM
└── icm-auditor/      -> Profile for running SkillEvaluator, AQUA, & contract gates
```

### 2.2. Bot 1: `hermes-icm-scaffolder`
* **Mission**: Interactively guide the user in designing fresh projects, generating `AGENTS.md`, `CONTEXT.md`, stage directories, and `contract.sh` gates.
* **System Prompt Core**:
  ```text
  You are Hermes ICM Scaffolder. You operate strictly under Interpretable Context Methodology.
  Your sole responsibility is to design and scaffold 5-layer ICM project directories.
  Never write business logic or application code. Produce only compliant directory layouts,
  invariants.md, stage contracts, and deterministic verification gates.
  ```
* **Tools**: POSIX file authoring, directory scaffolding, template cloning.

### 2.3. Bot 2: `hermes-icm-migrator`
* **Mission**: Ingest raw, legacy, or unstructured GitHub repositories and compile them into modular 5-layer ICM architectures.
* **Workflow**:
  1. Clones raw repository into a temporary inspection sandbox.
  2. Runs AST dependency analysis to identify entrypoints, circular imports, and global constants.
  3. Extracts shared state into `_config/invariants.md` and `shared/`.
  4. Partitions monolithic files into sequential stages (`01-probe/`, `02-controller/`, `03-execute/`).
  5. Authors atomic test harnesses (strictly under 60 lines) and independent `contract.sh` audit gates.

### 2.4. Bot 3: `hermes-icm-auditor`
* **Mission**: Continuously monitor and audit existing ICM repositories against context rot, rule duplication, broken links, and contract compliance.
* **Workflow**:
  - Runs NVIDIA SkillEvaluator to check link integrity and duplicate rules.
  - Executes all `contract.sh` gates across benchmark suites.
  - Emits structured audit reports to `output/audit_report.json`.

---

## 3. Golden Directive 3: Comprehensive Gauntlet C (Aquarium Simulation) Tutorial

Gauntlet C requires building a modular, high-fidelity 3D WebGL / Three.js Aquarium Simulation inside `benchmarks/gauntlet_c_aquarium/output/aquarium-sim/`. The simulation must match the visual and physical quality of simulations generated by frontier Claude 3.5 Sonnet and Opus models.

### 3.1. Addressing the User Challenge: Bridging Goal to Intermediate Stages
The user knows the end goal (a realistic 3D aquarium with dynamic water ripples, caustic light projections, buoyant floating spheres, and flocking fish), but does not know the intermediate mathematical and graphical steps.

ICM bridges this gap by decomposing the aquarium into **three discrete stages**:

```text
Gauntlet C Pipeline
├── Stage 01-probe/       -> WebGL2 Canvas, Float Texture Extension & Ping-Pong PDE Probe
├── Stage 02-controller/  -> Differential Caustics, Buoyancy Physics & Boid Flocking Controller
└── Stage 03-execute/     -> Full 60 FPS Simulation, AST Verification & Contract Certification
```

### 3.2. Detailed Stage Blueprint for Gauntlet C

#### Stage 1: Graphical & GPGPU Probe (`stages/01-probe/`)
* **Objective**: Verify that the browser environment supports WebGL2 compute extensions and confirm that two ping-pong framebuffers can simulate wave height propagation.
* **Mathematical Invariant**:
  Wave equation in 2D discrete space:
  $$h(x, y, t + \Delta t) = 2h(x, y, t) - h(x, y, t - \Delta t) + c^2 \frac{\Delta t^2}{\Delta x^2} \left[ h(x+1, y) + h(x-1, y) + h(y+1) + h(y-1) - 4h(x, y) \right]$$
* **Verification Gate**:
  - Confirm WebGL2 context creation.
  - Confirm `EXT_color_buffer_float` or `OES_texture_float_linear` support.
  - Render 10 ping-pong simulation steps and verify non-zero variance in heightfield buffers.
  - Output receipt: `stages/01-probe/output/probe_state.json`.

#### Stage 2: Shader, Physics & Flocking Controller (`stages/02-controller/`)
* **Objective**: Implement the core graphical shaders and physical algorithms as isolated modules:
  1. **Differential Area Caustics Shader (`js/caustics_shader.js`)**:
     - Compute refracted light rays from the wave normal into the floor plane.
     - Use hardware screen-space derivatives (`dFdx`, `dFdy`) to compute the triangle area of refracted rays:
       $$\text{Intensity} = \frac{\text{Area}_{\text{unrefracted}}}{\text{Area}_{\text{refracted}}}$$
     - Produces crisp, dynamic caustic light patterns on the aquarium floor and soft shadows behind objects.
  2. **Buoyancy & Hydrodynamic Drag Physics (`js/sphere_physics.js`)**:
     - Model submerged spherical caps:
       $$V_{\text{submerged}} = \frac{\pi h^2}{3} (3R - h)$$
     - Compute buoyant force: $\vec{F}_b = \rho_{\text{water}} V_{\text{submerged}} \vec{g}$.
     - Apply linear and quadratic hydrodynamic drag: $\vec{F}_d = -\frac{1}{2} \rho C_d A \|\vec{v}\| \vec{v}$.
  3. **3D Boid Flocking System (`js/boids_fish.js`)**:
     - Implement Craig Reynolds flocking algorithm with three steering forces:
       - **Separation**: Steer to avoid crowding local flockmates.
       - **Alignment**: Steer towards the average heading of local flockmates.
       - **Cohesion**: Steer to move toward the average position of local flockmates.
     - Add obstacle avoidance for aquarium glass boundaries and submerged spheres.

#### Stage 3: Simulation Assembly & Contract Certification (`stages/03-execute/`)
* **Objective**: Assemble all modules into `index.html` and `js/main.js`.
* **Execution & Verification**:
  - Run the simulation over headless Chrome CDP.
  - Assert sustained $\ge 50\text{ FPS}$ at $1280 \times 720$ resolution.
  - Validate AST syntax across all shader and JS modules.
  - Run [benchmarks/gauntlet_c_aquarium/contract.sh](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/hermes/devel/benchmarks/gauntlet_c_aquarium/contract.sh) to certify 100% PASS.

---

## 4. Golden Directive 4: Hermes Slash Command Orchestration & Professional Prompting

### 4.1. Analysis of Hermes Native Slash Commands
Hermes Agent OS provides built-in slash commands that automate complex workflows:
* `/goal <instruction>`: Puts Hermes into a persistent, autonomous execution mode. Hermes continues executing and self-auditing until the stated goal is fully satisfied.
* `/loop <interval> <instruction>`: Executes a recurring cron-like loop at specified intervals (e.g. every 5 minutes), ideal for continuous telemetry monitoring.
* `/new` / `/reset`: Instantly resets the active conversation session, clearing context memory while preserving on-disk files.
* `/clear`: Clears the visual terminal buffer.
* `/compact` / `/compress`: Summarizes active context to reduce KV cache footprint.

### 4.2. Orchestrating Multi-Stage ICM with `/new` and Contracts
Jake Van Clief's ICM mandates: **"One task, one clean session."** Context bleed between stages causes smaller models to confuse probe routines with execution routines.

#### The Clean Stage-Handoff Protocol:
1. **Stage 1 Session**:
   - User prompts Hermes to execute Stage 1 (`01-probe`).
   - Hermes verifies CDP, generates `probe_state.json`, and outputs the verification receipt.
2. **Context Reset (`/new`)**:
   - The user (or an automated runner) executes `/new`.
   - The conversational context is wiped 100% clean. The KV cache is reset to zero.
3. **Stage 2 Session**:
   - Hermes loads *only* the inputs declared in `stages/02-controller/CONTEXT.md` (which includes `probe_state.json` from Stage 1 as an input).
   - Hermes calibrates weapons, writes `gun_stats.json`, and halts.
4. **Context Reset & Stage 3 Execution**:
   - `/new` is issued again.
   - Hermes executes Stage 3 in a pristine session, consumes `gun_stats.json`, runs the match, and executes `contract.sh`.

### 4.3. Guide to Professional, Non-Spoon-Fed Prompt Engineering
To achieve elite results from Hermes without hardcoding magic numbers or spoon-feeding code, prompts must follow the **Executive Intent Architecture**:

```text
[Executive Prompt Template]
1. Context & Objective: State the high-level operational goal.
2. Architectural Boundaries: State what NOT to do (invariants, ceilings, wall avoidance).
3. Contract Path: Direct the agent to read the stage CONTEXT.md and invariants.
4. Acceptance Gate: Define the physical receipt required for certification.
```

#### Example Comparison:
* **Bad (Spoon-Fed & Brittle)**:
  "Set mx to 0.75 * dx and my to 0.65 * dy. If gun is rifle subtract 14 from dy. Then click at 480, 540."
* **Good (Professional Executive Directive)**:
  "Execute the Stage 3 autonomous match using output/splatbox_agent.py. Decouple movement from aiming: reposition when occluded, and steady the crosshair before firing. Select weapons dynamically based on target range and compensate elevation for distant rifle targets. Suppress fire whenever an obstacle obscures the reticle. Upon completion, run contract.sh to certify the benchmark."

---

## 5. Golden Directive 5: Socratic Sifting & Pre-Coding Alignment (Google Elephant & Fish Model)

### 5.1. The Google Elephant & Fish Paradigm
Google recently introduced the "Elephant & Fish" model for autonomous problem-solving:
* **The Elephant (Adversarial Socratic Inquirer)**:
  - Interrogates the user's high-level request through iterative probing questions.
  - Uncovers hidden assumptions, missing edge cases, and hardware boundaries.
  - Constructs a provisional execution plan, actively attempts to break/falsify the plan, and refines it with the user *before any code is written*.
* **The Fish (Technical Domain Specialist)**:
  - Explores technical schemas, API capabilities, and mathematical requirements.
  - Supplies precise domain constraints to the Elephant.

### 5.2. Benefits of Pre-Coding Socratic Alignment in ICM
In software engineering, **80% of bugs originate in flawed initial assumptions**, not in syntax errors:
* In Gauntlet B, the infinite wall-shooting bug occurred because the agent assumed any red contour was a target, failing to anticipate that red paint splatters on walls would also be red.
* A Socratic planning gate would have asked upfront: *"What happens when paintballs strike walls? Do they leave marks that match target color filters?"*
* Identifying this during the planning stage eliminates hours of runtime debugging and failed benchmark runs.

### 5.3. Designing the Socratic Planning Gate in Hermes
Lead Architect Argon must specify how to integrate this Socratic gate into Hermes:
1. **Interactive Planning Mode (`/plan` / Socratic Hook)**:
   - When a user submits a complex request or gauntlet, Hermes enters a mandatory Socratic interview state before touching files.
   - Hermes asks 3 to 5 targeted clarifying questions regarding edge cases, hardware constraints, and failure modes.
2. **Adversarial Plan Deconstruction**:
   - Hermes drafts a stage plan and presents "Failure Mode Hypotheses" (e.g. *"This plan could fail if the browser window size changes mid-run"*).
   - Once the user confirms the plan, Hermes locks the specification into `CONTEXT.md` and begins execution.
3. **Dedicated Socratic Planning Bot (`hermes-icm-planner`)**:
   - Blueprint an isolated profile bot that acts as the user's Socratic sparring partner for architectural alignment.

---

## 6. Golden Directive 6: Substrate Harmonization, Self-Learned Skills, and SOUL.md Evolution

### 6.1. Substrate Duality and Full Workspace Absorption
Hermes development currently exhibits a structural duality:
* **The Project Shelf**: Active development, gauntlets, and compiler pipelines reside in `hermes/devel/` inside the git repository.
* **The Upstream Substrate**: Upstream Hermes Agent OS configuration resides in `~/.hermes/` (rules, skills, tools, profiles, state databases), while binary sources live in `~/.hermes/hermes-agent/`.

Lead Architect Argon must deliver an architectural blueprint to **absorb `hermes/devel/` into native upstream `~/.hermes/` directories in strict ICM style** without violating **Rule 9 (Substrate Purity)**:
1. **Immutable Upstream Code**: The core runtime `/var/home/imshubhamsocial/.hermes/hermes-agent` remains 100% pristine and untouched.
2. **Native ICM User Substrate**: User configuration directories (`~/.hermes/rules/`, `~/.hermes/skills/`, `~/.hermes/tools/`) are structured to absorb all development layers directly:
   - `~/.hermes/rules/`: Layer 0 and Layer 3 rules mapped into clean domain namespaces (`icm/`, `hardware/`, `security/`).
   - `~/.hermes/skills/`: Native skill packages, each organized as a self-contained ICM folder containing internal routing and atomic Python scripts.
   - `~/.hermes/tools/`: Layer 3 tools (`_tools/`) mapped to native Hermes tool directories with inspectable markdown registries (`tools.md`).
   - `~/.hermes/benchmarks/`: Gauntlet suites (A, B, C) with deterministic `contract.sh` verification gates.

### 6.2. Native ICM Skill Directory Layout with Python Scripts
Every native skill located in `~/.hermes/skills/<skill-name>/` must follow the 5-layer ICM directory architecture:

```text
~/.hermes/skills/<skill-name>/
├── SKILL.md             # Frontmatter, metadata, trigger conditions, input/output schemas
├── scripts/             # Modular, deterministic execution logic
│   ├── helper_a.py      # Atomic task script (strictly under 60 lines)
│   └── helper_b.py      # Atomic task script (strictly under 60 lines)
├── references/          # Bounded contextual documentation and schemas
│   └── invariants.md    # Domain formulas and reference limits
└── tests/
    └── test_skill.py    # Self-contained audit gate returning exit code 0
```

1. **`SKILL.md` Routing Contract**: Frontmatter declares triggers, inputs, outputs, and sub-script routing. The LLM reads only `SKILL.md` initially (2,000 to 4,000 tokens).
2. **Atomic Execution Scripts**: Helper scripts inside `scripts/` provide deterministic Python or Bash execution logic strictly obeying Rule 6 (under 60 lines).
3. **Deterministic Test Gate**: Every skill contains `tests/test_skill.py` verifying that helper scripts execute with exit code 0.

### 6.3. Direct Substrate Auditing via NVIDIA SkillEvaluator and Google AQUA
Because native skills follow standard upstream paths, external auditing tools can evaluate the live `~/.hermes/` directory directly:
1. **Direct Path Auditing**: NVIDIA SkillEvaluator and Google AQUA point directly at `~/.hermes/skills/` and `~/.hermes/rules/`.
2. **Link and Parity Verification**: Auditing tools parse relative Markdown links, detect orphaned references, and identify duplicate rules across skill folders.
3. **AST Linting of Helper Scripts**: SkillEvaluator analyzes Python scripts in `scripts/` to confirm that line counts remain under 60 and dependencies resolve cleanly.

### 6.4. Autonomous Skill Distillation Under ICM (/learn)
When Hermes learns new skills autonomously (via `/learn`, automated reflection, or execution distillation), it must automatically generate them under the **ICM Autonomous Skill Protocol**:
1. **Target Location**: Writes the distilled skill directly into `~/.hermes/skills/<new-skill>/`.
2. **Single Responsibility**: Every self-learned skill solves exactly one atomic problem inside its own dedicated folder.
3. **Bounded Metadata Frontmatter**: Every `SKILL.md` declares name, description, inputs, and outputs.
4. **Atomic Helper Scripts**: Helper scripts generated in `scripts/` strictly obey Rule 6 (under 60 lines).
5. **Deterministic Validation**: Hermes authors a companion `tests/test_skill.py` and confirms exit code 0 before persisting the skill.
6. **No Rule Duplication**: Self-learned skills reference `_config/invariants.md` rather than duplicating shared constants.

### 6.5. Updating SOUL.md for Epistemic ICM Enforcement
The root cognitive persona in `.hermes/SOUL.md` must be updated to formally govern autonomous learning, tool registry maintenance, and workspace discipline:

```markdown
# Identity & Epistemic Posture (SOUL)

You are Hermes Agent OS, a deterministic local engineering system operating under Interpretable Context Methodology (arXiv:2603.16021).

## Core Directives

* **Glass-Box Precision**: Prefer inspectable plain-text files and verified JSON telemetry receipts over prose claims.
* **Zero Fake Green**: Never hardcode expected test outputs, mock live connections, or loosen test assertions to force an exit code 0. If a physical daemon or DOM element is unreachable, report the exact failure in output/ and halt cleanly.
* **Empirical Grounding**: Verify visual and DOM state through actual screenshots and accessibility snapshots before issuing state-mutating actions.
* **ASD-STE100 Communication Discipline**: Communicate every explanation, status update, and technical report using Simplified Technical English (ASD-STE100). Enforce short sentences, active voice, and zero conversational vagueness.
* **5-Layer ICM Execution**: Execute strictly through the 5-Layer ICM folder hierarchy. Never author bespoke orchestration wrappers.
* **Autonomous ICM Skill Authoring**: When saving, refining, or distilling skills via /learn or reflection, format them strictly under ICM standards: bounded context, explicit input/output contracts, and atomic scripts under 60 lines.
* **Tool Discovery & Plain-Text Registries**: Consult inspectable markdown tool registries (tools.md) before invoking commands. If an expected tool is absent, invoke tool_search before concluding a capability is missing.
* **Epistemic Honesty**: State uncertainty explicitly; never fabricate tool outputs, file states, or benchmark metrics. No hype, no sycophancy, no unverified completion claims.
```

---

## 7. Golden Directive 7: Universal Inter-Agent CONTEXT.md Specification

### 7.1. The Need for a Universal Agent Onboarding Document
When collaborating with different autonomous agents (subagents, swarm workers, Claude 3.5 Sonnet, ChatGPT, Gemini Argon, or Cursor IDE), incoming agents often lack workspace grounding. This causes context hallucinations, broken file paths, and rule violations.

A **Universal Inter-Agent CONTEXT.md** provides instantaneous, complete, and unambiguous situational awareness for any incoming model or process.

### 7.2. Master Blueprint for the Universal CONTEXT.md

```markdown
# Layer 1: Universal Workspace Context & Agent Routing Map

## 1. System Identity and Host Infrastructure
You are operating inside ws-hermes (/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes).
* Host OS: Fedora Kinoite 44 (x86_64, rpm-ostree, Linux kernel 6.x).
* Dedicated Compute GPU: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6).
  - VRAM Ceiling: Strictly at or below 5,800.0 MiB ($\le 5,800.0\text{ MiB}$).
  - Compute Dedication: 100% available (Wayland desktop compositor offloaded to Intel iGPU).
* System Host Memory: 16 GB physical RAM with 15.3 GiB zram + 2,048 MiB swap.
* Local Daemons & Ports:
  - Port 8138: Local Inference (Gemma 4 Exact 4B / NVIDIA Nemotron Dory 1.0 Looped 4B).
  - Port 8139: Local Embeddings (EmbeddingGemma-2 on CPU).
  - Port 1933: Local Knowledge (OpenViking on CPU).
  - Port 9222: Chrome DevTools Protocol (CDP) for browser verification.

## 2. Ten Non-Negotiable Compiler Rules
1. One Stage, One Job: Execute only the contract inside the active directory CONTEXT.md.
2. Bounded Context (2,000 to 8,000 Tokens): Load only the exact files declared in Inputs.
3. One Fact, One Home: Never duplicate rules from _config/invariants.md. Link to them.
4. Docs Over Outputs: Learn patterns from Layer 3 (_config/, shared/), never prior outputs.
5. Read Before Edit: Always call read_file on a target file before editing it.
6. Atomic Scripts: Author modular Python and shell scripts strictly under 60 lines.
7. Browser Verification: Use Playwright (CDP) to verify 0 runtime errors on UI tasks.
8. Fresh Context Auditing: Never grade your own output in the generating context; use contract.sh gates.
9. Substrate Purity: Never modify files inside /var/home/imshubhamsocial/.hermes/hermes-agent.
10. Mandatory ASD-STE100 & Google Docs Safety: Use Simplified Technical English and even fence/dollar parity.

## 3. Directory Layout and Task Routing
* CONTEXT.md: Root task router mapping objectives to project directories.
* AGENTS.md: Root operating protocol and layer definitions.
* hermes/devel/: Self-contained development workspace (compiler pipeline, gauntlets, phases).
  - stages/: Sequential compiler pipeline (01-probe/, 02-controller/, 03-execute/).
  - benchmarks/: Frontier Gauntlets A (3D FPS Netcode), B (Splatbox CV), and C (Aquarium WebGL).
  - phases/: Sealed verification ledger (Phases 1 to 58).
  - docs/research/: Historical GDR research packages (GDR30 to GDR39).
  - _config/: System invariants, hardware ceilings, and domain conventions.
  - _tools/: Deterministic Python/POSIX validators and stage runners.
  - shared/: Cross-stage mathematical, netcode, and vision schemas.
  - skills/: Domain skills (icm-architect, icm-stage-compiler).

## 4. Benchmark Routing Table
| Trigger | Target Benchmark | Verification Gate |
| :--- | :--- | :--- |
| gauntlet-a | benchmarks/gauntlet_a_voxel_fps/ | bash benchmarks/gauntlet_a_voxel_fps/contract.sh |
| gauntlet-b | benchmarks/gauntlet_b_splatbox/ | bash benchmarks/gauntlet_b_splatbox/contract.sh |
| gauntlet-c | benchmarks/gauntlet_c_aquarium/ | bash benchmarks/gauntlet_c_aquarium/contract.sh |

## 5. Inter-Agent Contract Protocol
1. Onboard: Read this CONTEXT.md and the active stage CONTEXT.md.
2. Bounded Inputs: Read ONLY the files listed in that stage's Inputs table.
3. Execute: Implement code and scripts obeying Rule 6 (strictly under 60 lines).
4. Verify: Run bash ./contract.sh and confirm exit code 0.
5. Receipt: Write completion telemetry to output/check.md.
```

---

## 8. Golden Directive 8: Cloudflare Decision Models for High-Speed ICM Routing and Verification

### 8.1. Operational Context: Decision Classification Against Autoregressive Generation
Autoregressive LLM generation generates text token-by-token. For many discrete operating tasks inside ICM, full autoregressive text generation creates unnecessary latency and token consumption:
1. **Routing Operations**: Selecting a single target directory or contract from `CONTEXT.md` based on a user prompt.
2. **Contract Acceptance**: Determining a binary PASS or FAIL decision from log telemetry or test exit codes.
3. **Stage Remediation**: Deciding whether to advance to Stage $N+1$ or execute remediation loops.
4. **Tool and Action Choice**: Selecting among atomic scripts without conversational preamble.

Cloudflare Workers AI decision and classification models provide sub-50ms categorical choices. These models operate with zero GPU VRAM consumption on the local host and minimal latency.

### 8.2. Integration Architecture for the 5-Layer ICM Machine

1. **Deterministic Router Script (`_tools/hermes_decision_router.py`)**:
   - The script accepts the raw user prompt and candidated routing paths from `CONTEXT.md`.
   - It dispatches a fast REST request to the Cloudflare decision endpoint.
   - It returns a structured JSON routing decision: `{"action": "route", "target": "stages/02-controller/"}`.
   - The script is modular and authored strictly under 60 lines.

2. **Contract Gate Decision Linter (`_tools/hermes_decision_gate.py`)**:
   - The gate receives physical telemetry files from `output/` and acceptance invariants from `invariants.md`.
   - It performs deterministic schema checks and invokes the decision model for boundary classification.
   - It emits exit code 0 for certified runs or exit code 1 with structured failure diagnostics.

3. **In-Stage Decision Nodes**:
   - Intermediate stages declare discrete decision states in `rules.md`.
   - The agent invokes the decision tool directly to select optimal execution paths.


