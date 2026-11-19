# Invariants, Scoping, and Path Isolation

**Standard**: Interpretable Context Methodology (ICM) Isolation Architecture  
**Language Standard**: ASD-STE100  
**Parent Index**: [docs/architecture/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/architecture/README.md)

---

## 1. Directory Scoping: Agent OS vs Project Workspaces

Hermes strictly isolates the Agent OS substrate from project-specific domains:

### Architectural Separation
* **`.hermes/`**: Houses Agent OS configs (`pyproject.toml`, `package.json`, `distrobox.ini`), developer profiles, tools, and skills.
* **`benchmarks/`**: Houses self-contained project gauntlets, project-level configurations, templates, and archives.
* **Elimination of Root Symlinks**: Symlinks at the workspace root have been eliminated. Each domain references its own configuration directly.

---

## 2. Path Portability: Relative vs Absolute Paths

To ensure portable skills and reproducible stages, follow these path rules:

1. **Root Scoping**: Use relative paths (`cwd: .` or `./`) for project and stage references.
2. **User Home Scoping**: Use standard tilde expansion (`~/.hermes/...`) for machine-level tool and profile locations.
3. **Prohibition of Machine-Hardcoded Paths**: Never hardcode user paths like `/var/home/imshubhamsocial/` inside portable configuration files or reusable stage contracts.

---

## 3. Hardware Ceilings and Resource Boundaries

All execution runs on local hardware under strict ceilings:

| Hardware Ceiling | Maximum Allowed Limit | Verification Tool |
| :--- | :--- | :--- |
| **GPU VRAM Ceiling** | **$5,800.0$ MiB** | [check_vram_limit.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/check_vram_limit.py) |
| **LLM Inference Port** | `127.0.0.1:8138` | `llama-server.service` |
| **Active Champion Model** | `gemma-4-exact-4b` | TurboQuant Q4_0 KV Cache |
| **Script Physical Lines** | $\le 59$ lines | [hermes_icm_validator.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/hermes_icm_validator.py) |
| **Layer 0 Token Ceiling** | $\le 800$ tokens | [icm_context_auditor.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/icm_context_auditor.py) |
| **Layer 1 Token Ceiling** | $\le 300$ tokens | [icm_context_auditor.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/icm_context_auditor.py) |
| **Layer 2 Token Ceiling** | $\le 500$ tokens | [icm_context_auditor.py](file:///var/home/imshubhamsocial/.hermes/tools/icm/icm_context_auditor.py) |

Any test run exceeding these ceilings triggers an immediate test failure.
