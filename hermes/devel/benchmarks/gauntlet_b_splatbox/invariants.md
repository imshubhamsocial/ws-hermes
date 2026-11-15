# Hard Invariants: Gauntlet B — Autonomous Splatbox Browser Gameplay

> 1. **Zero Bespoke Code in Upstream**: All agent controller logic MUST live in `output/splatbox_agent.py` and `output/vision_tracker.py`.
> 2. **Shared Debug Profile**: Chrome Dev data dir MUST reside in `/tmp/hermes_chrome_gauntlet` on Intel iGPU with remote debugging port 9222.
> 3. **Hardware Isolation**:
>    * NVIDIA RTX 3050 discrete GPU is strictly dedicated to Hermes LLM inference on port 8138.
>    * Total GPU VRAM usage MUST NOT exceed 5,800.0 MiB at any time.
>    * Google Chrome, Konsole, ffmpeg, and Python scripts MUST run on CPU / Intel Raptor Lake UHD Graphics (iGPU, `DRI_PRIME=0`, `__NV_PRIME_RENDER_OFFLOAD=0`, `__GLX_VENDOR_LIBRARY_NAME=mesa`).
> 4. **Researched Upstream Flags**: Port 8138 must run using canonical flags defined in `hermes/devel/_tools/run_model_server.sh` for each model mode. No uncoordinated server restarts or duplicate instances.
> 5. **Native Desktop Window Capture**:
>    * All recordings MUST capture authentic host application windows including titlebars, buttons, frames, and drop shadows via KWin ScreenShot2 DBus interface.
>    * Synthetic border rendering, manual window framing in PIL/OpenCV, or synthetic overlays are strictly forbidden.
> 6. **Zero Residuals**: Before and after each benchmark execution, all benchmark test processes (Konsole test windows, Chrome test instances, placeholder windows) must be cleanly terminated without touching host user processes.
