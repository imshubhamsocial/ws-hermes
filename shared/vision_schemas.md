# Shared Reference: Vision and Centroid Schemas (Gauntlet B)

## Vision Invariants
- Target Canvas: `#gameCanvas` at 1280x720 CSS pixels.
- High-DPI Scale Ratio: `canvas.width / rect.width` and `canvas.height / rect.height`.
- Aiming Algorithm: OpenCV CPU `cv2.HoughCircles` detection (dp=1.2, minDist=30, param1=50, param2=30).
- Latency Constraint: < 5 ms frame latency on CPU (0 MiB GPU VRAM).
- Precision Constraint: < 5 px aiming error relative to target center.
- Telemetry Schema: JSON with `frames_captured`, `score`, `elapsed_s`, and `vram_mib`.
