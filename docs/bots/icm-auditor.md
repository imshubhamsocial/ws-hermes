# Profile: icm-auditor (Deterministic Read-Only Substrate Auditor)

**Profile Location**: [~/.hermes/profiles/icm-auditor/](file:///var/home/imshubhamsocial/.hermes/profiles/icm-auditor/)  
**Persona Document**: [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-auditor/SOUL.md)  
**Configuration**: [config.yaml](file:///var/home/imshubhamsocial/.hermes/profiles/icm-auditor/config.yaml)  
**Parent Index**: [docs/bots/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/bots/README.md)

---

## 1. Role and Scope

`icm-auditor` is a zero-context, read-only verification auditor for workspaces and `~/.hermes/`.  
It never modifies source files or directories.  
It executes verification scripts and emits deterministic PASS/FAIL diagnostics.

---

## 2. Model and Runtime Parameters

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **Model** | `gemma-4-exact-4b` | Strict adherence to verification rubrics and zero hallucination. |
| **Provider** | `openai_compatible` (`http://127.0.0.1:8138/v1`) | Local GPU execution. |
| **Temperature** | `0.0` | Absolute determinism during auditing. |
| **Context Length** | `131,072` tokens | Wide window for long test logs and diagnostic outputs. |
| **Terminal Mode** | `read_only: true` | Hardware/filesystem protection: refuses file write operations. |

---

## 3. Core Operational Protocol

The bot executes four verification passes:

1. Execute `~/.hermes/tools/icm/icm_context_auditor.py` to verify layer token budgets.
2. Execute `~/.hermes/tools/icm/audit_hermes_home.sh` to verify Rule 9 substrate purity.
3. Verify that every Python, Bash, and JavaScript script is strictly under 60 lines.
4. Run SkillEvaluator Tier 1 static checks (`--no-llm`) across `~/.hermes/skills/icm/`.

---

## 4. Architectural Constraints

* Emit deterministic JSON or tabular PASS/FAIL diagnostics with exact file paths.
* Flag any GPU VRAM reading above 5,800.0 MiB.
* Flag any modified or untracked file in `~/.hermes/hermes-agent`.
* Refuse any instruction requesting code creation, file editing, or deletion.

---

## 5. Invocation Examples

### CLI Execution
```bash
hermes -p icm-auditor chat -q "Audit ~/.hermes/ for substrate purity, script line ceilings, and VRAM limits."
```

### In-Chat Slash Commands
```bash
/new --yes substrate-audit
/goal gate add bash ~/.hermes/tools/icm/audit_hermes_home.sh
/goal Run complete substrate purity audit and report all findings.
/goal clear
```

### Gateway Mention
```text
@icm-auditor Run a read-only audit of the workspace and report any script exceeding 59 lines.
```
