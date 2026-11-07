# Document 01: Forensic Benchmark Failure Audit, Error Transcripts, and Raw Logs Catalog

> **Scope**: Root-Cause Forensic Dissection of Gauntlet B (Splatbox CDP) and Master Raw Logs Catalog for `hermes-tests`  
> **Substrate Target**: Hermes Agent OS on Fedora Kinoite 44 (`chrome-dev-cdp.service` on Port 9222)  
> **Evaluation Repository**: [`https://github.com/imshubhamsocial/hermes-tests`](https://github.com/imshubhamsocial/hermes-tests)  

---

## 1. Executive Summary of the Gauntlet B Failure Loop

During Gauntlet B execution on `https://splatbox.alexdiaz.fyi/`, Hermes was trapped in a recurring multi-turn failure loop. Rather than achieving live, verified 60-second autonomous gameplay, the agent spent 12+ conversational turns and over 50,000 tokens struggling to generate and patch a monolithic Python script (`output/splatbox_agent.py`, 6,276 bytes).

The underlying pathology was **not a lack of raw coding ability**, but a profound architectural failure in **meta-prompting, task decomposition, and substrate selection**.

---

## 2. Forensic Error Transcripts & Protocol Traps

### 2.1 Error 1: Array Parsing KeyError on `/json` Endpoint
- **Symptoms**:
  ```python
  TypeError: list indices must be integers or slices, not str
  # Or KeyError: 'webSocketDebuggerUrl' when treating http://127.0.0.1:9222/json as a dict
  ```
- **Forensic Diagnosis**: Chrome DevTools Protocol HTTP endpoint `http://127.0.0.1:9222/json` returns a JSON **array of dictionaries**, one per active tab/target. Initial script logic attempted `data['webSocketDebuggerUrl']` instead of iterating over tabs and matching `splatbox` in `tab.get('url', '')`.

### 2.2 Error 2: KeyError 0 on `Target.getTargets`
- **Symptoms**:
  ```python
  targets = json.loads(response)
  target_id = targets['result'][0]['targetId']
  # Throws: KeyError: 0
  ```
- **Forensic Diagnosis**:
  In Chrome DevTools Protocol, the response payload for `Target.getTargets` is structured as:
  ```json
  {
    "id": 1,
    "result": {
      "targetInfos": [
        {"targetId": "F08B24B9E644B1A6...", "type": "page", "title": "Splatbox...", ...}
      ]
    }
  }
  ```
  `targets['result']` is a **dictionary**, not a list. The list is located at `targets['result']['targetInfos']`. Attempting index `[0]` immediately threw `KeyError: 0`.

### 2.3 Error 3: Chromium PointerLock Security Violation
- **Symptoms**:
  Synthetic JavaScript execution via `Runtime.evaluate`:
  ```javascript
  document.querySelector('#play').click();
  ```
  Returned `undefined`, and evaluation of `document.pointerLockElement` returned `null`. Chrome console logged:
  `error: A user gesture is required to request Pointer Lock.`
- **Forensic Diagnosis**:
  Chromium enforces a strict security invariant for PointerLock (and fullscreen): PointerLock can **only** be granted during the execution of a trusted, native user-gesture event (e.g., an actual hardware mouse or key event). Synthetic DOM events created via script (`element.click()` or `dispatchEvent(new MouseEvent(...))`) have `isTrusted == false` and are explicitly rejected by the browser security sandbox.
- **The Correct Architectural Path**:
  The agent must call CDP `Page.bringToFront` to ensure the tab is active and focused, dynamically resolve the element's client bounding rect (`getBoundingClientRect()`), compute the screen coordinates, and issue **native CDP mouse events** via `Input.dispatchMouseEvent` (`mousePressed` with `buttons: 1`, followed by `mouseReleased` with `buttons: 0`).

### 2.4 Error 4: CDP Nested Evaluation Return Schema
- **Symptoms**:
  ```python
  response = await websocket.recv()
  bounds = json.loads(response)['result']['value']
  # Throws: KeyError: 'value'
  ```
- **Forensic Diagnosis**:
  In CDP `Runtime.evaluate`, successful execution wraps the evaluated result twice:
  ```json
  {
    "id": 4,
    "result": {
      "result": {
        "type": "object",
        "value": { "left": 540, "top": 320, "width": 200, "height": 60 }
      }
    }
  }
  ```
  Unpacking `response['result']['value']` fails because the outer object has key `'result'`, and inside it lies another `'result'` object containing `'value'`. Furthermore, if `returnByValue: true` is not explicitly passed in the params, CDP returns an object handle (`objectId`) without serializing the dictionary values, yielding `KeyError: 'value'`.

### 2.5 Error 5: Execution Context ID vs Target ID Confusion
- **Symptoms**:
  ```python
  bounds_script = "document.querySelector('#play').getBoundingClientRect()"
  await websocket.send(json.dumps({"id": 4, "method": "Runtime.evaluate", "params": {"expression": bounds_script, "contextId": page_id}}))
  # Throws: NameError: name 'page_id' is not defined
  # Or CDP Error: {"code": -32602, "message": "Invalid parameters: contextId: integer value expected"}
  ```
- **Forensic Diagnosis**:
  When Hermes connected directly to the page WebSocket (`ws://127.0.0.1:9222/devtools/page/<GUID>`), commands operate directly on that page. It does not require a `contextId`.
  When Hermes tried to supply `page_id` (the 32-character hex GUID from the URL), CDP rejected it because in CDP, `contextId` is an integer execution context ID (e.g. `1`), NOT a target GUID. Omitting `contextId` entirely evaluates directly in the page's default execution context.

### 2.6 Error 6: Python Linter & Patching Desynchronization
- **Symptoms**:
  ```python
  SyntaxError: expected 'except' or 'finally' block (line 138, column 0)
  ```
- **Forensic Diagnosis**:
  Because Hermes attempted to write a 150-line async Python script containing nested `try/async with/while/with` blocks in a single tool call, line-based fuzzy patching frequently introduced desynchronized indentation. When Hermes attempted to overwrite the entire file with `write_file`, the 4B parameter model suffered attention drift near the bottom of the file, dropping the closing `except` block for the outer `try:` at line 49.

---

## 3. Why the "Monolithic Script" Prompt Approach Failed

The root cause of all 6 errors above lies in **how the prompt was formulated**:

1. **Monolithic Task Overload**:
   The prompt commanded:
   > "Connect over CDP Port 9222, wait for button#play to become enabled, click it to enter PointerLockControls gameplay, and execute a closed-loop autonomous player (output/splatbox_agent.py) that combines our local embeddinggemma2 multimodal vision substrate (Port 8139 / vision_tools.py) for visual target/HUD verification with OpenCV HoughCircles centroid tracking, ballistic gravity drop compensation (clip(380.0 / max(R_px^2, 25), 1.0, 28.0) px), proportional gain Kp=0.65 relative mouse deltas (movementX, movementY), and strict <= 6.0 px trigger discipline. Record the completed round metrics (#score, #timer, #accuracy, embeddinggemma2_verified) to output/telemetry.json and run bash ./contract.sh."

2. **Inversion of the Agentic Discovery Loop**:
   Instead of instructing Hermes to:
   - Step 1: Open the browser and visually inspect the page.
   - Step 2: Use developer tools to verify the button and click behavior.
   - Step 3: Implement minimal modular primitives.
   The prompt demanded that Hermes invent, debug, and certify an entire production game-playing engine from scratch in a single file before even testing if a click worked!

3. **Tool Blindness Induced by Prescriptive Prompts**:
   Because the prompt was packed with prescriptive code formulas, Hermes treated the task as a **coding exam** rather than an **agentic task**. It never searched the web for CDP documentation, never checked its built-in browser skills, and never wrote 2-line test scripts to verify assumptions.

---

## 4. Master Raw Benchmark Logs Catalog for `hermes-tests`

The following raw benchmark execution logs, traces, and artifacts are preserved in the workspace and ready for synchronization to [`https://github.com/imshubhamsocial/hermes-tests`](https://github.com/imshubhamsocial/hermes-tests):

### 4.1 Gauntlet B (Splatbox CDP) Artifacts (`benchmarks/gauntlet_b_splatbox/output/`)
- [`output/splatbox_agent.py`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox/output/splatbox_agent.py): Full 6,276-byte autonomous CDP controller source code.
- [`output/live_game_screen.png`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox/output/live_game_screen.png): Raw initial screenshot of Splatbox menu modal showing `#play` button ("Practice"), instructions legend (`WASD`, `Click`, `R`, `1-5`).
- [`output/live_game_playing.png`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox/output/live_game_playing.png): Raw live in-game capture showing 3D arena, floating bullseye targets, rifle HUD (`40 / 40`), and crosshair (`+`).
- [`output/after_play_click.png`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox/output/after_play_click.png): Diagnostic capture after initial synthetic click attempt.
- [`output/after_cdp_click.png`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox/output/after_cdp_click.png): Diagnostic capture confirming CDP native mouse event delivery.
- [`output/target_detected.png`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox/output/target_detected.png): OpenCV HoughCircles target detection bounding overlay.
- [`output/target_crop.png`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox/output/target_crop.png): Cropped floating target candidate for vision verification.
- [`benchmarks/gauntlet_b_splatbox/contract.sh`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks/gauntlet_b_splatbox/contract.sh): Verification contract script requiring zero fake green.

### 4.2 Standard Evaluation Logs (`logs/`)
- [`logs/2026-10-26T20-11-48-00-00_tau2-retail_9Eo5qBTpZZmK3vpqnNMATi.eval`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/logs/2026-10-26T20-11-48-00-00_tau2-retail_9Eo5qBTpZZmK3vpqnNMATi.eval) (1.4 MB): Full Inspect AI raw eval run for TAU-2 Retail.
- [`logs/2026-10-26T19-41-48-00-00_tau2-retail_98PCk3vRpww4nuLTGayami.eval`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/logs/2026-10-26T19-41-48-00-00_tau2-retail_98PCk3vRpww4nuLTGayami.eval) (1.5 MB): Second full TAU-2 Retail raw evaluation archive.
- [`logs/2026-10-29T19-29-20-00-00_bfcl_Tg4Fd9NReaWS68xajabotf.eval`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/logs/2026-10-29T19-29-20-00-00_bfcl_Tg4Fd9NReaWS68xajabotf.eval) (22 KB): Berkeley Function-Calling Leaderboard (BFCL) eval run.
- [`logs/2026-10-29T19-34-35-00-00_bfcl_U8GbDDnBKWpxQHH9nPnjpa.eval`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/logs/2026-10-29T19-34-35-00-00_bfcl_U8GbDDnBKWpxQHH9nPnjpa.eval) (15 KB): BFCL second iteration evaluation run.
- [`logs/gaia_custom_tui/`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/logs/gaia_custom_tui/): Full GAIA Level 1/2 benchmark execution logs and transcripts.
- [`logs/inspect_gaia_test/`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/logs/inspect_gaia_test/): Inspect AI automated GAIA harness test outputs.
- [`BENCHMARK_ANALYSIS_REPORT.md`](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/BENCHMARK_ANALYSIS_REPORT.md) (40 KB): Comprehensive analytical report analyzing pass/fail patterns across GAIA, TAU-2, and BFCL.
