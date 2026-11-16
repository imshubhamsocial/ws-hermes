---
name: rule_splatbox_target_acquisition_optimization
description: Optimizes target acquisition speed and refines error tolerance for Gauntlet B splatbox contracts.
context: Gauntlet B requires reliable bullseye hits. Current PD loop tracking is stable but target acquisition is too slow, leading to missed shots and a score of 0.
invariants:
  - Increase horizontal sweep speed (movementX) from +25 to +35 to accelerate target acquisition across the arena width.
  - Refine the error tolerance check: The maximum acceptable error hypotenuse should be dynamically scaled based on the target radius R_px to ensure smaller, high-value targets are prioritized over large, low-value splats.
examples:
  - Implementation requires modifying output/splatbox_agent.py and re-running contract.sh.
---