# 02-controller - CPU OpenCV HoughCircles Aiming Controller

One job: Compute target centroids on CPU from probe metadata and write output/aim_controller.py.

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| Stage 1 Output | ../01-probe/output/probe_state.json | Full JSON file | Canvas bounding rect & DPI ratio |
| System Invariants | ../../_config/invariants.md | Section 1: CPU Vision Offload | Enforce 0 MiB GPU VRAM & <5 ms |
| Vision Schemas | ../../shared/vision_schemas.md | HoughCircles Parameters | Coordinate scaling math |

Do NOT load: ../03-execute/, ../../benchmarks/, or ../../phases/.

## Process

> 1. Read ../01-probe/output/probe_state.json and verify width and height keys exist.
> 2. Calculate CSS-to-canvas coordinate scale ratio (canvas.width / rect.width).
> 3. Implement OpenCV cv2.HoughCircles centroid detection on CPU (0 MiB GPU VRAM, < 5 ms execution).
> 4. Write the modular controller (<60 lines) to output/aim_controller.py.

## Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Aiming Controller | output/aim_controller.py | Python 3 module (<60 lines) |
| Stage Audit Receipt | output/check.md | YAML-frontmattered Markdown |

## Check

Run python3 -m py_compile output/aim_controller.py and verify < 5 ms CPU centroid latency and < 5 px error.
