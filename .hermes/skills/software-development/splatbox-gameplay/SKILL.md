---
name: splatbox-gameplay
description: "Workflow for CDP connection and Splatbox gameplay."
---
# Splatbox Gameplay Workflow (Gauntlet B)

## ⚙️ Procedure
1. **Launch Browser**: Use `distrobox-host-exec` to launch Chrome Dev with remote debugging on Port 9222, ensuring the user data directory is set to `$HOME/.cache/chrome_dev_debug`.
2. **CDP Polling**: Robustly poll `http://127.0.0.1:9222/json` using `terminal` with `curl` and `jq` until the `webSocketDebuggerUrl` for `splatbox.alexdiaz.fyi` is retrieved.
3. **Navigation & Readiness**: Navigate to the URL and poll the DOM until `button#play` is enabled (text "Practice").
4. **Engagement**: Click `button#play` via `browser_exec` and wait for game initialization.
5. **Verification**: Verify HUD visibility (`div#hud`) and PointerLock activation via `browser_exec` after engagement.
6. **Gameplay Loop**: Enter the loop: Capture viewport frame (CDP), visually analyze rules/HUD using selectors (`span#score`, `span#timer`, `span#ammo`), synthesize controller logic (`splatbox_agent.py`), execute for 60s, extract telemetry to `output/telemetry.json`, and verify contract via `bash contract.sh` (exit code 0).

## ⚠️ Pitfalls
* **CDP Polling Fragility**: Do NOT attempt CDP polling using `execute_code` with Python loops; the kernel environment is prone to `SyntaxError` in complex loops. Use `terminal` with `curl` and `jq` for robust, shell-native polling.
* **State Check**: Initial game state (HUD hidden, PointerLock inactive) is expected immediately after clicking 'Play'; wait for the game to transition to the active state before proceeding to visual analysis.