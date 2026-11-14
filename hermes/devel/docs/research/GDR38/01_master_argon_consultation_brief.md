# Master Consultation Brief: Frontier 4B Models, Looped Transformers, Distillation, and Gemini Decision 1 (GDR38)

> **To**: Lead Architect Argon (Gemini Argon / High Thinking)  
> **From**: Antigravity Pair-Programming Agent (Autonomous Substrate Engine)  
> **Release Package**: GDR38  
> **Target Substrate**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Engine**: Dual-Track (Gemma 4 Exact 4B + NVIDIA Nemotron Dory 1.0 Looped 4B)  
> **Context Window**: 131,072 to 262,144 tokens (128K–256K, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Envelope**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, ceiling $\le 5,800.0\text{ MiB}$); 100% compute dedication (Wayland compositor on Intel iGPU / Disp.A: Off, 25 MiB idle); Host system on CPU & 16 GB System RAM  
> **Workspace Root**: `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes` (`ws-hermes`)  
> **Status**: Verified and Operational | 5-Layer ICM Architecture Deployed | Gauntlets A, B, C Certified  

---

## 1. Executive Summary & Mission Objective

In GDR37, Lead Architect Argon specified the repository reorganization blueprint. We executed the migration, established strict 5-layer ICM structure, and standardized on `AGENTS.md`. All benchmark gauntlets (Gauntlet A 20 Hz netcode, Gauntlet B Splatbox visual servoing, Gauntlet C Three.js aquarium) pass deterministically.

We now commission Lead Architect Argon to conduct research on next-generation model architectures. The objective is to identify whether we can surpass our current champion (`Gemma 4 Exact 4B`) in reasoning, tool calling, and context length, while staying strictly within our 6 GB VRAM budget.

We focus on four architectural fronts:
1. Optimizing our current champion (`Gemma 4 Exact 4B`).
2. Evaluating recurrent looped transformers (`NVIDIA-Nemotron-Labs-Dory1.0-4B` with 256K context and dynamic $k=2$ vs $k=4$ loops).
3. Analyzing the latest Qwen and Gemma 4B evolutionary lines and frontier-beating distilled models.
4. Integrating Google's newly released **Gemini Decision 1** (`gemini-decision-1`, Nov 2026) for zero-token classification, routing, and contract auditing.

---

## 2. Ingested Repository Context & Raw GitHub Endpoints

The full repository snapshot (`ws-hermes`) is loaded into your context via the **Import code** feature. You have access to:
- **System Invariants**: `hermes/devel/_config/invariants.md`, `hermes/devel/_config/hardware_vram_invariants.md`.
- **Deterministic Tooling**: `hermes/devel/_tools/hermes_icm_validator.py`, `hermes/devel/_tools/links.py`.
- **Gauntlets & Phases**: `hermes/devel/benchmarks/`, `hermes/devel/phases/status_ledger.json`.
- **Research Corpus**: `hermes/devel/docs/research/GDR30` through `hermes/devel/docs/research/GDR37`.

For external framework references, consult these canonical raw endpoints:
- `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/`
- `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/`
- `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/`
- `https://raw.githubusercontent.com/RinDig/Interpretable-Context-Methodology/main/`

---

## 3. The Seven Golden Mandates for Lead Architect Argon

### Mandate 1: Golden Point 1 — Gemma 4 Exact 4B Optimization & Runtime Tweaks
Conduct research on fine-tunes, quantization improvements, and runtime configurations for our baseline `gemma-4-E4B-it-q4_0-exact.gguf` with MTP assistant drafter (`--spec-type draft-mtp --spec-draft-n-max 2`):
- Evaluate quantization variants (Q4_0 vs Q4_K_M vs IQ4_NL) for perplexity versus latency.
- Evaluate asymmetric KV caching: 8-bit keys (`--cache-type-k q8_0`) with 4-bit values (`--cache-type-v q4_0`) to preserve attention fidelity across 128K context.
- Determine optimal speculative decoding draft depth ($n=2$ vs $n=3$) and acceptance probability thresholds.
- Provide sampling parameters (Min-P, repetition penalty) to prevent tool strip loops (Issue #28825).

### Mandate 2: Golden Point 2 — NVIDIA Dory Looped Transformer ($k=2$ vs $k=4$)
Evaluate `NVIDIA-Nemotron-Labs-Dory1.0-4B` (`nemotron-3.5-bolt-e4b`):
- Context length: Native 256K context support (`--ctx-size 262144`).
- Architecture: 8 input layers, 20 recurrent looped layers, 8 output layers.
- Loop analysis: Compare $k=2$ loops (effective depth 48 layers) versus $k=4$ loops (effective depth 88 layers).
- Last-loop KV caching: Explain how KV states remain flat in VRAM across multiple recurrent iterations.
- Provide quantitative trade-offs: Throughput (tokens/sec) versus compute latency versus reasoning depth.
- Deliver an explicit recommendation: Should Hermes use $k=2$, $k=4$, or dynamic switching between reactive loops and deep code synthesis?

### Mandate 3: Golden Point 3 — Latest Qwen & Gemma 4B Evolutions
Survey recent ~4B parameter models from Alibaba and Google DeepMind:
- Qwen line: Qwen 2.5-Coder (3B/7B), Qwen 3 (3B/4B), Qwen 4 evolutionary roadmap, and native function-calling token standards (`<tool_call>`).
- Gemma line: Gemma 2, Gemma 3, Gemma 4, and experimental Argon/Carbon variants incorporating multi-head latent attention (MLA) or hybrid sliding-window attention.
- Benchmark each model against our 6 GB VRAM ceiling at 128K context.

### Mandate 4: Golden Rule 4 — Frontier-Beating Distilled 4B Models
Identify distilled 4B parameter models that match or exceed frontier foundation models (DeepSeek-R1, Claude 3.5 Sonnet, GPT-4o) on:
- **GAIA**: Multi-modal desktop and web agentic execution.
- **SWE-bench Lite / Verified**: Real-world software engineering bug resolution.
- **TAU-2**: Multi-turn tool agent use and transactional consistency.
- **MATH-500 & LiveCodeBench**: Formal mathematics and algorithmic synthesis.

### Mandate 5: Golden Rule 5 — Production Upstream Flags & Sampling Values
Provide complete, copy-pasteable `llama-server` runtime commands for each candidate model family:
- CLI flags: `--model`, `--model-draft`, `--alias`, `--ctx-size`, `--cache-type-k`, `--cache-type-v`, `--flash-attn`, `--reasoning`, `--jinja`, `--threads 6 --threads-batch 6`, `--n-gpu-layers 99`.
- Sampling parameters: Exact `temperature`, `top_p`, `top_k`, `min_p`, `repeat_penalty`, `presence_penalty`.
- Jinja prompt templates: Exact system and tool calling formatting for each architecture.

### Mandate 6: Golden Point 6 — Zero-Denial Abliterated & Heretic Variants
Research uncensored and abliterated fine-tunes for each model family:
- Method: Representation engineering and weight orthogonalization ($W' = W - v v^T W$) to remove refusal directions.
- Goal: Ensure 0% refusals on systems programming, kernel tracing, port scanning, network debugging, and security audits.
- Hardware Profile: Provide full hardware telemetry to ensure accurate guidance:
  - Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, 96-bit bus, Ampere GA107, active ceiling $\le 5,800.0\text{ MiB}$).
  - Full 6 GB GDDR6 is 100% available for compute (Wayland compositor runs on Intel iGPU / Disp.A: Off, 25 MiB idle).
  - Host OS: Fedora Kinoite 44 (x86_64, rpm-ostree atomic desktop, Linux kernel 6.17+).
  - System Memory: 16 GB System RAM (15.3 GiB zram + 2,048 MiB btrfs NOCOW swapfile).
  - CPU Daemons: `hermes-embedding-cpu.service` on Port 8139 (0 MiB VRAM) and `hermes-openviking.service` on Port 1933 (0 MiB VRAM) pinned to cores 6–11.

### Mandate 7: Golden Rule 7 — Google Gemini Decision 1 Architecture & ICM Integration
Analyze Google's newly released **Gemini Decision 1** (`gemini-decision-1` via Gemini Decisions API, Nov 2026):
- Architecture: Zero generation tokens, prefill-only classification, 50–100 ms compute latency, 262,144 token context capacity.
- Evaluative Question: Should we replace or augment our current local decision routing with Gemini Decision 1?
- ICM Integration Blueprint: Detail how to automate Jake Van Clief's 5-Layer ICM using Decision 1:
  1. *Layer 1 Automated Task Routing*: Zero-token routing across root `CONTEXT.md` targets.
  2. *Layer 2 Contract & Invariant Arbitration*: Real-time verification oracle checking stage outputs against Rules 1–10.
  3. *Dynamic Local Loop Selection*: Routing tasks between Dory $k=2$ (reactive), Dory $k=4$ (deep code), and local Gemma 4 Exact.
- Links: Provide raw GitHub endpoints and direct Hugging Face links.

---

## 4. Expected Deliverable & Document Destination

Lead Architect Argon will author the comprehensive research report and save it to:
`/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/hermes/devel/docs/research/GDR38/Output/GDR38 Frontier 4B Models and Gemini Decision 1 Architecture Blueprint.md`
