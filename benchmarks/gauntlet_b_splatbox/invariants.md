# Hard Invariants: Gauntlet B — Autonomous Splatbox Browser Gameplay

> 1. **Zero Bespoke Code in Upstream**: All agent controller logic MUST live in output/splatbox_agent.py.
> 2. **Shared Debug Profile**: Chrome Dev data dir MUST reside in $HOME/.cache/chrome_dev_debug across container-host boundary.
> 3. **PointerLock Delta Dispatch**: Camera movements MUST use relative deltas (movementX, movementY) with proportional gain Kp=0.65 via CDP Input.dispatchMouseEvent and Runtime.evaluate.
> 4. **Ballistic Gravity Drop Formula**: Target elevation MUST apply vertical drop compensation clip(380.0 / max(R_px^2, 25), 1.0, 28.0) px.
> 5. **Trigger Discipline**: Never fire unless radial error sqrt(ex^2 + ey^2) <= 6.0 px and ammo > 0. Auto-reload when ammo <= 5.
> 6. **VRAM Invariant**: Total GPU VRAM on RTX 3050 must remain <= 5,800.0 MiB (embeddinggemma2 runs on CPU Port 8139).
