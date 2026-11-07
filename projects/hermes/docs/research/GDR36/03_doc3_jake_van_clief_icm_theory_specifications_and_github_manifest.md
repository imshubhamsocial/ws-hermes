# Document 03: Jake Van Clief ICM Theory, Upstream Specifications, and GitHub Ecosystem

> **Standard**: ASD-STE100 (Simplified Technical English)  
> **Release Package**: GDR36  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44  
> **Academic Foundation**: *Interpretable Context Methodology: Folder Structure as Agent Architecture* (Jake Van Clief & David McDermott, arXiv:2603.16021)  
> **Ecosystem Sources**:
> - `RinDig/Interpretable-Context-Methodology` (`https://raw.githubusercontent.com/RinDig/Interpretable-Context-Methodology/main/README.md`)
> - `_core/CONVENTIONS.md` (`https://raw.githubusercontent.com/RinDig/Interpretable-Context-Methodology/main/_core/CONVENTIONS.md`)
> - `ktnCodes/icm-template` (`https://raw.githubusercontent.com/ktnCodes/icm-template/master/README.md`)
> - `RinDig/icm-architect` (`https://raw.githubusercontent.com/RinDig/icm-architect/main/SKILL.md`)

---

## 1. RinDig / Interpretable-Context-Methodology Specifications

The Interpretable Context Methodology (ICM) replaces complex orchestration code with filesystem structure.
Numbered folders provide sequencing.
Directory hierarchies provide context scoping.
Plain markdown files provide state.

### 1.1 The Five-Layer Routing Architecture

```
Layer 0: CLAUDE.md           "Where am I?"            Always loaded (~800 tokens)
Layer 1: CONTEXT.md          "Where do I go?"          Read on entry (~300 tokens)
Layer 2: Stage CONTEXT.md    "What do I do?"            Read per-task (~200-500 tokens)
Layer 3: Reference material  "What rules apply?"        Loaded selectively (varies)
Layer 4: Working artifacts   "What am I working with?"  Loaded selectively (varies)
```

- **Layer 0 (`CLAUDE.md` / `AGENTS.md`)**: Automatically loaded by coding agents. Contains workspace directory maps, naming conventions, and routing pointers. Budget: ~800 tokens.
- **Layer 1 (`CONTEXT.md` at root)**: Read by agents on initial entry. Maps specific tasks to corresponding stage directories. Budget: ~300 tokens.
- **Layer 2 (Stage `CONTEXT.md`)**: Located inside each stage folder. Defines inputs, execution process, and output artifacts. Budget: 200–500 tokens.
- **Layer 3 (Reference Material)**: Stable rules, design systems, voice guides, and APIs. Configured once; remains stable across runs. Loaded selectively.
- **Layer 4 (Working Artifacts)**: Dynamic per-run outputs, previous stage deliverables, and temporary files. Loaded selectively.

### 1.2 The Canonical Workspace Directory Structure

```
workspace/
  CONTEXT.md               # Layer 1: task routing
  stages/
    01-research/
      CONTEXT.md            # Layer 2: stage contract
      references/           # Layer 3: reference material for this stage
      output/               # Layer 4: working artifacts
    02-script/
      CONTEXT.md
      references/
      output/
    03-production/
      CONTEXT.md
      references/
      output/
  _config/                  # Layer 3: brand, voice, design system
  shared/                   # Layer 3: cross-stage resources
  skills/                   # Layer 3: bundled domain knowledge
  setup/
    questionnaire.md        # One-time onboarding
```

### 1.3 The Stage Contract Schema

Every stage `CONTEXT.md` follows an exact three-section schema:

```markdown
## Inputs
| Source | File/Location | Section/Scope | Why |
|---|---|---|---|
| Previous stage | ../01-research/output/ | Full file | Source material |
| Style guide | ../../brand-vault/voice-rules.md | Voice Rules section | Tone guidance |

## Process
1. Read the research output
2. Identify the narrative angle
3. Write the script following voice-rules
4. Run audit checks
5. Save to output/

## Outputs
| Artifact | Location | Format |
|---|---|---|
| Script | output/[slug]-script.md | Markdown with metadata header |
```

### 1.4 Available Workspaces in RinDig Repository

The upstream repository provides three reference implementations:

| Workspace | Functionality Description | Number of Stages |
| :--- | :--- | :--- |
| **`script-to-animation`** | Converts a content idea into script writing, animation specification, and Remotion video code. | 3 stages |
| **`course-deck-production`** | Converts unstructured source material (PDFs, research papers, notes) into polished PowerPoint slide decks. | 5 stages |
| **`workspace-builder`** | A meta-workspace whose output is a complete new ICM workspace configured for any arbitrary domain. | 5 stages |

### 1.5 Instructions to Build Your Own Workspace

1. Enter directory: `cd workspaces/workspace-builder`
2. Run setup: execute `setup` to describe your target domain.
3. Complete the five stages: discovery, mapping, scaffolding, questionnaire design, and validation.
4. Obtain output: the output is a fully functional, self-contained ICM workspace ready for production.

---

## 2. ktnCodes / icm-template Specifications

The `ktnCodes/icm-template` repository provides a model-agnostic implementation of ICM extended with Andrej Karpathy's LLM knowledge base compilation pattern.

### 2.1 Quick Start — Install the Skills

To install the skills in your local agent skills directory:

```bash
# Clone this repo
git clone https://github.com/ktncodes/icm-template.git

# Copy all skills to your agent skills
cp -r icm-template/SKILLS/icm-scaffold ~/.claude/skills/icm-scaffold
cp -r icm-template/SKILLS/icm-sync ~/.claude/skills/icm-sync
cp -r icm-template/SKILLS/icm-context-scaffold ~/.claude/skills/icm-context-scaffold
```

Available skill commands:

| Skill | Purpose |
| :--- | :--- |
| `/icm-scaffold` | Set up ICM on a project — generates `IDENTITY.md`, `CONTEXT.md`, and `_config/`. |
| `/icm-sync` | Keep ICM routing accurate — syncs `IDENTITY.md` and `CONTEXT.md` with disk state. |
| `/icm-context-scaffold` | Fill gaps — generates missing `CONTEXT.md` files across the workspace. |

### 2.2 What You Get

The skill generates an ICM layer on top of an existing project:

```
your-project/
├── IDENTITY.md     # Layer 0 — "Where am I?" (workspace map)
├── CONTEXT.md      # Layer 1 — "Where do I go?" (task routing)
├── _config/        # Layer 3 — "What rules apply?" (conventions, glossary, voice)
│   ├── conventions.md
│   ├── glossary.md
│   ├── voice.md
│   └── article-template.md  (if content generation project)
└── [your existing folders stay untouched]
```

- **Quick mode (default)**: 3 layers — routing and reference only. Adds ICM to an existing project without restructuring.
- **Full mode**: 5 layers — adds physical stage folders with contracts and output directories for new pipelines.

### 2.3 The Five Layers Table

| Layer | File | Question | Token Budget |
| :--- | :--- | :--- | :--- |
| **0** | `IDENTITY.md` | "Where am I?" | ~800 tokens |
| **1** | Root `CONTEXT.md` | "Where do I go?" | ~300 tokens |
| **2** | Stage `CONTEXT.md` | "What do I do?" | 200–500 tokens |
| **3** | `_config/`, `references/` | "What rules apply?" | 500–2,000 tokens |
| **4** | `output/` | "What am I working with?" | varies |

### 2.4 The Compilation Metaphor

Karpathy's LLM knowledge base architecture (raw $\to$ compile $\to$ wiki $\to$ Q&A) maps directly onto ICM stages:

| Karpathy Stage | ICM Equivalent | What Happens |
| :--- | :--- | :--- |
| **Raw** | Layer 4 inputs | Source documents, notes, transcripts — unstructured. |
| **Compile** | Stage 2 | LLM reads raw sources $\to$ produces structured articles with citations. |
| **Wiki** | Layer 4 outputs | Compiled, cross-referenced articles organized by topic. |
| **Q&A** | Layer 1 routing | LLM reads index files to navigate compiled knowledge. |

### 2.5 The Five Principles

1. **One stage, one job**: Each stage does one thing and writes to its own output folder.
2. **Plain text as the interface**: Markdown files; no proprietary binary formats or database servers.
3. **Layered context loading**: Load only what the current stage needs.
4. **Every output is an edit surface**: Review and edit artifacts between stages.
5. **Configure the factory, not the product**: Set up rules once; produce repeatedly.

### 2.6 Documentation Section with Tier 4 Raw Links

All links mentioned in the documentation section of `ktnCodes/icm-template`:

- **Methodology**: `https://raw.githubusercontent.com/ktnCodes/icm-template/master/docs/methodology.md`
- **Best Practices**: `https://raw.githubusercontent.com/ktnCodes/icm-template/master/docs/best-practices.md`
- **Layer Reference**: `https://raw.githubusercontent.com/ktnCodes/icm-template/master/docs/layer-reference.md`
- **Model Adapters**: `https://raw.githubusercontent.com/ktnCodes/icm-template/master/docs/model-adapters.md`
- **Original Paper (PDF)**: `https://raw.githubusercontent.com/ktnCodes/icm-template/master/docs/Interpretable_Context_Methdology_.pdf`

---

## 3. RinDig / icm-architect Specifications

The `RinDig/icm-architect` repository provides an open agent skill that designs any process into an ICM workspace or restructures an existing folder tree into one.

### 3.1 The Ten Invariants

1. **One folder, one job**: Each folder executes a single step or holds a single kind of artifact.
2. **A small, stable entry file**: `AGENTS.md` at root answers "where am I, where does everything live, where do I go for task X" in under ~60 lines.
3. **Numbering encodes order**: `01_`, `02_`, ... where execution sequence matters.
4. **Every working folder has a contract**: A `CONTEXT.md` defining inputs, process, outputs, and checks.
5. **Factory vs product**: Reference material (stable rules) lives separate from working artifacts (per-run outputs).
6. **Every step ends at a check**: Output is verified before moving downstream. A failed check stops the pipeline.
7. **Load only what the step needs**: Keep prompt context under 8,000 tokens. Prevent context bloating.
8. **Plain text, linkable, queryable**: Markdown with YAML frontmatter. Relative links that resolve.
9. **Status lives on disk**: What exists on disk represents true system state.
10. **Instantiate by copying**: New units of work are created by copying templates from `_templates/`.

### 3.2 Three Primitives and Five Forms

- **Three Primitives**:
  1. *Sequence*: Numbered folders where each step's output is the next step's input.
  2. *Shelf*: A folder holding same-shaped files copied from one template.
  3. *Catalog*: A small file that points down and contains no bulky content.
- **Five Forms**: Pipeline, Record library, Knowledge bundle, Context map, and System map.

### 3.3 Skill Installation Matrix Across Agent Ecosystems

| Agent Substrate | Installation Directory / Command |
| :--- | :--- |
| **Hermes Agent** | `~/.hermes/skills/icm-architect` or list directory in `config.yaml` under `skills.external_dirs`. |
| **Gemini CLI** | `~/.gemini/skills/` or `~/.agents/skills/`, or run `gemini skills install <repo-url>`. |
| **Codex** | `~/.agents/skills/` (global) or `.agents/skills/` (per-repo). |
| **Claude Code** | `~/.claude/skills/` or `.claude/skills/`. |
| **Cursor / Copilot** | Client-specific agent skills folder. |

### 3.4 Canonical Stage CONTEXT.md Contract Template

```markdown
# {NN}_{stage-name} - {the job in five words}

One job: {the single thing this stage does}.

## Inputs
- Working (this run): `../{prev-stage-folder}/output/{file}`
- Reference (every run): `../../_shared/{rules-file}.md`
- Reference (every run): `references/{stage-specific-guide}.md`
- Example (optional): `examples/`

Do NOT load: {anything an eager agent would wrongly pull in}.

## Process
1. If an input is missing or empty, stop and say which.
2. {Transform following reference constraints.}
3. {Hard limits: length, count, format.}

## Outputs
- `{artifact}.md` -> `output/`

## Check
{Who or what checks: human review, script execution, or validator. Writes check.md beside output.}
```

---

## 4. RinDig / agentless Specifications

The `RinDig/agentless` repository is an open-source Claude Code skill that builds an agent or team as a folder of markdown.
It was created by Jake Van Clief as an ICM-based alternative to heavy agent frameworks like Agentlas OS.

### 4.1 The Core Philosophy: Method Document vs. Worker with Capabilities

Agentlas OS requires 2,058 files, 339,886 lines of Python code, 88 JSON schemas, and 28 to 31 required files per package.
In contrast, `agentless` implements one foundational premise:
> *"An agent package is not a worker with capabilities. It is a method document."*

A method document is a structured folder of markdown files:
- Numbered folders hold the execution sequence.
- Each folder's `CONTEXT.md` holds its single job.
- Files on disk hold the current system state.
- `agentless` contains only 225 lines of markdown across `SKILL.md` and seven starter templates.
- It requires zero Python dependencies, zero JSON schemas, and zero daemon services.

### 4.2 Side-by-Side Comparison: Agentlas OS vs. Agentless

| Architectural Dimension | Agentlas OS (Heavy Framework) | Agentless (ICM Skill) |
| :--- | :--- | :--- |
| **Codebase Footprint** | 339,886 lines of Python, 88 JSON schemas | 225 lines of markdown, 0 Python lines |
| **Package Structure** | 28 to 31 mandatory files per package | 1 folder with numbered stage subdirectories |
| **Onboarding Protocol** | 8 to 12 questions with ambiguity scoring | 2 to 4 direct questions about run workflow |
| **Verification Gate** | Independent verifier with JSON receipts | Check stage in a fresh context; output files are receipts |
| **Memory Architecture** | Memory Events, Tickets, Curator, PM Soul | Simple "Proposed" list in `rules.md`; human keeps or cuts |
| **Host Integration** | Complex installation writing into 11 hosts | Simple git clone into local skills directory |
| **Audit Requirement** | Rigid JSON schema length validation | The Walk Test: fresh agent navigates from `AGENTS.md` |

### 4.3 Empirical Findings on Instruction Length and Attention Degradation

The documentation of `agentless` cites empirical benchmark measurements demonstrating how context pollution degrades model performance:
- A **54-word instruction** pointing at external rule files scored **7.00 out of 7** across two test models.
- A **652-word instruction** scored **6.33 and 5.00**.
- A **4,115-word instruction** (with entire rule sheets pasted inline) scored only **5.67 and 6.00**.

Conclusion: Models follow instructions significantly better when prompts point to external files rather than pasting heavy rule documents into the prompt buffer.

### 4.4 The Walk Test and Fresh Context Verification

- **The Walk Test**: A fresh agent with no conversational memory must orient itself, identify where a run starts, and understand the next step from `AGENTS.md` plus at most two additional files.
- **Fresh Context for Auditing**: The context that generates an output must never grade that output. The final check stage runs in a clean, fresh context window to ensure objective evaluation.

---

## 5. Multimedia Systems and Video Research Corpus

This section compiles the six key video presentations and empirical analyses for deep research ingestion:

### 5.1 Video 1: "We Built Multiplayer AI, No New Agents Needed"
- **Author**: Jake Van Clief
- **Canonical URL**: `https://www.youtube.com/watch?v=qzVXfVvXbXU`
- **Core Subject**: Demonstrates how multiple humans and AI agents collaborate synchronously using folders as the shared state machine. Rather than using central WebSocket servers or database coordination, filesystem markdown files serve as the universal synchronization layer.

### 5.2 Video 2: "Do You Actually Need AI Agents? (Why I Use Folders Instead)"
- **Author**: Jake Van Clief
- **Canonical URL**: `https://www.youtube.com/watch?v=m7en7ugujlI`
- **Core Subject**: The foundational critique of multi-agent software frameworks. Explains how black-box agent loops create silent cascading failures, memory fragmentation, and token budget exhaustion. Demonstrates how ICM folders turn opaque agent swarms into transparent, human-auditable workflows.

### 5.3 Video 3: "Is Jake Van Clief a Charlatan? [ICM Folder Structure Shown Live]"
- **Author**: RyMac
- **Canonical URL**: `https://www.youtube.com/watch?v=NMAgustrvJU`
- **Core Subject**: Independent empirical evaluation and live demonstration of the ICM folder methodology. Tests the claims against complex development tasks, demonstrating that folder-based stage compilation outperforms monolithic agent prompts in consistency and maintainability.

### 5.4 Video 4: "Systems Thinking for People Who Build With AI"
- **Author**: Jake Van Clief
- **Canonical URL**: `https://www.youtube.com/watch?v=NWyTsKTKka8`
- **Core Subject**: Comprehensive 90-minute masterclass on systems engineering applied to autonomous AI. Details feedback control theory, bounded contexts, error propagation limits, and the compilation metaphor.

### 5.5 Video 5: "Stop Building AI Agents. Use This Folder System Instead."
- **Author**: Jake Van Clief
- **Canonical URL**: `https://www.youtube.com/watch?v=MkN-ss2Nl10`
- **Core Subject**: Deep dive into the 5-layer folder architecture. Details the 2,000–8,000 token working context boundary, "one stage, one job", and why plain markdown files beat vector databases and multi-agent frameworks.

### 5.6 Video 6: "Reaction to Jake Van Clief's Folder System"
- **Author**: iScaleLabs
- **Canonical URL**: `https://www.youtube.com/watch?v=KPVaUuBkPz8`
- **Core Subject**: Industrial review and architectural reaction. Examines the economic benefits, token savings, and quality assurance advantages of replacing monolithic agent prompts with modular ICM compiler pipelines.
