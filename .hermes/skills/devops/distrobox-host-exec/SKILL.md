---
name: distrobox-host-exec
description: "Run host OS commands from inside Distrobox."
---
# Procedure for Host Execution

1.  **Identify Host Task**: Determine if the required action (e.g., launching an application) must run outside the current container environment (`ws-hermes`).
2.  **Verify Executable**: Confirm the correct host execution wrapper is available. The standard executable is `distrobox-host-exec`.
3.  **Execute Command**: Run the desired command using the wrapper.
    *   *Example*: `distrobox-host-exec <command>`
4.  **Manage Process**: Since host applications often run persistently, use `process_manage` to track the background job.
    *   *Command*: `terminal(command="distrobox-host-exec dolphin", background=True)`
    *   *Tracking*: Use the returned `session_id` with `process_manage(action='poll', session_id='...')`.

# Pitfalls

*   **Typographical Error**: The wrapper is `distrobox-host-exec`, not `ditrobox-host-exec`. Failure to use the correct spelling results in exit code 127 (`command not found`).
*   **Environment Scope**: Commands executed via this method run on the host OS, not within the Distrobox container's environment.

# References

## Host Execution Guide
distrobox-host-exec: The wrapper used to execute commands outside the container.
