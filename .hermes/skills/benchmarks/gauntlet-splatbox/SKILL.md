---
name: gauntlet-splatbox
description: "Workflow for executing Gauntlet B (Splatbox 3D CV) missions."
---

# Gauntlet Splatbox

## Mission Procedure
1. **Browser Initialization**: Execute `launch_chrome.sh` to start the required remote debugging environment (CDP port 9222).
2. **Agent Execution**: Run the agent script (`run_agent.sh`) within the active benchmark directory.
3. **Timeout Management**: Set a generous timeout (e.g., 1200 seconds) for the execution phase to allow for complex 3D simulation and AI reflex loops.
4. **Verification Phase**: After the process terminates, perform an explicit file system audit of the working directory.

## Pitfalls & Lessons
* **Exit Code Insufficiency**: A successful exit code (Exit Code 0) from the execution script is not sufficient confirmation of mission success. The agent must verify the existence of the `check.md` receipt and recorded MP4 video frames before declaring a pass.
* **OpenCV Bounding Box Error**: If `cv2.boundingRect(cnt)` leads to a `TypeError: 'int' object is not subscriptable` when accessing dimensions, verify that the unpacking correctly maps the 4-tuple result `(x, y, width, height)` to variables, ensuring height is accessed via index 3.
* **OpenCV ArcLength Error**: If `cv2.arcLength` fails with a missing argument error, explicitly pass `closed=True` as the second argument: `cv2.arcLength(cnt, True)`.

## References
- `splatbox_cdp_protocol` (references/splatbox_cdp.md)
