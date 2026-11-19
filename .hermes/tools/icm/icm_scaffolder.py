#!/usr/bin/env python3
"""Greenfield 5-Layer ICM Workspace Scaffolder (<60 lines)."""
import pathlib
import sys

STAGES = ["01-spec", "02-scaffold", "03-implement", "04-verify"]
CONFIG_FILES = {
    "conventions.md": "# Layer 3 Conventions\n- Scripts < 60 lines.\n- ASD-STE100 active prose.\n",
    "hardware_ceilings.md": "# Hardware Ceilings\n- RTX 3050 <= 5800.0 MiB.\n- Intel iGPU Wayland.\n",
    "glossary.md": "# ICM Glossary\n- Layer 0: IDENTITY.md\n- Layer 1: CONTEXT.md\n",
}

STAGE_TEMPLATE = """# Stage {stage} Contract (Layer 2)
## Inputs
| Source | Path | Section |
| :--- | :--- | :--- |
| Factory Rules | _config/conventions.md | All |

## Process Steps
1. Load strictly the declared inputs for Stage {stage}.
2. Execute the single bounded stage task and write artifacts to output/.

## Outputs
| Artifact | Target Path | Verification |
| :--- | :--- | :--- |
| Stage Deliverable | stages/{stage}/output/result.md | verify_stage.py |
"""

def scaffold_workspace(root: pathlib.Path) -> None:
    for folder in ["_config", "shared", "skills", "_tools", "setup"]:
        (root / folder).mkdir(parents=True, exist_ok=True)
    (root / "IDENTITY.md").write_text("# Layer 0 Identity\nWorkspace: " + root.name + "\n", encoding="utf-8")
    (root / "CONTEXT.md").write_text("# Layer 1 Routing\nRoute to stages/01-spec through 04-verify.\n", encoding="utf-8")
    for name, body in CONFIG_FILES.items():
        (root / "_config" / name).write_text(body, encoding="utf-8")
    for stg in STAGES:
        sdir = root / "stages" / stg
        (sdir / "references").mkdir(parents=True, exist_ok=True)
        (sdir / "output").mkdir(parents=True, exist_ok=True)
        (sdir / "CONTEXT.md").write_text(STAGE_TEMPLATE.format(stage=stg), encoding="utf-8")

if __name__ == "__main__":
    target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    scaffold_workspace(target)
