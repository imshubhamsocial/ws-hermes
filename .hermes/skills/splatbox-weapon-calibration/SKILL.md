---
name: splatbox-weapon-calibration
description: "Calibrates Splatbox weapons with vision_tracker bug fixes."
---

# Splatbox Weapon Calibration

## Splatbox Weapon Ballistics Calibration Protocol

This skill provides the standardized, tested procedure for executing the closed-loop weapon calibration in the Splatbox 3D CV environment, including necessary fixes for common script errors.

### Procedure:

1.  **Initialize Environment**:
    *   Execute the game launcher to start the isolated Chrome session:
        `./launch_chrome.sh`
2.  **Run Calibration Probe**:
    *   Execute the main calibration script:
        `python3 output/calibrate_weapons.py`
3.  **Validate Output**:
    *   Verify successful completion via the exit code and check the resulting `output/gun_stats.json` for validated parameters (e.g., Effective Range, Drop Offset).

### Critical Pitfalls & Fixes:

*   **Target Detection NameError (Line 35, `output/vision_tracker.py`)**:
    *   **Rule**: Before calling any `cv2.inRange` function that requires a `crop` variable, ensure the `crop` slice is explicitly defined using the bounding box coordinates (`x, y, cw, ch`) of the detected target.
    *   **Why**: The initial script logic failed to define the local variable `crop` within the target detection loop, causing a `NameError`.
    *   **Correction**: Insert `crop = bgr[y:y+ch, x:x+cw]` immediately prior to the color masking call.
*   **Ratio Calculation NameError (Line 37, `output/vision_tracker.py`)**:
    *   **Rule**: When calculating target detection ratios, utilize the pre-calculated bounding box area (`bbox_area`) instead of an undefined variable like `crop_size`.
    *   **Why**: The variable `crop_size` was never initialized in the scope of the target validation logic, leading to a `NameError` during the red-ring contrast check.
    *   **Correction**: Replace `crop_size` with `bbox_area` in the ratio calculation.
*   **Wall Collision Handling**:
    *   **Rule**: If a target is consistently hit against a static geometry, utilize WASD movement within the browser viewport to clear the obstacle and re-trigger the capture.
    *   **Why**: Edge density checks identify high-contrast lines characteristic of geometry, which can skew metrics if the target is partially obscured by a wall.

### Output Schema Reference:

The expected output `output/gun_stats.json` follows this structure:
```json
{
  "pistol": {"effective_range_px": 380, "drop_offset_px": -10.0, "drop_coeff": -0.018, "capacity": 12},
  "rifle": {"effective_range_px": 580, "drop_offset_px": -15.0, "drop_coeff": -0.012, "capacity": 40},
  "shotgun": {"effective_range_px": 190, "drop_offset_px": -5.0, "drop_coeff": -0.028, "capacity": 5},
  "target_dynamics": {"drift_speed_px_s": 42.0, "lead_compensation": true, "reposition_on_wall_hit": true}
}
```