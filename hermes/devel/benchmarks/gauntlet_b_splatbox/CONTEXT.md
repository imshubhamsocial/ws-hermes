# Gauntlet B - Splatbox 3D Paintball CV Targeting Testbed

One job: Execute autonomous Splatbox gameplay via 3-stage compiler pipeline on CDP Port 9222.

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| System Invariants | `../../_config/invariants.md` | Network Ports | CDP Port 9222 connection |
| Vision Schemas | `../../shared/vision_schemas.md` | Vision Invariants | Centroid detection math |

## Process

> 1. Execute Stage 1: Browser and canvas state probing (stages/01-probe/).
> 2. Execute Stage 2: CPU OpenCV HoughCircles centroid calculation (stages/02-controller/).
> 3. Execute Stage 3: CDP action dispatch and frame telemetry capture (stages/03-execute/).
> 4. Verify telemetry.json records >= 100 frames and score >= 1.

## Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Telemetry | output/telemetry.json | Execution metrics JSON |
| Audit Receipt | output/check.md | YAML-frontmattered receipt |

## Check

Run bash ./contract.sh and confirm 145 frames captured, score = 1, and exit code 0.
