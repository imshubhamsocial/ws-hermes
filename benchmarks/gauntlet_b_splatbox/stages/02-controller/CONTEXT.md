# Layer 2: Stage 02-controller Contract (Closed-Loop Vision & Semantic Verifier)

## 1. Inputs (Selective Section Routing)

| Source | File / Location | Section / Lines | Why |
| :--- | :--- | :--- | :--- |
| Stage 1 Frame | ../01-probe/output/playing_frame.png | Full image | Real captured frame for offline target detection tuning |
| Stage 1 Receipt | ../01-probe/output/probe_state.json | Lines 1–20 | Viewport center coordinates (cx, cy) |
| Layer 3 Blueprint | ../../references/splatbox_dom_cdp.md | Lines 51–110 | OpenCV centroid tracker & embeddinggemma-2 verification blueprint |

## 2. Process (Single Job: Build & Verify Vision Tracker Module)

> 1. Read ../01-probe/output/probe_state.json and Lines 51–110 of ../../references/splatbox_dom_cdp.md.  
> 2. Write output/vision_tracker.py (under 55 lines) implementing:  
   * find_nearest_target(bgr_frame, cx, cy) using OpenCV cv2.HoughCircles to return (tx, ty, r, dx, dy) for the bullseye target closest to crosshair (cx, cy).  
   * verify_crop_semantic(crop_bgr) querying Port 8139 (embeddinggemma-2) or fallback colour-ring check to confirm the crop is an active target.  
> 3. Run python3 output/vision_tracker.py ../01-probe/output/playing_frame.png to generate output/target_detected.png, output/target_crop.png, and output/tracker_verified.json.

## 3. Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Vision Module | output/vision_tracker.py | Python module (under 55 lines) |
| Overlay Receipt | output/target_detected.png | Annotated PNG |
| Tracker Receipt | output/tracker_verified.json | JSON (targets_found_ge_1, dx, dy, embeddinggemma2_verified) |

## 4. Checkpoints & Audits

Run: jq -e '.targets_found_ge_1 == true and (.dx | type == "number")' output/tracker_verified.json && test -s output/target_detected.png
