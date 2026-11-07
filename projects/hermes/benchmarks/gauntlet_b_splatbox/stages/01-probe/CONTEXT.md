# Layer 2: Stage 01-probe Contract (DOM & PointerLock Activation)

## 1. Inputs (Selective Section Routing)

| Source | File / Location | Section / Lines | Why |
| :--- | :--- | :--- | :--- |
| Layer 0 DNS | ../../../../IDENTITY.md | Lines 1–20 | Verify CDP Port 9222 endpoint |
| Layer 3 Blueprint | ../../references/splatbox_dom_cdp.md | Lines 1–50 | Playwright CDP attach & trusted native click blueprint |

## 2. Process (Single Job: Probe & Engage PointerLock)

> 1. Read Lines 1–50 of ../../references/splatbox_dom_cdp.md.  
> 2. Write a compact Python script output/probe.py (under 45 lines) using playwright.sync_api (connect_over_cdp("http://127.0.0.1:9222")) to:  
   * Locate the tab whose URL contains splatbox.alexdiaz.fyi and call page.bring_to_front().  
   * Save an initial menu screenshot to output/menu_frame.png.  
   * If #play is visible, click it via page.locator("#play").click() (which dispatches a trusted CDP mouse gesture) and wait 500 ms.  
   * Evaluate document.pointerLockElement !== null and extract HUD selectors (#score, #timer, #ammo).  
   * Save an in-game screenshot to output/playing_frame.png and write output/probe_state.json.  
> 3. Execute python3 output/probe.py via the terminal tool.

## 3. Outputs

| Artifact | Location | Format |
| :--- | :--- | :--- |
| Probe Script | output/probe.py | Python (under 45 lines) |
| In-Game Frame | output/playing_frame.png | PNG (1280x720) |
| Probe Receipt | output/probe_state.json | JSON (pointer_lock_active, viewport, hud) |

## 4. Checkpoints & Audits

Run: jq -e '.pointer_lock_active == true and .viewport.width > 0' output/probe_state.json && test -s output/playing_frame.png
