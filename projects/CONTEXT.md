# projects - Multi-Project Workspace Shelf

Shelf for independent, self-contained project workspaces under the ws-hermes umbrella.

## Projects Catalog

| Project ID | Directory | Role / Domain | Entry Contract |
| :--- | :--- | :--- | :--- |
| `project1` | `hermes/` | Hermes Agent OS (Compiler pipeline, gauntlets, ledger) | `hermes/AGENTS.md` |
| `project2` | `project2/` | Reserved for auxiliary project workspace | `project2/AGENTS.md` |

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| System Invariants | `../_config/invariants.md` | Hardware & VRAM | Global limits apply to all projects |
| Templates | `../_templates/` | Full directory | Starter templates for new projects |

## Process

> 1. Project 1 (Hermes) lives in `projects/hermes/` with root backward-compatibility symlinks.
> 2. To add an auxiliary project (for example, `project2`):
>    a. Create a self-contained folder under `projects/project2/`.
>    b. Add a local `project2/AGENTS.md` and `project2/CONTEXT.md`.
>    c. Deploy sequential stage directories under `project2/stages/`.
> 3. Enforce context takeover: when an agent enters `project2/`, it reads `project2/AGENTS.md` and ignores `project1`.
> 4. Never import execution scripts across sibling projects (Zero Cross-Talk).

## Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Project Workspaces | `projects/*/` | Self-contained ICM directories |
| Project Index | `projects/_index.md` | Generated catalog |

## Check

Run `python3 -I _tools/links.py . --skip docs --skip phases` from the workspace root.
