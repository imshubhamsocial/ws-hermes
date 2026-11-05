---
name: splatbox-cdp-gameplay
description: "Automates Splatbox gameplay using CDP on host Chrome Dev."
---
# Procedure: Splatbox CDP Gameplay Pipeline

1. **Setup Host Browser**: Use `terminal` to launch the host Chrome Dev instance on CDP Port 9222, ensuring the user-data-dir is correctly set in `$HOME/.cache/chrome_dev_debug`.
2. **Wait for Readiness**: Poll `http://127.0.0.1:9222/json` until the `webSocketDebuggerUrl` for `https://splatbox.alexdiaz.fyi/` is found.
3. **Engage Game**: Poll DOM via `execute_code` (using `Runtime.evaluate`) until `#play` is enabled, then execute the click. Verify HUD activation (`#hud` not hidden).
4. **Gameplay Loop**: Execute `execute_code` loop:
    a. Capture frame via CDP (`Page.captureScreenshot`).
    b. Query vision/Gemma (Port 8139) for target bullseyes and HUD state.
    c. Calculate vertical drop compensation using the formula from `invariants.md`.
    d. Slew camera using relative deltas (Kp=0.65) via CDP `Input.dispatchMouseEvent`.
    e. Fire only if radial error $\le 6.0$ px and ammo $> 0$.
    f. Auto-reload if ammo $\le 5$ using CDP `Input.dispatchKeyEvent` (KeyR).
5. **Finalize**: Record metrics to `output/telemetry.json` and execute `bash contract.sh` until exit code 0.

# Pitfalls
* **CDP Parsing**: Always wrap CDP responses in robust JSON parsing logic (e.g., check if the response is a list or a dictionary) to prevent `AttributeError` when the endpoint returns an array of results instead of a single object.
* **Tool Isolation**: All agent controller logic MUST reside in `output/splatbox_agent.py` and never in bespoke wrapper scripts.
* **VRAM Gate**: Monitor GPU VRAM (RTX 3050 $\le 5,800.0$ MiB) to ensure CPU-based embeddings (Port 8139) do not exceed the limit.
