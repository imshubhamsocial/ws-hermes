---
name: gauntlet-b
description: Run Gauntlet B splatbox with 3D ballistic compensation.
---

## Procedure: Autonomous Splatbox Execution (3-Stage ICM Pipeline)

1.  **Initialization**: Start the 3-stage Interpetable Context Methodology (ICM).
2.  **Target Acquisition & Ballistics**:
    *   If a target (`tgt`) exists, apply distance-dependent ballistic correction: `ey = tgt["dy"] - (10.0 + factor)`.
    *   Execute tracking and firing based on calculated trajectory.
3.  **Target Loss Handling**:
    *   If no target is present (`tgt` is None), initiate a horizontal sweep (`movementX: 250`).
    *   Restore camera pitch to horizon level (`movementY: -10`) for continuous scanning.
4.  **Verification**: Record all decoded CDP frames using the `mp4v` code for post-execution analysis.

## Pitfalls & Lessons

*   **Ground Lock Prevention**: The vision tracker must enforce a minimum vertical target threshold (e.g., target `ty > 0.75h`). Allowing targets near the ground causes false centroids, resulting in incorrect downward pitch and agent immobilization.
*   **Ballistic Accuracy**: Always use distance-dependent compensation; static offsets are insufficient for variable ranges.

## References

*   `references/gauntlet_splatbox_ballistics.md`: Detailed breakdown of range factors.
