# hermes - Hermes Agent OS Project Domain

Hermes Agent OS project workspace and development tracks under ws-hermes.

## Tracks Catalog

| Track ID | Directory | Role / Domain | Entry Contract |
| :--- | :--- | :--- | :--- |
| `devel` | `devel/` | Active development (Compiler pipeline, gauntlets, phases, docs) | `devel/AGENTS.md` |

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| System Invariants | `devel/_config/invariants.md` | Hardware & VRAM | Global hardware bounds apply to all tracks |
| Templates | `devel/_templates/` | Full directory | Starter templates for new stages |

## Process

> 1. Hermes Agent OS development lives in `hermes/devel/`.
> 2. Route active compiler and gauntlet tasks directly to `hermes/devel/`.
> 3. Enforce context takeover: when an agent enters `hermes/devel/`, it reads `hermes/devel/AGENTS.md`.
> 4. Load only the files declared in the target stage or gauntlet contract.

## Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Track Workspaces | `hermes/*/` | Self-contained ICM directories |
| Track Index | `hermes/_index.md` | Generated catalog |

## Check

Run python3 -I hermes/devel/_tools/links.py . --skip docs --skip phases from the workspace root.
