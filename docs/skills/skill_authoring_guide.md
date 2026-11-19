# Skill Authoring & Certification Guide

**Target Audience**: Autonomous Agents & System Engineers  
**Evaluation Standard**: NVIDIA SkillEvaluator (Version 1.0.1+)  
**Language Standard**: ASD-STE100  
**Parent Index**: [docs/skills/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/skills/README.md)

---

## 1. Directory Structure Requirements

Every skill must reside in its own folder under `.hermes/skills/icm/<skill-name>/` or `~/.hermes/skills/icm/<skill-name>/`:

```text
my-new-skill/
├── SKILL.md            # Required: Instructions with YAML frontmatter
├── scripts/            # Required: Modular Python/Bash scripts (<60 lines)
│   └── helper.py
└── references/         # Optional: Schemas, templates, or test assets
```

---

## 2. YAML Frontmatter Specification

The frontmatter in `SKILL.md` must be valid YAML enclosed in triple dashes (`---`).  
It must contain at least `name` and `description`:

```yaml
---
name: my-new-skill
description: "Brief imperative description under 200 characters explaining exact capability."
tools:
  - bash
  - python
  - read_file
---
```

### Frontmatter Rules
* Do not leave unclosed quotes or invalid indentation.
* Do not use generic words like `various`, `etc.`, or `miscellaneous`.
* Name must use lowercase alphanumeric characters and hyphens only.

---

## 3. The 60-Line Ceiling (Rule 6)

Every script inside `scripts/` must contain strictly fewer than 60 physical lines ($\le 59$ lines).  
A file with 60 lines or more fails static evaluation.

### Authoring Best Practices
* One script, one function.
* Condense simple loops and list comprehensions.
* Move schemas or long configuration constants into `references/`.
* Avoid unnecessary blank lines or multi-line comment blocks.

---

## 4. Prompt and Markdown Hygiene (ASD-STE100)

* Keep sentences short ($\le 25$ words).
* Use active voice and imperative commands ("Execute...", "Verify...", "Compile...").
* Ensure balanced code fences (```) and math delimiters ($).
* Provide absolute or valid relative file paths.

---

## 5. Certification Verification Workflow

Before deploying a new skill, run the static check gate:

```bash
# 1. Audit line ceilings of all scripts
for f in scripts/*.py scripts/*.sh; do
    lines=$(wc -l < "$f")
    if [ "$lines" -ge 60 ]; then
        echo "FAIL: $f has $lines lines (limit: 59)"
        exit 1
    fi
done

# 2. Run NVIDIA SkillEvaluator static checks
python3 -m skill_evaluator.cli eval --skill-path . --no-llm
```

A passing skill produces:
```text
Score: 100.0/100.0 | Grade: A | Warnings: 0 | Status: PASS
```
