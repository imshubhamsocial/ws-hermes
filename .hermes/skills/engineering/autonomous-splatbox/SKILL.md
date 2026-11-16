---
name: autonomous-splatbox
description: "Workflow for executing Gauntlet B Splatbox gameplay tests."
---

# Autonomous Splatbox Execution Protocol

This skill governs the discovery, setup, and execution of autonomous Splatbox agents (e.g., `splatbox_agent`, `gauntlet_b`). It ensures correct path resolution and environment preparation before attempting execution.

## Procedure: Agent Discovery and Execution
1. **Identify Target:** Determine the specific agent script required for the task (e.g., "Gauntlet B", "Splatbox 3D").
2. **Locate Script:** Use `search_files` or `find` commands to locate the absolute path of the target Python script within the workspace.
    *   **Pitfall**: Do not assume the script's location based on its name. The execution environment may require an absolute path relative to the root, or it may be nested in a specific benchmark directory.
3. **Verify Environment:** Check for required dependencies and virtual environments (e.g., `.venv`). If present, use `terminal` with `source <path_to_venv>/bin/activate`.
4. **Execute Agent:** Run the script using the absolute path: `python3 <absolute_script_path>`.
5. **Monitor Output:** Observe the terminal output for execution status (Exit Code 0 = Success).

## Pitfalls and Constraints
*   **Path Resolution**: Execution failures often stem from incorrect relative paths. Always verify the exact location using `find` before attempting to run.
*   **Environment State**: Ensure any required virtual environments are activated or that all dependencies are installed in the active environment.
*   **Verification**: Never declare success based on intent; wait for a non-zero exit code or a valid verification receipt (`/tmp/hermes_verified_script.json`).