# Layer 3 Reference Schemas: Gauntlet B (Splatbox DOM & CDP Specs)

## 1. Upstream GitHub Repositories
* **CDP Automation**: https://github.com/browser-use/browser-use & https://github.com/browser-use/browser-harness
* **Agent Browser CLI**: https://github.com/vercel-labs/agent-browser
* **Container-to-Host Bridge**: https://github.com/89luca89/distrobox (/usr/bin/distrobox-host-exec)

## 2. Verbatim Splatbox DOM Selectors (https://splatbox.alexdiaz.fyi/)
* Start Button: `button#play` (initially disabled with text "Loading…", becomes enabled when assets load).
* HUD Container: `div#hud` (hidden attribute removed on play).
* Telemetry Nodes: `span#score`, `span#timer` (60 down to 0), `span#accuracy`, `span#weapon-name` (Rifle), `span#ammo` (40), `span#capacity` (/ 40), `div#crosshair`.

## 3. CDP PointerLock Relative Mouse Delta & Shot Dispatch Schema
* **Relative Camera Slew (CDP + PointerLock Canvas Event)**:
  1. `await cdp.send("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": 640, "y": 360, "movementX": dx, "movementY": dy})`
  2. `await cdp.send("Runtime.evaluate", {"expression": f"(document.pointerLockElement || document.querySelector('canvas')).dispatchEvent(new MouseEvent('mousemove', {{movementX: {dx}, movementY: {dy}, bubbles: true}}))"})`
* **Left-Click Fire**:
  `await cdp.send("Input.dispatchMouseEvent", {"type": "mousePressed", "x": 640, "y": 360, "button": "left", "buttons": 1, "clickCount": 1})`
  `await cdp.send("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": 640, "y": 360, "button": "left", "buttons": 0, "clickCount": 1})`
* **Reload (KeyR)**:
  `await cdp.send("Input.dispatchKeyEvent", {"type": "keyDown", "key": "r", "code": "KeyR", "windowsVirtualKeyCode": 82})`
  `await cdp.send("Input.dispatchKeyEvent", {"type": "keyUp", "key": "r", "code": "KeyR", "windowsVirtualKeyCode": 82})`
