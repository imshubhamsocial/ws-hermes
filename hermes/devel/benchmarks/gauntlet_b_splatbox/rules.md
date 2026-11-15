# Procedural Rules: Gauntlet B — Dual-Launch Splatbox Benchmark

> 1. **Prompt Contract (Zero Spoon-Feeding)**:
>    * Prompts must follow user conversational style.
>    * Never provide hardcoded pixel coordinates, bounding box areas, or specific numeric offsets.
>    * Prompt instructs Hermes to analyze shooting angles, weapon distances (pistol, rifle, shotgun), and fix vision tracking and ballistics.
> 2. **Stage 1 — Remediation & Weapon Analysis Run**:
>    * Launch host Konsole running Hermes TUI (`hermes chat --in <BENCH> -m <model> --skills icm-architect --accept-hooks --tui --yolo -q <prompt>`).
>    * Launch native KDE dummy placeholder on right screen (`placeholder.py`).
>    * Record Konsole window on left (frame, titlebar, shadows) for Stage 1 duration.
> 3. **Stage 2 — Autonomous Execution Run**:
>    * Launch fresh Konsole running Hermes TUI instructing execution of `python3 output/splatbox_agent.py`.
>    * Record Konsole window on left executing command and verifying telemetry.
> 4. **Stage 3 — WebGPU Game Play & Window Capture**:
>    * Launch Google Chrome on Intel iGPU (`DRI_PRIME=0`, `__NV_PRIME_RENDER_OFFLOAD=0`, `__GLX_VENDOR_LIBRARY_NAME=mesa`) on port 9222.
>    * Record Chrome window with full Breeze titlebar, tabs, canvas, and shadows playing `https://splatbox.alexdiaz.fyi/?autoplay`.
>    * Splatbox agent writes match telemetry to `stages/03-execute/output/telemetry.json` (score >= 25, frames >= 120).
> 5. **Stage 4 — Deterministic Composition**:
>    * Composite left stream (Hermes Run 1 followed by Hermes Run 2) side-by-side with right stream (KDE placeholder during Run 1, Chrome WebGPU game during Run 2).
>    * Output master benchmark video to `output/<model_video>.mp4`.
> 6. **Hardware & Substrate Cleanliness**:
>    * Stop all test processes before and after each benchmark run.
>    * Zero residual processes, temporary profiles, or background subshells.
>    * Never modify `/var/home/imshubhamsocial/.hermes/hermes-agent`.
