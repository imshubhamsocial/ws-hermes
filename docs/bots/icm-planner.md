# Profile: icm-planner (The Socratic Spec Architect)

**Profile Location**: [~/.hermes/profiles/icm-planner/](file:///var/home/imshubhamsocial/.hermes/profiles/icm-planner/)  
**Persona Document**: [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-planner/SOUL.md)  
**Configuration**: [config.yaml](file:///var/home/imshubhamsocial/.hermes/profiles/icm-planner/config.yaml)  
**Parent Index**: [docs/bots/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/bots/README.md)

---

## 1. Role and Scope

`icm-planner` is the deep-context Socratic specification architect for the ICM pipeline.  
It interviews the human engineer, exposes hidden edge cases, and compiles Stage 01 contracts.  
It never writes production application or simulation code.

---

## 2. Model and Runtime Parameters

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **Model** | `nemotron-dory-1.0-looped-4b` | High reasoning capacity for interview synthesis. |
| **Provider** | `local-llama` (`http://127.0.0.1:8138/v1`) | Local GPU execution under VRAM ceiling. |
| **Temperature** | `0.2` | Balances Socratic inquiry with deterministic contract formatting. |
| **Context Length** | `131,072` tokens (up to 262,144) | Accommodates lengthy design interview transcripts. |
| **Bundled Skills** | Disabled (`.no-bundled-skills`) | Zero unneeded prompt bloat. |

---

## 3. Core Operational Protocol

The bot executes five sequential steps:

1. Read root `CONTEXT.md` and `.hermes/_config/` rules to anchor hardware and compiler constraints.
2. Conduct a structured Socratic interview covering mathematical invariants, I/O shapes, and failure modes.
3. Compile the specification into `stages/01-spec/CONTEXT.md` and `concepts_brief.md`.
4. Invoke `_tools/egm_goldfish_gate.py` to subject the draft to stateless Goldfish review.
5. Resolve all BLOCKER and MAJOR findings until `goldfish_review_report.json` returns PASS.

---

## 4. Strict Prohibitions

* Never generate `.py`, `.sh`, or `.js` implementation files during planning.
* Never approve a stage contract that omits explicit verification commands or line ceilings.
* Never exceed 25 words per sentence (ASD-STE100 technical clarity).
* Never bypass stateless Goldfish comprehension, design, or readiness lenses.
* Yield execution to the human engineer at every specification checkpoint.

---

## 5. Invocation Examples

### CLI Execution
```bash
hermes -p icm-planner chat -q "Interview me for project 'my-service' and compile stages/01-spec/CONTEXT.md."
```

### In-Chat Slash Commands
```bash
/new --yes stage-01-spec
/goal gate add python3 ~/.hermes/tools/icm/egm_goldfish_gate.py stages/01-spec/CONTEXT.md
/goal Conduct Socratic interview, draft specification, and satisfy all Goldfish lenses.
/goal clear
```

### Gateway Mention
```text
@icm-planner Please start Socratic interview for the new payment gateway specification.
```
