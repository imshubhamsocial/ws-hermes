# Skills Ecosystem Reference Manual

**Substrate**: Hermes Agent OS & Interpretable Context Methodology (ICM)  
**Skill Directory**: `~/.hermes/skills/icm/` and `.hermes/skills/icm/`  
**Language Standard**: ASD-STE100  
**Parent Index**: [docs/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/README.md)

---

## 1. Skill Architecture in Hermes

Hermes skills are self-contained modular capabilities.  
Each skill lives in its own folder and contains:
* `SKILL.md`: Main instructions with YAML frontmatter (`name`, `description`).
* `scripts/`: Modular Python or Bash helper scripts (each strictly under 60 lines).
* `examples/` or `references/`: Optional schemas, prompts, or test fixtures.

---

## 2. NVIDIA SkillEvaluator Compliance

All custom skills must pass the NVIDIA SkillEvaluator test harness:

| Evaluation Tier | Focus | Checks Performed |
| :--- | :--- | :--- |
| **Tier 1 (Static)** | Structural & Frontmatter | Valid YAML, name/description presence, script permissions, file references. |
| **Tier 2 (Syntactic)** | Prompt Hygiene | ASD-STE100 clarity, zero vague placeholders, balanced code fences, no ungrounded imports. |
| **Tier 3 (Runtime)** | Execution & Sandbox | Deterministic script execution, exit code 0, no unhandled exceptions. |

Our primary compiler skill, [icm-stage-compiler](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/SKILL.md), achieved a certified score of **100.0/100 (Grade: A)** with zero warnings.

---

## 3. Skill Catalog

| Skill Name | Location | Primary Purpose | Certified Score |
| :--- | :--- | :--- | :--- |
| **`icm-stage-compiler`** | [.hermes/skills/icm/icm-stage-compiler/](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/skills/icm/icm-stage-compiler/) | Stage contract compilation and deterministic testing. | **100.0 / 100 (Grade A)** |
| **`icm-architect`** | `~/.hermes/skills/icm/icm-architect/` | Architectural design and multi-stage planning patterns. | Certified |

---

## 4. Documentation Links

* [icm-stage-compiler Reference](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/skills/icm-stage-compiler.md)
* [Skill Authoring & Certification Guide](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/skills/skill_authoring_guide.md)
