# Hard Invariants: Gauntlet B — Autonomous Splatbox Browser Gameplay

> 1. **Zero Bespoke Code in Upstream**: All agent controller logic MUST live in output/splatbox_agent.py.
> 2. **Shared Debug Profile**: Chrome Dev data dir MUST reside in $HOME/.cache/chrome_dev_debug across container-host boundary.
> 3. **PointerLock Delta Dispatch**: Camera movements MUST use relative deltas (movementX, movementY) with proportional gain Kp=0.65 via CDP Input.dispatchMouseEvent and Runtime.evaluate.
> 4. **Arena Bullseye Filtering & Ballistic Compensation**: Target detection MUST reject circles outside active wall coordinates (80 < y < 0.70*h, 12 <= r <= 70) AND MUST reject the gun viewmodel zone (x > 0.52*w and y > 0.46*h) to prevent locking onto weapon parts or floor splats. Aiming MUST align directly with zero horizontal offset (dx_offset = 0.0 px) and compensate for empirical ballistic drop (dy_offset = -18.0 px) by aiming 18 px above target centroid.
> 5. **Scan Sweep & Trigger Discipline**: When aligned within effective error hypot(ex, ey) <= max(18.0, 0.50 * R_px), dispatch CDP fire events. When no target is visible, pan camera horizontally (movementX = +25) to acquire the next arena bullseye. Auto-reload (press 'r') every 25 frames.
> 6. **VRAM Invariant**: Total GPU VRAM on RTX 3050 must remain <= 5,800.0 MiB (embeddinggemma2 runs on CPU Port 8139).
