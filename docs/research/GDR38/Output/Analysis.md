# Executive Analysis: GDR38 Frontier 4B Models and Gemini Decision 1 Architecture

> **Document**: Analysis.md  
> **Release Package**: GDR38  
> **Standard**: ASD-STE100 (Simplified Technical English)  
> **Date**: November 14, 2026  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Hardware Status**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, ceiling $\le 5,800.0\text{ MiB}$)  
> **Host Environment**: 100% compute dedication (Disp.A: Off, 25 MiB idle); Host system on CPU & 16 GB System RAM  
> **Source Blueprint**: `GDR38 4B Models & Decision 1 Blueprint.md`  

---

## 1. Executive Summary: The Hybrid Split-Plane Architecture

Lead Architect Argon authored the GDR38 research blueprint.
The blueprint evaluates next-generation 4B parameter models and Google Gemini Decision 1.
Every evaluated configuration stays strictly below our physical hardware ceiling of 5,800.0 MiB VRAM.

Argon introduces a **Hybrid Split-Plane Architecture**:
1. **The Cloud Control Plane (Google Gemini Decision 1)**:
   * Handles high-speed classification, task routing, and invariant verification.
   * Generates zero output tokens.
   * Responds in 150 to 250 milliseconds.
2. **The Local Execution Plane (Local Port 8138)**:
   * Dedicates 100% of local GPU memory to code synthesis and tool execution.
   * Runs local ~4B parameter models with zero safety refusals.

| Architectural Dimension | GDR37 Baseline Champion | GDR38 Upgraded Architecture | Operational Benefit |
| :--- | :--- | :--- | :--- |
| **Primary Models** | `gemma-4-E4B-it-q4_0-exact.gguf` | Gemma 4 Exact + Nemotron Dory 1.0 + DeepSeek-R1 Distill | Scales effective depth from 36 to 96 layers |
| **Context Window** | 131,072 tokens (128K) | 131,072 to 262,144 tokens (128K to 256K) | Double context window via Dory 3:1 sliding attention |
| **KV Cache Mode** | Symmetric Q4_0 (1,075 MiB) | Asymmetric Q8_0/Q4_0 (1,335 MiB) & Dory flat (1,120 MiB) | 128K needle retrieval increases from 96.8% to 99.4% |
| **Speculative Drafter** | MTP Drafter ($n=2$, unpruned, 29.5 t/s) | MTP Drafter ($n=2$, $p\text{-min}=0.75$, 30.8 t/s) | Draft acceptance increases from 68.4% to 74.6% |
| **ICM Task Routing** | Local generative LLM (1,500 to 3,000 ms) | Google Gemini Decision 1 (150 to 250 ms) | 10 times faster routing with zero output tokens |
| **Safety Refusal Rate** | 99/100 on low-level system tasks | 0/465 (HauhauCS) to 3/100 (Heretic ARA) | Eliminates agent failures during security gauntlets |

---

## 2. Directive 1: Gemma 4 Exact 4B Enhancements

Argon recommends three specific improvements for our current baseline champion:

### 2.1 Quantization Formats
* Google trained Gemma 4 using Quantization-Aware Training (QAT).
* Use `xbill9/gemma-4-E4B-it-qat-q4_0-exact.gguf` (3,922 MiB) when pairing with the MTP drafter.
* Use `IQ4_NL` (3,890 MiB) for standalone or abliterated executions.
* `IQ4_NL` uses a non-linear codebook. It reduces perplexity from 6.84 to 6.68 and reaches 99.3% tool accuracy.
* Always pass `-ot "per_layer_token_embd.weight=CUDA0"` to store Per-Layer Embeddings (PLE) in GPU memory.

### 2.2 Asymmetric KV Caching (`--cache-type-k q8_0 --cache-type-v q4_0`)
* Symmetric 4-bit KV caching (`q4_0/q4_0`) causes attention errors beyond 96,000 tokens.
* Upgrade to asymmetric caching: store **Keys in 8-bit** (`q8_0`) and **Values in 4-bit** (`q4_0`).
* Key vectors control attention routing. Value vectors store representation states.
* Asymmetric caching adds only 260 MiB of VRAM (total KV cache is 1,335 MiB at 128K context).
* Total active VRAM is 5,341 MiB, leaving 459 MiB of free safety margin.
* Needle-in-a-haystack retrieval accuracy rises from 96.8% to 99.4%.

### 2.3 Speculative Decoding Tuning
* Keep the 57 MB Multi-Token Prediction (MTP) companion drafter with draft length $n=2$.
* Add the probability cutoff parameter: `--spec-draft-p-min 0.75`.
* This parameter stops speculative drafting when draft token confidence drops below 75%.
* Drafting acceptance rises from 68.4% to 74.6%.
* Net generation speed increases to 30.8 tokens per second without rollback pauses.

### 2.4 Eliminating Tool Strip Loops (Issue #28825)
* Lower temperature from 1.0 to 0.2 (`--temp 0.2`) for deterministic tool calls.
* Add `--min-p 0.05` to remove low-probability tail tokens.
* Set `--repeat-penalty 1.05` to prevent repetitive loop errors.

---

## 3. Directive 2: NVIDIA Nemotron Dory 1.0 4B Looped Transformer

`NVIDIA-Nemotron-Labs-Dory1.0-4B` is an open-weight model with native **256K context** (`--ctx-size 262144`).

### 3.1 The Looped Architecture
Dory separates its transformer layers into three sequential blocks:
1. **Input Block**: 8 static layers that execute once.
2. **Recurrent Core Block**: 20 layers that execute in a loop $k$ times ($k \in \{1, 2, 4\}$).
3. **Output Block**: 8 static layers that execute once.

Total computational depth follows this formula: $\text{Depth} = 8 + 20k + 8$.
* When $k=1$: executes 36 total layer passes (baseline fast inference).
* When $k=2$: executes 56 total layer passes (48 post-input layers).
* When $k=4$: executes 96 total layer passes (88 post-input layers).

The 20 recurrent layers reuse the exact same weights across every loop pass.
The model file size never increases. It remains fixed at 3.5 GB on disk (3,584 MiB in VRAM for Q5_K_M).

### 3.2 Last-Loop KV Caching
Standard recurrent models copy attention caches on every loop pass, causing Out-Of-Memory errors.
Dory uses **Last-Loop KV Caching** (`dory.recurrent_kv_cache_mode=str:last_loop`):
* Intermediate loops ($1$ to $k-1$) overwrite temporary attention memory in place.
* Only the final loop ($k$) writes to permanent KV cache memory.
* The KV cache footprint stays completely flat across all loop counts (exactly 1,120 MiB at 128K context).
* Total active VRAM at 128K context is 4,704 MiB, leaving 1,096 MiB of free safety margin.

### 3.3 Quantitative Trade-Offs: $k=2$ Versus $k=4$

| Benchmark / Characteristic | Dory $k=2$ (56 Layers) | Dory $k=4$ (96 Layers) | Operational Significance |
| :--- | :--- | :--- | :--- |
| **Active VRAM (128K Context)** | 4,704 MiB | 4,704 MiB | Flat memory footprint across loops |
| **Generation Speed** | 24.2 tokens/sec | 13.8 tokens/sec | $k=2$ satisfies real-time 20 Hz and 4 Hz control loops |
| **Time To First Token** | 180 ms | 310 ms | $k=2$ delivers sub-200 ms response times |
| **SWE-bench Verified** | 59.5% | 61.8% | $k=4$ outperforms Qwen 3.5 9B (61.0%) |
| **HumanEval-X Coding** | 74.8% | 85.2% | $k=4$ provides +10.4% coding accuracy gain |
| **MATH-500 Proofs** | 71.4% | 82.6% | $k=4$ provides +11.2% mathematical deduction gain |

### 3.4 Operational Recommendation for Hermes
Deploy a **Dynamic Dual-Loop Strategy**:
1. **Run $k=2$ (`dory.num_loops=int:2`) for Reactive Gauntlets**:
   * Use for Gauntlet A (20 Hz netcode), Gauntlet B (4 Hz visual servoing), and CLI queries.
   * Provides 24.2 tokens per second and 180 ms response time.
2. **Run $k=4$ (`dory.num_loops=int:4`) for Deep ICM Compilation**:
   * Use for Phase contracts, complex SWE bug fixes, Three.js shaders, and multi-file refactoring.
   * Delivers 88 post-input layers of reasoning without increasing VRAM consumption.

---

## 4. Directives 3 & 4: Qwen Evolutions and Distilled Champions

Argon evaluated recent ~4B models within our 6 GB VRAM envelope:

1. **`Qwen2.5-Coder-3B-Instruct`**:
   * Consumes only 3,850 MiB total VRAM at 128K context.
   * Generates 34.0 tokens per second on our RTX 3050 GPU.
   * Scores 99.1% on tool calling with native `<tool_call>` tags. Serves as our fast tool specialist.
2. **`DeepSeek-R1-Distill-Qwen-4B`**:
   * 4.02B parameters, consumes 4,890 MiB VRAM at 128K context.
   * Scores **89.4%** on MATH-500, **86.8%** on HumanEval, and **91.0%** on TAU-2 tool use.
   * Outperforms larger 14B and 32B non-distilled models.
3. **`NVIDIA Dory 1.0 4B`**:
   * Scores **61.8%** on SWE-bench Verified at $k=4$.
   * Ranks first overall on $\tau^3$-bench banking tool use.

---

## 5. Directive 5: Production `llama-server` Launch Commands

Argon provided exact production launch commands for Port 8138:

### Track 1A: Gemma 4 Exact (Asymmetric KV Cache + MTP Drafter)
```bash
exec taskset -c 0-5 /var/home/imshubhamsocial/.local/bin/llama-server.bin \
    --model "/var/home/imshubhamsocial/.hermes/models/gemma-4-E4B-it-q4_0-exact.gguf" \
    --model-draft "/var/home/imshubhamsocial/.hermes/models/gemma-4-E4B-it-qat-assistant-q4_0-exact.gguf" \
    --n-gpu-layers-draft all \
    --spec-type draft-mtp \
    --spec-draft-n-max 2 \
    --spec-draft-p-min 0.75 \
    --alias "gemma-4-exact" \
    --host 127.0.0.1 --port 8138 \
    --ctx-size 131072 \
    --cache-type-k q8_0 --cache-type-v q4_0 \
    --batch-size 2048 --ubatch-size 1024 \
    --flash-attn on --reasoning on --jinja --n-gpu-layers 99 \
    --threads 6 --threads-batch 6 --parallel 1 --cont-batching \
    --temp 0.2 --top-p 0.95 --top-k 64 --min-p 0.05 --repeat-penalty 1.05 --metrics
```

### Track 1B: NVIDIA Nemotron Dory 1.0 4B (Looped 256K Context)
```bash
exec taskset -c 0-5 /var/home/imshubhamsocial/.local/bin/llama-server.bin \
    --model "/var/home/imshubhamsocial/.hermes/models/NVIDIA-Nemotron-Labs-Dory1.0-4B-Q5_K_M.gguf" \
    --alias "dory,nemotron-dory" \
    --host 127.0.0.1 --port 8138 \
    --ctx-size 262144 \
    --cache-type-k q4_0 --cache-type-v q4_0 \
    --batch-size 2048 --ubatch-size 1024 \
    --flash-attn on --jinja --n-gpu-layers 99 \
    --threads 6 --threads-batch 6 --parallel 1 --cont-batching \
    --temp 0.3 --top-p 0.90 --top-k 50 --min-p 0.05 --repeat-penalty 1.08 \
    --override-kv "dory.num_loops=int:2,dory.recurrent_kv_cache_mode=str:last_loop" \
    --metrics
```

---

## 6. Directive 6: Zero-Denial Abliterated Models

Standard models refuse commands when inspecting `/proc`, binding raw sockets, or debugging binaries.
Argon evaluated **Arbitrary-Rank Ablation (ARA)** using **Heretic v1.2.0**:
* Removes the refusal vector $v$ from weight matrices: $W' = W - v v^T W$.
* Eliminates refusal responses while preserving 99.8% of coding and reasoning capabilities.
* **Top verified models**:
  * `llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic-GGUF`: Refusals drop from 99/100 to 3/100.
  * `HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive`: 0/465 refusals (100% compliance).
  * `somenetworktrouble/NVIDIA-Nemotron-Labs-Dory1.0-4B-heretic-GGUF`: Zero refusals on 256K Dory.

---

## 7. Directive 7: Google Gemini Decision 1 Architecture & ICM Integration

Released on November 11, 2026, **Gemini Decision 1** (`gemini-decision-1` via `client.decisions.create` in v1beta):
* Reads up to 262,144 input tokens.
* Evaluates up to 1,000 structured questions in parallel during a single forward pass.
* Generates zero output tokens (pricing is $0.10 per 1M input tokens, $0.00 for output tokens).
* Returns calibrated linear probabilities (0.0 to 1.0) in 150 to 250 milliseconds.

### Argon's Three-Pillar ICM Integration Plan:
Argon authored a complete Python class (`HermesDecisionOracle`) to automate ICM:

1. **Pillar 1 (Zero-Token Task Router)**:
   * Evaluates user prompt plus root `CONTEXT.md` in one forward pass.
   * Returns the exact destination stage folder with confidence percentage in 75 ms.
2. **Pillar 2 (Invariant Gate Arbiter)**:
   * Audits stage artifacts and `contract.sh` output against Rules 1–10.
   * Returns structured verdicts: `PASS_ALL_INVARIANTS`, `FAIL_RULE_5_VRAM_CEILING`, etc.
   * Prevents self-grading bias (Rule 8).
3. **Pillar 3 (Dynamic Loop Controller)**:
   * Evaluates task difficulty.
   * Directs local inference to Dory $k=2$ (reactive), Dory $k=4$ (deep code), or Gemma 4 Exact (tools).

---

## 8. Master Summary Comparison of Models

| Candidate Model | Context | VRAM Footprint | Primary Role in Hermes | Generation Speed |
| :--- | :--- | :--- | :--- | :--- |
| **Gemma 4 Exact 4B** | 131,072 | 5,341 MiB (Asymmetric KV) | Multimodal tasks, tool calling, 128K needle retrieval | 30.8 t/s |
| **NVIDIA Dory 1.0 ($k=2$)** | 262,144 | 4,704 MiB (Flat KV) | Real-time agent loops (Gauntlets A & B, 20 Hz / 4 Hz) | 24.2 t/s |
| **NVIDIA Dory 1.0 ($k=4$)** | 262,144 | 4,704 MiB (Flat KV) | Deep code generation, SWE-bench bug fixes, shaders | 13.8 t/s |
| **Qwen 2.5 Coder 3B** | 131,072 | 3,850 MiB | High-speed CLI execution, syntax generation | 34.0 t/s |
| **DeepSeek-R1 Distill 4B** | 131,072 | 4,890 MiB | Formal mathematics, algorithmic verification, MATH-500 | 25.0 t/s |
| **Gemini Decision 1** | 262,144 | Cloud (0 MiB GPU) | Layer 1 task routing and Layer 2 invariant gate auditing | 50–100 ms |

---

## 9. Immediate Implementation Plan for Hermes

To apply the GDR38 blueprint in `ws-hermes`:
1. **Apply Asymmetric KV Cache**: Update `/var/home/imshubhamsocial/.local/bin/llama-server` to pass `--cache-type-k q8_0 --cache-type-v q4_0` and `--spec-draft-p-min 0.75`.
2. **Download NVIDIA Dory GGUF**: Obtain `NVIDIA-Nemotron-Labs-Dory1.0-4B-Q5_K_M.gguf` under `~/.hermes/models/`.
3. **Deploy `HermesDecisionOracle`**: Embed Argon's Python script into `hermes/devel/_tools/` to automate Layer 1 task routing with zero generated tokens.
