# Layer 2: Stage 03-execute Contract (Live 60-Second Closed-Loop Match)

## 1. Inputs (Selective Section Routing)

| Source | File / Location | Section / Lines | Why |
| :--- | :--- | :--- | :--- |
| Stage 1 Receipt | ../01-probe/output/probe_state.json | Lines 1–20 | Verified viewport dimensions |
| Stage 2 Module | ../02-controller/output/vision_tracker.py | Lines 1–55 | Certified target centroid detector |
| Layer 3 Blueprint | ../../references/splatbox_dom_cdp.md | Lines 111–160 | Closed-loop PD mouse delta actuation & telemetry logger |

## 2. Process (Single Job: Execute Match & Pass Contract)

> 1. Read Lines 111–160 of ../../references/splatbox_dom_cdp.md.  
> 2. Write output/run_match.py (under 55 lines) that imports find_nearest_target from ../02-controller/output/vision_tracker.py, attaches to Port 9222 via Playwright CDP, ensures PointerLock is active, and runs a 60-second closed-loop control cycle:  
   * Capture viewport JPEG buffer via CDP Page.captureScreenshot.  
   * Compute (dx, dy) via find_nearest_target.  
   * Dispatch relative mouse movement via CDP Input.dispatchMouseEvent (type: "mouseMoved", movementX, movementY).  
   * When hypot(ex, ey) <= 8.5, fire via mousePressed/mouseReleased and reload (r) periodically.  
   * Write final DOM #score, duration_sec, frames_processed, and embeddinggemma2_verified to output/telemetry.json.  
> 3. Execute python3 output/run_match.py and run bash ../../contract.sh.

## 3. Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Match Runner | output/run_match.py | Python (under 55 lines) |
| Final Telemetry | output/telemetry.json | JSON (score, duration_sec, frames_processed, embeddinggemma2_verified) |

## 4. Checkpoints & Audits

Run: bash ../../contract.sh
