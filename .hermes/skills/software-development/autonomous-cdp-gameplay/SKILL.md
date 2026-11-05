---
name: autonomous-cdp-gameplay
description: "Execute CDP rounds for web games and verify contracts."
---
# Autonomous CDP Gameplay Workflow

## Procedure
1. **Resolve CDP URL:** Call `get_websocket_url()` to dynamically fetch the WebSocket URL and Page ID from the CDP HTTP endpoint.
2. **Connect:** Establish a WebSocket connection to the resolved URL.
3. **Pre-Check:** Verify the play button visibility using `Runtime.evaluate` on the page ID.
4. **Engage PointerLock:**
    a. Call `Page.bringToFront` to ensure tab focus.
    b. Query `#play` bounds using `Runtime.evaluate` to calculate dynamic center coordinates (x + width/2, y + height/2).
    c. Dispatch `Input.dispatchMouseEvent` (mousePressed then mouseReleased) to the calculated center.
5. **Run Round:** Execute the round loop (e.g., 60s), capturing screenshots via `Page.captureScreenshot`.
6. **Extract Telemetry:** Use `Runtime.evaluate` on specific DOM selectors (`span#score`, `span#timer`, `span#ammo`) to extract real-time metrics.
7. **Seal Telemetry:** Write metrics to `output/telemetry.json`.
8. **Verify Contract:** Execute `bash contract.sh` and confirm exit code 0.

## Pitfalls
* **Do NOT** use the conversational `browser_exec` tool; use the standalone `output/splatbox_agent.py` runner for reliable CDP control.
* **Always** resolve the WebSocket URL and Page ID dynamically; never hardcode coordinates or URLs.
* **Unpack** `Runtime.evaluate` responses using the full nested path: `response['result']['result']['value']`.
* **Ensure** the output directory (`output/`) exists and is writable before writing `output/telemetry.json` to prevent contract failure (exit code 1).