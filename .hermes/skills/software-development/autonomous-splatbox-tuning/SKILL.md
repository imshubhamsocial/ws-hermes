---
name: autonomous-splatbox-tuning
description: "Tune Gauntlet B PD loops for max stability and hits."
---
## Always-On Rules (Tuning Discipline)
* When a Splatbox agent fails to reach the target score threshold, treat the PD loop stability as the primary hypothesis, not the target visibility.
* Never attempt to fix a PD loop (aiming) without first ensuring the firing threshold is sufficiently relaxed to avoid oscillation on target acquisition.
* All tuning modifications (PID coefficients, thresholds) must be recorded as a reference for future runs to prevent re-discovery of dead ends.

## Procedure: PD Loop Stabilization & Tuning
1. **Initial Validation**: Execute the agent and check `stages/03-execute/output/telemetry.json`.
2. **Check Threshold**: If Score is 0 and frames are high, the firing threshold is likely too low, causing PD oscillation.
   * **Action**: Increase the minimum firing threshold ($\text{hypot}(e_x, e_y) \le \max(25.0, 0.45 \times R_{\text{px}})$).
3. **Check Aiming Stability**: If hits are sporadic despite a relaxed threshold, the PD controller gains are likely too aggressive or too passive.
   * **Action**: Perform surgical tuning on the horizontal PD parameters:
     * Increase Horizontal Proportional Gain ($0.45 \to 0.5$).
     * Decrease Derivative Gain ($0.12 \to 0.1$).
4. **Final Validation**: Re-execute the full 58-second loop and verify score and frame count against contract.

## Pitfalls
* **Oscillation Risk**: Increasing the threshold is a blunt instrument; ensure it is still below the maximum possible bullseye radius to maintain effective aiming range.
* **Tuning Lock-in**: Once successful parameters are found, they must be committed to a reference file; do not rely on trial-and-error in subsequent sessions.

## References
* [Splatbox Ballistic Parameters](#splatbox-ballistic-parameters)