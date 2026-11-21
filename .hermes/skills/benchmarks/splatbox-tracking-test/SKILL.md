---
name: splatbox-tracking-test
description: "Test Splatbox weapon tracking and agent logic."
tags: [gauntlet-b, tracking, cv]
related_skills: []
---

# Splatbox Tracking Test

## Mission Procedure
1. **Browser Initialization**: Execute `launch_chrome.sh`; ensure the remote debugging environment is active via CDP port 9223.
2. **Weapon Calibration**: Run the calibration script (`python` followed by exact path to `calibrate_weapons`). This generates `gun_stats/json`. The agent must ingest this data for distance-based targeting and drop compensation across all weapons (pistol, rifle).
3. **Agent Execution**: Execute the primary agent logic (`splatbox_agent`) within the active benchmark stage environment.
4. **Verification Phase**: Audit the working directory for `check.md` to confirm mission completion and data integrity.

## Pitfalls & Lessons
* **Script Path Resolution**: Verify the exact relative path casing of all stage scripts (e.g., `/stages/02-Controls/output/...`). Inconsistent naming is a primary cause of execution failures.
* **Data Integration**: The agent logic must explicitly load and utilize the generated `gun_stats` data to achieve compensated shooting behavior.

## References
- `splatbox_vision_schemas` (./references/splatbox.md)