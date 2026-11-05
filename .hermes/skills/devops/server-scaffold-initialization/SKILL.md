---
name: server-scaffold-initialization
description: "Build a Node.js server scaffold and stub-free core."
---

## Overview
This skill automates the initial setup of a backend server project, following a strict, sequential engineering process to ensure correctness and verifiability, adhering to the user's requirement for a complete implementation over a stub.

## Procedure
1. **Analyze Requirements (Stage 1):**
    - Read `CONTEXT.md`, `invariants.md`, `rules.md`, and `references.md` to define project constraints.
    - Document the expected output structure and wire protocol in a temporary specification.

2. **Establish Workspace:**
    - Create all necessary directories (e.g., `output/voxel-paintball-app/server`, `output/voxel-paintball-app/client/js/engine`, etc.).

3. **Manage Dependencies:**
    - Write `package.json` including all required dependencies (e.g., `express`, `ws`, `three`).
    - Run `npm install --prefix <project-path> --silent` to install dependencies and keep output compact.

4. **Implement Core Logic (Stub-Free):**
    - Write the full `server.js` implementation.
    - Ensure the code is complete, handles all specified packets (`JOIN_ROOM`, `INPUT`, `SHOOT`, `STATE_SNAPSHOT`, `SPLAT`), and contains the required physics simulation (e.g., $g = -24.0 \text{ m/s}^2$).
    - Define and implement the core game loop (e.g., 20 Hz tick loop).

5. **Finalize and Handoff:**
    - Generate and write the Stage 1 handoff receipt (e.g., `output/stage1_spec_receipt.json`).
    - Explicitly state completion and stop the workflow.

## Pitfalls and Lessons
*   **Stale Write Block:** Before using `write_file` on any existing file, always perform a preceding `read_file` operation to ensure the disk content is current. Attempting to write to an unknown or unread file results in a write refusal.
*   **Tool Idempotency:** When using `search_files` or `read_file` multiple times, monitor the response for identical, repeated results (tool loop warning). Use the first valid result or change the query/tool.
*   **Scope:** Do not include client Three.js file implementations in this stage; keep active context focused strictly on server and infrastructure setup.

## References
- [None currently applicable. Add recipe for physics simulation or specific packet structure here when applicable.]