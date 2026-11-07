# Procedural Rules: Gauntlet B — Autonomous Splatbox Browser Gameplay

> 1. **Step 1 — Host Browser Launch (89luca89/distrobox)**:
   * Create mkdir -p "$HOME/.cache/chrome_dev_debug".
   * Launch /usr/bin/distrobox-host-exec flatpak run com.google.ChromeDev --remote-debugging-port=9222 --user-data-dir="$HOME/.cache/chrome_dev_debug" --window-size=1280,720 "https://splatbox.alexdiaz.fyi/" &.
> 2. **Step 2 — Readiness & PointerLock Engagement (browser-use / CDP)**:
   * Poll http://127.0.0.1:9222/json until the Splatbox tab webSocketDebuggerUrl is available.
   * Poll DOM via Runtime.evaluate until document.querySelector('#play') && !document.querySelector('#play').disabled.
   * Click #play and verify #hud is unhidden (!document.getElementById('hud').hidden).
> 3. **Step 3 — Hybrid Vision & Ballistic Engagement Loop**:
   * Capture viewport frame via CDP Page.captureScreenshot (format: "jpeg", quality: 70).
   * Query embeddinggemma2 (Port 8139) / vision_tools.py on initial frame and every 10th cycle to confirm active target clusters and HUD state; run cv2.HoughCircles masking the top 80px and bottom 90px HUD regions to lock onto the nearest target bullseye.
   * Compute vertical drop offset, slew camera by relative deltas, and fire only when error <= 6.0 px.
   * Press KeyR whenever parseInt(document.getElementById('ammo').textContent) <= 5.
