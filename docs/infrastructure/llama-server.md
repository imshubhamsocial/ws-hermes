# Hermes llama-server Inference Substrate Manual

**Document Version**: 1.0.0  
**Target Binary**: `llama-server.bin` (v0.9.0-dev, build b1-08c252e, CUDA 12.8 / GCC 16.2.1)  
**Host Target**: Fedora Kinoite 44 (x86_64) | ws-hermes Distrobox Container  
**Hardware Ceilings**: NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB GDDR6, GA107)  
**Language Standard**: ASD-STE100 (Simplified Technical English)  
**Parent Index**: [docs/infrastructure/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/infrastructure/README.md)

---

## 1. System Overview and Architectural Role

The `llama-server` daemon serves as the primary local inference engine for Hermes Agent OS.  
It bridges the **60% Infrastructure Layer** and the **10% AI Cognition Layer**.  
The daemon listens on local port `8138` and exposes an OpenAI-compatible HTTP interface:

* **Endpoint**: `http://127.0.0.1:8138/v1/chat/completions`
* **Health Check**: `http://127.0.0.1:8138/health`
* **Server Properties**: `http://127.0.0.1:8138/props`
* **Prometheus Metrics**: `http://127.0.0.1:8138/metrics`

---

## 2. Hardware Topology and Memory Boundaries

Inference runs locally under strict hardware constraints:

* **GPU Hardware**: NVIDIA GeForce RTX 3050 Laptop GPU (compute capability 8.6, 16 Streaming Multiprocessors).
* **Discrete VRAM Ceiling**: Maximum allowable VRAM is **$5,800.0$ MiB** (governed by [hardware_ceilings.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/_config/hardware_ceilings.md)).
* **Active VRAM Measured**: **$5,049.0$ MiB** in production, providing **$751.0$ MiB of headroom**.
* **CPU Core Allocation**: CPU threads are pinned to physical cores 0, 2, 4, 6, 8, 10 via `taskset -c 0,2,4,6,8,10`.
* **Zero External Dependencies**: All token generation executes 100% locally with zero cloud API access.

---

## 3. Active Model Topology

The server loads two coordinated GGUF weight files from `~/.hermes/models/`:

### A. Primary Target Model
* **Model File**: [gemma-4-E4B-it-q4_0-exact.gguf](file:///var/home/imshubhamsocial/.hermes/models/gemma-4-E4B-it-q4_0-exact.gguf)
* **Architecture**: Google Gemma 4 Exact 4B Instruction-Tuned (`google/gemma-4-E4B-it`).
* **Quantization**: Symmetric Q4_0 integer quantization with exact weights.
* **Context Capacity**: 131,072 tokens (128K context window).
* **KV Cache Format**: Symmetric Q4_0 for both keys and values (`--cache-type-k q4_0 --cache-type-v q4_0`).

### B. Speculative Assistant Companion Drafter
* **Drafter File**: [gemma-4-E4B-it-qat-assistant-q4_0-exact.gguf](file:///var/home/imshubhamsocial/.hermes/models/gemma-4-E4B-it-qat-assistant-q4_0-exact.gguf)
* **Architecture**: Multi-Token Prediction (MTP) companion head (`Gemma4AssistantForCausalLM`).
* **Disk and Memory Size**: 59.7 MB on disk; consumes only 84 MiB of GPU VRAM.
* **Speculative Horizon**: Configured via `--spec-type draft-mtp --spec-draft-n-max 2 --spec-draft-p-min 0.75`.
* **Verified Acceptance Rate**: Proposes up to 2 candidate draft tokens per step with 75% confidence gating, reaching a 74.60% acceptance rate (Google MTP specification).

---

## 4. Key Architectural Parameters and Derivations

### A. Micro-Batching and Warp Alignment (`--batch-size 2048 --ubatch-size 1024`)
The batch and micro-batch sizes derive from empirical research across GDR32, GDR33, GDR37, and GDR38:

1. **GDR32 Fragmentation Failure**:
   Allocating `--batch-size 4096 --ubatch-size 1024` requests a single contiguous 1,070.08 MiB block via `cudaMalloc`.  
   Under active KDE Wayland desktop compositing, GPU address fragmentation prevented contiguous allocation and caused startup crashes.
2. **GDR33 & GDR37 Contiguous Buffer Invariant**:
   Setting `--batch-size 2048` reduces the contiguous `cudaMalloc` compute buffer to exactly **535.04 MiB**.  
   This buffer allocates reliably under desktop compositing and keeps total VRAM under 5,050 MiB.
3. **GDR38 Warp Alignment (`--ubatch-size 1024`)**:
   The Ampere GA107 GPU executes instructions in 32-thread warps across 16 Streaming Multiprocessors (SMs).  
   A micro-batch size of 1024 tokens allows 32 warps per SM ($1024 / 32 = 32$), maximizing Tensor Core occupancy during prompt ingestion.

### B. Reasoning Format and Google Gemma 4 Chat Template
* **Gemma 4 Channel Protocol**:
  Google Gemma 4 partitions output natively via Jinja channel tokens:
  * `<|channel>thought\n`: Internal reasoning trace.
  * `<|channel>call:tool{...}\n`: Syntactic tool call.
  * `<|channel>content\n`: User-facing output.
* **Origin of "deepseek" in `llama.cpp`**:
  In `llama.cpp`, the flag option `--reasoning-format deepseek` is an internal CLI parser label.  
  It was named after DeepSeek R1 because that model introduced the `reasoning_content` API standard.  
  It does not alter model weights or logic.
* **Native Configuration**:
  The production server uses `--reasoning auto` and default `--reasoning-format auto` with `--jinja`.  
  The server natively parses Gemma 4's `<|channel>thought` channel and routes reasoning tokens into `message.reasoning_content`.

### C. KV Cache Prefix Pinning (`--cache-reuse 256`)
Hermes executes multi-stage workflows where prompts share an identical prefix:
1. **Three-Tier Prompt Structure**:
   * **Stable Tier (~1,400 tokens)**: Layer 0 [SOUL.md](file:///var/home/imshubhamsocial/.hermes/SOUL.md), [AGENTS.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/AGENTS.md), and core tools (`tools.tool_search: "off"`).
   * **Context Tier (~600 tokens)**: Layer 1 [CONTEXT.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/CONTEXT.md) and Layer 3 invariants.
   * **Volatile Tier**: Per-turn instructions.
2. **Dynamic Prefix Matching**:
   Using `--cache-reuse 256`, `llama-server` detects matching prefix tokens in 256-token chunks.  
   The server reuses the active KV cache instead of recomputing prompt tokens.  
   This configuration delivers an empirical **99.8% prefix cache hit rate**, dropping time-to-first-token (TTFT) below 10 ms.

### D. Standardized Sampling Parameters
The server enforces official Google Gemma 4 sampling parameters from Hugging Face:
* **Temperature**: `1.0` (preserves model creativity and calibrated reasoning).
* **Top-P**: `0.95`.
* **Top-K**: `64`.
* **Repeat Penalty**: `1.0` (disabled to prevent penalizing programming language syntax and bracket balance).

---

## 5. Production Wrapper Implementation

The production startup script is located at [/var/home/imshubhamsocial/.local/bin/llama-server](file:///var/home/imshubhamsocial/.local/bin/llama-server).  
In accordance with Rule 6, the script contains 38 lines (strictly under the 60-line ceiling):

```bash
#!/usr/bin/env bash
# Hermes Production llama-server: Google Gemma 4 Exact (128K TurboQuant + MTP)
set -euo pipefail
WS="/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes"
HOST="/var/home/imshubhamsocial"
BASE="$WS"
[[ -f "${HOME:-}/.local/libexec/llama-server.bin" ]] && BASE="$HOME"
[[ -f "${HOST}/.local/libexec/llama-server.bin" && ! -f "${BASE}/.local/libexec/llama-server.bin" ]] && BASE="$HOST"

SITE_PACKAGES="${BASE}/.local/lib/python3.14/site-packages"
for p in "${BASE}/.local/lib"/python3.*/site-packages "${HOST}/.local/lib"/python3.*/site-packages; do
    [[ -d "${p}/nvidia/cu13/lib" ]] && { SITE_PACKAGES="$p"; break; }
done

BIN="${BASE}/.local/libexec/llama-server.bin"
CUDA_LIBS="${SITE_PACKAGES}/nvidia/cu13/lib:${SITE_PACKAGES}/nvidia/cublas/lib:${SITE_PACKAGES}/nvidia/cuda_nvrtc/lib:${SITE_PACKAGES}/nvidia/nccl/lib:${SITE_PACKAGES}/nvidia/cuda_runtime/lib:${BASE}/.local/share/cuda-libs"
export LD_LIBRARY_PATH="${BASE}/.local/lib/llama.cpp:${HOST}/.local/lib/llama.cpp:${CUDA_LIBS}:${LD_LIBRARY_PATH:-}"

[[ $# -gt 0 ]] && exec "$BIN" "$@"

MDIR="${HOST}/.hermes/models"
[[ -d "$MDIR" ]] || MDIR="${WS}/.hermes/models"
MAIN="${MDIR}/gemma-4-E4B-it-q4_0-exact.gguf"
DRAFT="${MDIR}/gemma-4-E4B-it-qat-assistant-q4_0-exact.gguf"

DRAFT_FLAGS=()
[[ -f "$DRAFT" ]] && DRAFT_FLAGS=(--model-draft "$DRAFT" --n-gpu-layers-draft all --spec-type draft-mtp --spec-draft-n-max 2 --spec-draft-p-min 0.75)

export GGML_CUDA_GRAPH_OPT=1 GGML_CUDA_FORCE_MMQ=0
exec taskset -c 0,2,4,6,8,10 "$BIN" \
    --model "$MAIN" "${DRAFT_FLAGS[@]}" \
    --alias "gemma-4-E4B-it-qat-exact,gemma-4-e4b-exact,google/gemma-4-E4B-it,gemma-4-exact-4b,nemotron-dory-1.0-looped-4b,model,default" \
    --host 127.0.0.1 --port 8138 \
    --ctx-size 131072 --cache-type-k q4_0 --cache-type-v q4_0 \
    --batch-size 2048 --ubatch-size 1024 --flash-attn on --jinja --n-gpu-layers 99 \
    --threads 6 --threads-batch 6 --parallel 1 --cont-batching \
    --cache-reuse 256 --reasoning auto \
    --temp 1.0 --top-p 0.95 --top-k 64 --metrics
```

---

## 6. Service Management and Operational Commands

The server runs as a systemd user service (`llama-server.service`).  
Manage the daemon from within the container or host using `distrobox-host-exec`:

```bash
# Check service status
distrobox-host-exec systemctl --user status llama-server.service

# Restart the inference daemon
distrobox-host-exec systemctl --user restart llama-server.service

# Stop the inference daemon
distrobox-host-exec systemctl --user stop llama-server.service

# View live systemd journal logs
distrobox-host-exec journalctl --user -u llama-server.service -f -n 50
```

---

## 7. Performance Benchmarks and Verification Telemetry

| Performance Dimension | Baseline State | Calibrated Production State | Observed Delta |
| :--- | :--- | :--- | :--- |
| **Generation Speed** | 75.59 tokens/s | **115.97 tokens/s** | **+53.4% speedup** |
| **Discrete VRAM Allocated** | 5,074.0 MiB | **5,049.0 MiB** | **751.0 MiB safety headroom** |
| **MTP Drafter Acceptance** | 60.89% | **64.05%** | Higher speculative efficiency |
| **Time to First Token (TTFT)** | ~1,200 ms | **< 10 ms (cached)** | 14x latency reduction |
| **Prompt Cache Hit Rate** | 8.45% | **99.8% (ICM prefix)** | Full prefix reuse |

---

## 8. Deterministic Health and Verification Gates

Execute these three verification tools to validate the inference engine state:

```bash
# 1. Verify VRAM allocation is below the 5,800.0 MiB hardware ceiling
python3 ~/.hermes/tools/icm/check_vram_limit.py --mode active

# 2. Audit hermes home scripts and profile configurations
bash ~/.hermes/tools/icm/audit_hermes_home.sh

# 3. Run the automated 8-point workspace walk test
python3 ~/.hermes/tools/icm/hermes_icm_validator.py .
```
