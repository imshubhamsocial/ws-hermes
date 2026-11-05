# Layer 3: Hermes System-Wide Invariants (Tripartite 60% Core)

## 1. Hardware and VRAM Envelope Invariants

* Host OS: Fedora Kinoite 44 (x86_64, rpm-ostree immutable atomic desktop).
* Discrete GPU: NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6).
* Hard VRAM Safety Ceiling (Active Inference): 5,800.0 MiB maximum under 131,072-token (128K) context with Q4_0 TurboQuant KV cache (-ctk q4_0 -ctv q4_0).
* Quiescent VRAM Ceiling (Daemon Stopped): <= 100.0 MiB (40 MiB nominal idle at ~55°C, 12W) when hermes-llama-server.service is stopped.
* Display Compositor Offload: Wayland compositor must run on the Intel integrated GPU (Disp.A: Off on NVIDIA nvidia-smi).
* CPU Vision Offload: Computer vision centroid calculations (OpenCV HoughCircles) must run on host CPU (0 MiB GPU VRAM, < 5 ms frame latency).

## 2. Canonical Network Port Map

* Port 8138: Local llama-server OpenAI-compatible inference engine (http://127.0.0.1:8138/v1) and /slots endpoint.
* Port 8642: Hermes Agent Gateway API server (http://127.0.0.1:8642/v1).
* Port 1933: OpenViking persistent memory graph daemon (http://127.0.0.1:1933).
* Port 8139: Dedicated SmolVLM2 vision daemon (on-demand).
* Port 9222: Chromium / Chrome DevTools Protocol (CDP) debugging endpoint (http://127.0.0.1:9222).

## 3. Execution and Verification Invariants

* Champion Primary Substrate: xbill9/gemma-4-E4B-it-qat-q4_0-exact.gguf (4,169 MiB VRAM at 128K).
* Secondary Substrate: unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-UD-Q4_K_XL.gguf (4,975 MiB VRAM at 128K).
* Deprecated Substrate: google/gemma-4-E4B-it-qat-q4_0-gguf (prohibited for tool calling due to QAT logit shift).
* Read-Before-Edit Law: Every fresh-context stage must invoke read_file on existing disk targets prior to calling file-edit tools.
* Headless Runtime Gate: Every browser/WebGL deliverable must pass the 4-Gate Playwright Runtime Audit (0 console errors, 0 page errors, 0 HTTP 4xx/5xx responses, 1280x720 non-degenerate pixel variance).
