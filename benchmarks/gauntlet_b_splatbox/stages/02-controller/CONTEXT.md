# Layer 2: Stage 02-controller Contract (Closed-Loop Vision & Gun Calibration)

## 1. Inputs (Selective Section Routing)

| Source | File / Location | Section / Lines | Why |
| :--- | :--- | :--- | :--- |
| Benchmark Map | ../../AGENTS.md | Lines 1–27 | Benchmark operating protocol |
| Stage 1 Frame | ../01-probe/output/playing_frame.png | Full image | Target detection frame |
| Stage 1 Receipt | ../01-probe/output/probe_state.json | Lines 1–20 | Viewport center coordinates (cx, cy) |
| Gun Blueprint | ../../references/splatbox_dom_cdp.md | Lines 35–84 | Live weapon switching and ballistics |

## 2. Process (Single Job: Calibrate Weapons & Verify Occlusion Filtering)

> 1. Update `output/vision_tracker.py` to filter out targets completely blocked by walls, prioritizing visible ones.  
> 2. Run `python3 output/calibrate_weapons.py` over CDP (Port 9222) to probe live weapon characteristics (pistol, rifle, shotgun) and write `output/gun_stats.json`.  
> 3. Verify `jq -e '.rifle.drop_offset_px != null' output/gun_stats.json`.

## 3. Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Vision Module | output/vision_tracker.py | Python module (< 60 lines) |
| Calibration Script | output/calibrate_weapons.py | Python script (< 60 lines) |
| Calibrated Stats | output/gun_stats.json | JSON (effective_range, drop_offset, ammo) |
| Tracker Receipt | output/tracker_verified.json | JSON (targets_found_ge_1, dx, dy) |

## 4. Checkpoints & Audits

Run: jq -e '.rifle.drop_offset_px != null and .pistol.effective_range_px != null' output/gun_stats.json