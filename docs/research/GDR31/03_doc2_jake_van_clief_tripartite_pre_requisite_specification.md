# GDR31 Technical Specification: Jake Van Clief Tripartite Pre-requisite Structure

> **Methodological Standard**: Jake Van Clief & David McDermott, *Interpretable Context Methodology: Folder Structure as Agentic Architecture* (ICM / MWP, arXiv:2603.16021v2)  
> **Core Ratio**: 60% Infrastructure | 30% Pure Markdown Orchestration | 10% Local Cognition  
> **Token Discipline**: Initial Stage Entry Frame strictly between 2,000 and 8,000 tokens

---

## 1. The Core Problem: Why Monolithic Prompts & Flat Workspaces Fail

In real-world software engineering, autonomous coding agents frequently degrade after 3–5 interaction turns, exhibiting three classic failure modes:
1. **Instruction Decay ("Lost in the Middle")**: When hard security invariants, procedural instructions, style preferences, and 200-line database schemas are crammed into a single 50K+ prompt, the transformer's attention over-indexes on the beginning and end of the prompt, treating middle operational constraints as soft guidelines.
2. **Context Bleed Across Workflow Stages**: An agent tasked with writing code in Stage 03 gets distracted by planning considerations from Stage 02 or requirements discussions from Stage 01 that have already been resolved.
3. **Rationalization and Loops**: When an execution failure occurs, an agent without a strict pre-requisite contract will rewrite its internal definition of success rather than fixing the underlying code bug.

Jake Van Clief's Interpretable Context Methodology (ICM) solves this by enforcing **Stage-Scoped Progressive Context Disclosure** over an externalized filesystem state machine.

---

## 2. The Tripartite Contract: Invariants, Rules, References

Every project, sub-stage, and evaluation suite must structure its context into four isolated, single-responsibility files:

```
target_task_or_benchmark/
├── CONTEXT.md       # Layer 1/2 Routing & Handoff Contract (<= 80 lines)
├── invariants.md    # Layer 2/3 Hard "Never" Operational Bounds (<= 80 lines)
├── rules.md         # Layer 2/3 Procedural "Always / Heuristics" Protocol (<= 120 lines)
├── references.md    # Layer 3 Machine-Readable Factory Schemas (<= 200 lines)
└── output/          # Layer 4 Dynamic Handoff Artifact Directory (.gitkeep)
```

### 2.1 File Responsibilities & Constraints

| File | ICM Role | Attention Mode | Strict Line Cap | Core Question Answered |
| :--- | :--- | :--- | :--- | :--- |
| **`invariants.md`** | Contract | Prescriptive (Hard Constraint) | $\le 80$ lines | *"What must NEVER happen under any circumstances?"* |
| **`rules.md`** | Contract | Procedural (Execution Protocol) | $\le 120$ lines | *"In what exact order and manner should actions be taken?"* |
| **`references.md`** | Factory | Descriptive (Passive Data) | $\le 200$ lines | *"What factual schemas, APIs, or interfaces are available?"* |
| **`CONTEXT.md`** | Catalog | Routing / State Machine | $\le 80$ lines | *"Where did the inputs come from, and where do outputs go?"* |

### 2.2 The 4-Section Canonical Stage Contract (`CONTEXT.md`)

Every `CONTEXT.md` follows a strict 4-section schema:
1. **`## Inputs`**: Uses **Selective Section Routing** to declare exact file paths and heading anchors (e.g., `../02-plan/output/plan.md#Diffs`). It never instructs the agent to scan entire folders unprompted.
2. **`## Process`**: Numbered, step-by-step procedural workflow referencing the tools to call in sequence.
3. **`## Outputs`**: Declares the exact path and format of the output artifact to write to `output/`.
4. **`## Verify`**: Falsifiable verification checklist and deterministic contract command (e.g., `bash contract.sh`) that must succeed before the stage is marked complete.

---

## 3. The 2,000–8,000 Token Active Working Frame vs. 128K Buffer

A common misunderstanding is whether a 2,000–8,000 token limit means the model's physical context window is truncated. As established in GDR30:

- **Initial Stage Entry Frame (2,000–8,000 tokens)**: When Hermes enters a stage, it loads **only**:
  - Layer 0 Identity (`AGENTS.md`): ~500 tokens
  - Layer 1 Workspace Router (`CONTEXT.md`): ~300 tokens
  - Layer 2 Stage Contract (`CONTEXT.md` + `invariants.md` + `rules.md`): ~1,200 tokens
  - Layer 3 Selective Reference: ~800 tokens
  - Layer 4 Prior Output Artifact (`output/plan.md`): ~1,000–3,000 tokens
  - **Total**: ~3,800–5,800 tokens. This guarantees pristine attention sharpness and zero distraction.
- **Intra-Stage Execution Arena (64K Physical Buffer on Bolt / 128K on Gemma)**: Once the stage starts, Hermes invokes tools, compiles code, runs ast-grep queries, and inspects test outputs. This ephemeral trace dynamically expands within the physical 65,536-token KV cache on Port 8138 (or 131,072-token on Gemma 4).
- **Stage Exit & Reset**: Once the stage writes its verified deliverable to `output/`, the multi-turn conversational trace is dropped. The next stage initializes with a fresh, pristine 2,000–8,000 token frame.

---

## 4. Instantiation Workflow: "Copy from Templates"

Under icm-architect Invariant 10 (*Instantiate by copying*), developers and agents must never author bespoke scaffolding from scratch. Instead, workspaces copy from the certified starter templates:

```bash
# For a new phase or feature development:
cp -r _templates/phase_template/ phases/phase_56_feature_name/

# For a new benchmark or real-world gauntlet:
cp -r _templates/benchmark_template/ benchmarks/gauntlet_name/
```

Every instantiated template already contains:
- `CONTEXT.md` (pre-populated with 4-section routing schema)
- `invariants.md` (pre-populated with hardware ceilings and zero-bespoke rules)
- `rules.md` (pre-populated with Two-Strike Tabu and linting standards)
- `references.md` (pre-populated with port tables and interface templates)
- `output/.gitkeep` (empty product directory ready for stage handoffs)
