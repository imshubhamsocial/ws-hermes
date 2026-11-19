# Skill: icm-stage-compiler Reference

**Canonical Skill Location**: [.hermes/skills/icm/icm-stage-compiler/](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/)  
**Main Specification**: [SKILL.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/SKILL.md)  
**NVIDIA SkillEvaluator Score**: **100.0 / 100.0 (Grade: A, Warnings: 0)**  
**Parent Index**: [docs/skills/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/skills/README.md)

---

## 1. Skill Overview

`icm-stage-compiler` is the core single-pass stage compiler skill for the ICM state machine.  
It enables an agent to compile, execute, and verify stage contracts sequentially.  
It enforces all 10 Non-Negotiable Compiler Rules during code generation.

---

## 2. Bundled Scripts and Tool Manifest

The skill bundles three deterministic Python scripts in its `scripts/` directory:

| Script Path | Line Count | Function | Verification Role |
| :--- | :--- | :--- | :--- |
| [scripts/verify_stage.py](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py) | 39 lines | Validates stage directory structure, `CONTEXT.md`, and output directory. | Pre-execution contract check |
| [scripts/hermes_icm_validator.py](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/scripts/hermes_icm_validator.py) | 57 lines | Validates core files, line ceilings, and required section headers. | Static workspace validator |
| [scripts/hermes_stage_runner.py](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/scripts/hermes_stage_runner.py) | 57 lines | Executes stage verification scripts deterministically. | Automated test runner |

All scripts strictly obey Rule 6 (atomic scripts under 60 lines).

---

## 3. Skill Metadata and Frontmatter

The frontmatter defines the tool capabilities and execution scope:

```yaml
---
name: icm-stage-compiler
description: "Compiles, runs, and verifies single-pass stage contracts in the Interpretable Context Methodology (ICM) architecture."
tools:
  - bash
  - python
  - read_file
  - write_file
  - edit_file
---
```

---

## 4. Operational Invariants Enforced by the Skill

1. **One Stage, One Job**: Compiles only the target stage folder.
2. **Bounded Context**: Ingests only files explicitly listed in the stage's `Inputs` section.
3. **Docs Over Outputs**: Learns implementation patterns only from Layer 3 invariants.
4. **Header Compliance**: Enforces required Markdown sections:
   - `## 1. Identity and Workspace Map`
   - `## 2. Core Directory Locations`
   - `## 3. Ten Non-Negotiable Compiler Rules`
5. **Atomic Line Ceiling**: Rejects any generated script containing 60 lines or more.

---

## 5. Usage in Stage Workflows

Agents invoke the skill directly during multi-stage runs:

```bash
# Verify stage readiness
python3 .hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py stages/02-scaffold

# Run stage execution
python3 .hermes/skills/icm/icm-stage-compiler/scripts/hermes_stage_runner.py stages/02-scaffold
```
