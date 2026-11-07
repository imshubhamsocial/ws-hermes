# Document 2: Jake Van Clief's ICM Deep Research, Commercial Architecture, and Universal Folder Scaffolding

> **Standard**: Jake Van Clief and David McDermott's *Interpretable Context Methodology* (ICM / MWP, arXiv:2603.16021)  
> **Target Reviewer**: Gemini Argon (Google DeepMind Cognitive Architecture Review / Deep Research Web)  
> **Core Focus**: Resolving the 2,000–8,000 Token Working Context Paradox, Analyzing Commercial Tooling, and Defining Universal Repository Scaffolding

---

## 1. The Core Paradox: 2,000–8,000 Working Context vs. 128K Physical Context

In the modern LLM landscape, frontier models advertise context windows of 128,000 to 2,000,000 tokens. However, in *Interpretable Context Methodology* (ICM / MWP, arXiv:2603.16021), Jake Van Clief enforces a strict discipline:

> *"The active working context delivered to an autonomous coding agent must remain strictly bounded between 2,000 and 8,000 tokens at every stage of execution."*

To many practitioners, this appears contradictory: Why run an inference engine like `llama-server` with `-c 131072` (128K context) if the active prompt must never exceed 8,000 tokens?

### 1.1 The Two Competing Hypotheses
* **Hypothesis A (The Virtual Sliding Window)**: ICM enforces an artificial sliding window on the agent's prompt to keep KV-cache compute fast, using the large 128K buffer merely as an in-memory buffer for raw conversation history.
* **Hypothesis B (Externalized Markdown Relational Database)**: Modern transformer models experience severe **attention degradation**, **middle-context fog**, and **instruction decay** when context balloons beyond 16K tokens. Rather than stuffing entire codebases, documentation, and database schemas into a monolithic 100K prompt, Jake treats the filesystem (structured markdown files, directories, and AST search tools) as an **external, human-interpretable relational database**. The 128K physical engine buffer exists to accommodate large tool outputs (compiler dumps, multi-file diffs, database snapshots), while the agent's core prompt remains surgically focused between 2,000 and 8,000 tokens.

---

## 2. Deep Research Mandate: Jake Van Clief's Commercial Ecosystem & Tooling

Gemini Argon is instructed to execute an exhaustive web and literature crawl into Jake Van Clief, his published works, video presentations, and commercial tools:

### 2.1 Key Research Questions for Argon
1. **Commercial Selling Points**:
   * What are the specific enterprise value propositions that Jake Van Clief markets to commercial clients?
   * How does he position ICM against competing agentic frameworks (e.g., AutoGen, CrewAI, LangGraph, Devin, Cursor)?
2. **Real-World Tooling & Monetization**:
   * What software tools, CLI harnesses, or SaaS platforms has Jake developed around these open-source models?
   * How are these tools structured to generate enterprise revenue?
   * Does he license proprietary scaffolding packages, run managed agent fleets, or provide deterministic auditing engines?
3. **Enterprise Production Discipline**:
   * How does Jake prevent the common failure modes of commercial agents (infinite loops, hallucinated dependencies, silent syntax errors, budget explosions)?
   * What role do deterministic shell contracts (`contract.sh`) and AST validators play in his production offerings?

---

## 3. Universal Repository Scaffolding: `invariants.md`, `rules.md`, and `references.md`

In his technical presentations on markdown-driven orchestration, Jake emphasizes that agent systems fail when repository structures are unstructured or ad-hoc. An autonomous agent must never guess where rules, constraints, or schemas reside.

### 3.1 The 3 Essential Scaffolding Documents
Every project, task, and benchmark suite must adhere to a standardized tripartite contract structure:

1. **`invariants.md` (Hard Operational Boundaries — The "Never" Layer)**:
   * Absolute mathematical, architectural, and security constraints that the agent must never violate under any circumstance.
   * *Examples*: Hardware VRAM ceilings ($\le 5,800.0$ MiB), upstream git repository purity (zero dirty submodules), zero custom Python glue scripts in `scripts/`, read-only database constraints.
2. **`rules.md` (Procedural Directives — The "Always" and "Ask First" Layers)**:
   * Execution protocols, coding conventions, AST querying requirements, linting directives (`ruff check`), commit message standards, and permission boundaries.
   * *Examples*: Always verify source code with AST grep before compiling; ask user confirmation before deleting files; always format code with black/ruff.
3. **`references.md` (Domain Schemas & Context Pointers — The "Knowledge" Layer)**:
   * Machine-readable interfaces, API schemas, product catalogs, mock database layouts, and port topologies.
   * *Examples*: OmniRoute customer endpoint specifications, Port 8642 OpenAI-compatible schema definitions, retail product catalogs, AST pattern cheatsheets.

---

## 4. Architectural Blueprint: Universal Folder Hierarchy for Hermes Agent OS

To ensure that every future task, production project, and benchmark run maintains 100% consistency with Jake's 60/30/10 paradigm, Argon must critique and standardize the following universal layout:

```
hermes-workspace/
├── AGENTS.md                                    # Layer 0: Global Workspace Map (< 80 lines)
├── CONTEXT.md                                   # Layer 1: Global Stage Router (< 80 lines)
├── Makefile                                     # Layer 0: Deterministic Infrastructure CLI
│
├── rules/                                       # Layer 1: Global Rules Engine
│   ├── invariants.md                            # Global hard bounds (VRAM <= 5,800M, zero bespoke code)
│   ├── anti_rationalization_tables.md           # Prohibited agent excuses & deceptive behaviors
│   └── anti_sycophancy_directives.md            # Prohibition of blind agreement with flawed prompts
│
├── stages/                                      # Layer 2: 4-Stage Autonomous Pipeline
│   ├── 01-spec/                                 # Stage 1: Requirement Specification
│   │   ├── CONTEXT.md                           # Stage routing & entrypoint (< 80 lines)
│   │   ├── invariants.md                        # Stage-specific hard constraints
│   │   └── rules.md                             # Specification guidelines & rubrics
│   ├── 02-plan/                                 # Stage 2: Architectural & File Planning
│   │   ├── CONTEXT.md                           # Stage routing (< 80 lines)
│   │   ├── invariants.md                        # Plan boundaries (zero net new wrappers)
│   │   └── rules.md                             # Stage contract templates & AST queries
│   ├── 03-execute/                              # Stage 3: Code Mutation & Implementation
│   │   ├── CONTEXT.md                           # Execution entrypoint (< 80 lines)
│   │   ├── invariants.md                        # Mutation boundaries & AST safety gates
│   │   └── rules.md                             # Linter rules, compiler flags, testing steps
│   └── 04-verify/                               # Stage 4: Fresh-Session Verification Gate
│       ├── CONTEXT.md                           # Verification entrypoint (< 80 lines)
│       ├── invariants.md                        # Independent session isolation constraints
│       └── rules.md                             # Test execution & cryptographic receipt rules
│
├── benchmarks/                                  # Layer 2: Canonical Agent Harness Suites
│   ├── tau_bench/                               # Sierra Research Retail/Airline ReAct Gauntlet
│   │   ├── invariants.md                        # Port isolation (Cust 20128, Agent 8642), zero OOM
│   │   ├── rules.md                             # Multi-turn customer authentication & DB commit rules
│   │   └── references.md                        # Mock retail schema, tool names, product IDs
│   ├── gaia/                                    # UK DSIT Inspect AI GAIA Assistant Suite
│   │   ├── invariants.md                        # Local sandbox bounds (/shared_files), max 30 turns
│   │   ├── rules.md                             # Mathematical derivation & submit() invocation rules
│   │   └── references.md                        # Wikipedia orbital data, reference physical constants
│   └── ast_grep_eval/                           # Local CLI AST + GCC Verification Testbed
│       ├── invariants.md                        # Execution sandbox limits, gcc compile flags
│       ├── rules.md                             # AST pattern query syntax & binary execution rules
│       └── references.md                        # Reference C source (fibonacci.c) & pattern signatures
│
└── references/                                  # Layer 3: Machine-Readable Global References
    ├── substrate_ports.md                       # Canonical daemon port registry (8138, 8642, 1933, 20128)
    └── hardware_vram_invariants.md              # Physical NVML GDDR6 telemetry & allocations
```

---

## 5. Synthesis Directive for Argon

Argon must evaluate this scaffolding against Jake Van Clief's published literature and commercial tools:
1. Does this folder hierarchy strictly enforce the 2,000–8,000 token working context constraint at every stage?
2. Does it completely eliminate the risk of the agent becoming trapped in 60-turn circular loops?
3. How can Hermes Agent OS be updated to reflect this universal standard across all current and future projects?
