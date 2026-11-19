# Profile: icm-scaffolder (Greenfield Workspace Architect)

**Profile Location**: [~/.hermes/profiles/icm-scaffolder/](file:///var/home/imshubhamsocial/.hermes/profiles/icm-scaffolder/)  
**Persona Document**: [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-scaffolder/SOUL.md)  
**Configuration**: [config.yaml](file:///var/home/imshubhamsocial/.hermes/profiles/icm-scaffolder/config.yaml)  
**Parent Index**: [docs/bots/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/bots/README.md)

---

## 1. Role and Scope

`icm-scaffolder` transforms approved Stage 01 specifications into 5-layer ICM filesystem hierarchies.  
It configures the factory directories (`_config/`, `shared/`, `stages/`) before product code runs.  
It compiles stage contracts and configures deterministic verification scripts.

---

## 2. Model and Runtime Parameters

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **Model** | `gemma-4-exact-4b` | High instruction fidelity for exact directory and file creation. |
| **Provider** | `openai_compatible` (`http://127.0.0.1:8138/v1`) | Local GPU execution with TurboQuant Q4_0 KV cache. |
| **Temperature** | `0.1` | Minimizes hallucination during structural code authoring. |
| **Context Length** | `131,072` tokens | Provides wide headroom for multi-stage contract synthesis. |
| **Turn Limit** | `8` turns (`goals.max_turns`) | Enforces bounded intra-stage execution. |

---

## 3. Core Operational Protocol

The bot executes four sequential steps:

1. Verify that `stages/01-spec/output/goldfish_review_report.json` exists and equals PASS.
2. Execute `~/.hermes/tools/icm/icm_scaffolder.py` against the target workspace root.
3. Populate Layer 0 (`IDENTITY.md`), Layer 1 (`CONTEXT.md`), and Layer 2 stage contracts.
4. Wire deterministic verification scripts into `_tools/` and stage output gates.

---

## 4. Architectural Constraints

* Keep Layer 0 under 800 tokens, Layer 1 under 300 tokens, and Layer 2 under 500 tokens.
* Enforce one-way dependencies across numbered stage directories (`stages/01-*` $\to$ `stages/02-*`).
* Never modify upstream files in `~/.hermes/hermes-agent`.
* Keep all generated helper scripts strictly under 60 lines.

---

## 5. Invocation Examples

### CLI Execution
```bash
hermes -p icm-scaffolder chat -q "Read spec review. Execute ~/.hermes/tools/icm/icm_scaffolder.py . to scaffold the workspace."
```

### In-Chat Slash Commands
```bash
/new --yes stage-02-scaffold
/goal gate add python3 ~/.hermes/tools/icm/hermes_icm_validator.py
/goal Read stages/02-scaffold/CONTEXT.md and scaffold all module contracts.
/goal clear
```

### Gateway Mention
```text
@icm-scaffolder Goldfish review passed. Scaffold the 5-layer ICM structure for this repository.
```
