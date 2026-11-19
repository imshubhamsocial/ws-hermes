# Profile: icm-migrator (Brownfield AST Repository Refactorer)

**Profile Location**: [~/.hermes/profiles/icm-migrator/](file:///var/home/imshubhamsocial/.hermes/profiles/icm-migrator/)  
**Persona Document**: [SOUL.md](file:///var/home/imshubhamsocial/.hermes/profiles/icm-migrator/SOUL.md)  
**Configuration**: [config.yaml](file:///var/home/imshubhamsocial/.hermes/profiles/icm-migrator/config.yaml)  
**Parent Index**: [docs/bots/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/bots/README.md)

---

## 1. Role and Scope

`icm-migrator` audits unstructured repositories and migrates them into the 5-layer ICM architecture.  
It classifies every file into exactly one of five buckets:
* **catalog**: Read-only documentation, specifications, and references.
* **contract**: Interfaces, schemas, and verification invariants.
* **factory**: Generators, builders, and tooling scripts.
* **product**: Output code, artifacts, and simulation assets.
* **dead**: Unused code, stale experiments, and orphaned files.

It decomposes monolithic scripts exceeding 59 lines into atomic modules under 60 lines.

---

## 2. Model and Runtime Parameters

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **Model** | `nemotron-dory-1.0-looped-4b` | Deep reasoning for AST traversal and dependency analysis. |
| **Provider** | `openai_compatible` (`http://127.0.0.1:8138/v1`) | Local GPU execution with TurboQuant Q4_0 KV cache. |
| **Temperature** | `0.0` | Maximum determinism during file classification and AST refactoring. |
| **Context Length** | `131,072` tokens | Accommodates large repository file manifests and dependency trees. |

---

## 3. Core Operational Protocol

The bot executes four sequential steps:

1. Run `~/.hermes/tools/icm/icm_repo_migrator.py` on the target repository path.
2. Inspect the generated AST dependency map and 5-bucket classification report.
3. Present `migration_map.json` to the engineer for checkpoint approval before moving files.
4. Decompose monolithic source files exceeding 59 lines into atomic modules under 60 lines.

---

## 4. Architectural Constraints

* Never delete files classified as dead without explicit human checkpoint approval.
* Ensure a memoryless agent passes the Walk Test using only migrated `CONTEXT.md` files.
* Keep all generated modules strictly under 60 lines.
* Maintain backward compatibility during all file moves.

---

## 5. Invocation Examples

### CLI Execution
```bash
hermes -p icm-migrator chat -q "Execute python3 ~/.hermes/tools/icm/icm_repo_migrator.py . to analyze and classify the repository."
```

### In-Chat Slash Commands
```bash
/new --yes repo-migration
/goal gate add python3 ~/.hermes/tools/icm/icm_repo_migrator.py . --verify-only
/goal Classify files into 5 buckets, emit migration_map.json, and refactor scripts over 59 lines.
/goal clear
```

### Gateway Mention
```text
@icm-migrator Analyze the legacy src/ directory, emit migration_map.json, and decompose files over 59 lines.
```
