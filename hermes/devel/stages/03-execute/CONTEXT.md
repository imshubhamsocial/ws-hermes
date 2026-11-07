# 03-execute - CDP Action Dispatch and Frame Telemetry

One job: Dispatch normalized mouse clicks via Playwright CDP and record output/telemetry.json.

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| Stage 2 Output | ../02-controller/output/aim_controller.py | Centroid function | Target coordinates |
| System Invariants | `../../_config/invariants.md` | Section 2: Network Ports | CDP Port 9222 attachment |
| Vision Schemas | `../../shared/vision_schemas.md` | Telemetry Schema | Frame count & score keys |

Do NOT load: ../01-probe/CONTEXT.md or ../../benchmarks/gauntlet_a_voxel_fps/.

## Process

> 1. Attach to Chromium on Port 9222 via Playwright connect_over_cdp("http://127.0.0.1:9222").
> 2. Execute the aiming loop using ../02-controller/output/aim_controller.py across >= 100 frames.
> 3. Dispatch normalized mouse click actions to #gameCanvas.
> 4. Save execution metrics (frames_captured, score, elapsed_s, vram_mib) to output/telemetry.json.

## Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Execution Telemetry | output/telemetry.json | JSON receipt (frames >= 100, score >= 1) |
| Stage Audit Receipt | output/check.md | YAML-frontmattered Markdown |

## Check

Run bash ../../benchmarks/gauntlet_b_splatbox/contract.sh and confirm 145 frames captured, score = 1, exit 0.
