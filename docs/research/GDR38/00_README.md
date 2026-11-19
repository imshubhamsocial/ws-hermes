# GDR38 Master Release: Frontier 4B Architectures, Looped Transformers, Distillation, and Gemini Decision 1 Specification

> **Release Package**: GDR38  
> **Date**: November 14, 2026  
> **Substrate Target**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Substrate**: Dual-Track (Gemma 4 Exact 4B + NVIDIA Nemotron Dory 1.0 Looped 4B)  
> **Context Window Enforced**: 131,072 to 262,144 tokens (128K–256K, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Status**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, ceiling $\le 5,800.0\text{ MiB}$); 100% compute dedication (Wayland compositor on Intel iGPU / Disp.A: Off, 25 MiB idle); Host system on CPU & 16 GB System RAM  
> **Decision Oracle**: Google Gemini Decision 1 (`gemini-decision-1` via Gemini Decisions API, Nov 2026) for zero-token Layer 1 routing and invariant arbitration  
> **Status**: Verified and Operational | 5-Layer ICM Architecture Deployed | Gauntlets A, B, C Operational  

---

## 1. Master GitHub Repositories (Raw Endpoints)

| Repository Role | Canonical Raw Base URL | Target Branch | Local Workspace Directory |
| :--- | :--- | :--- | :--- |
| **Hermes Workspace & Code (ws-hermes)** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/` | `master` | `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes` |
| **Hermes Evaluation & Tests** | `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/` | `main` | `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks`<br>`/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/logs` |
| **Upstream Hermes Substrate** | `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/` | `main` | `~/.hermes/hermes-agent` (100% clean) |
| **Jake Van Clief ICM Repo** | `https://raw.githubusercontent.com/RinDig/Interpretable-Context-Methodology/main/` | `main` | `~/.cache/icm-datasets/Interpretable-Context-Methodology` |
| **ICM Template Repository** | `https://raw.githubusercontent.com/ktncodes/icm-template/main/` | `main` | `~/.cache/icm-datasets/icm-template` |
| **ICM Architect Skill** | `https://raw.githubusercontent.com/RinDig/icm-architect/main/` | `main` | `~/.agents/skills/icm-architect` |
| **Content Agent Routing** | `https://raw.githubusercontent.com/RinDig/Content-Agent-Routing-Promptbase/main/` | `main` | `~/.cache/icm-datasets/Content-Agent-Routing-Promptbase` |
| **Clief Notes Foundations** | `https://raw.githubusercontent.com/donroy26/Clief-Notes-Foundations-Tutor/main/` | `main` | `~/.cache/icm-datasets/Clief-Notes-Foundations-Tutor` |

---

## 2. Release Documents Index (GDR38)

| Document Number | Document Title | Path | Description |
| :--- | :--- | :--- | :--- |
| **Briefing** | Master Argon Consultation Brief | `docs/research/GDR38/01_master_argon_consultation_brief.md` | Executive briefing for Gemini Argon on frontier 4B models, looped transformers, and Gemini Decision 1 integration. |
| **Document 01** | Hardware Baseline and Current Champion Telemetry | `docs/research/GDR38/02_doc1_hardware_and_current_champion_baseline.md` | Hardware audit (RTX 3050 6 GB dedicated, 16 GB CPU/RAM host) and telemetry analysis of `Gemma 4 Exact 4B` on Port 8138. |
| **Document 02** | Frontier 4B Architectures, Looped Transformers, Distillation & Decision 1 Spec | `docs/research/GDR38/03_doc2_frontier_4b_models_and_gemini_decision_spec.md` | Comprehensive specifications across the 7 Golden Points: Gemma 4 optimizations, NVIDIA Dory looped inference ($k=2$ vs $k=4$), Qwen & Gemma evolutions, distilled 4B champions, exact `llama-server` runtime flags, abliterated/zero-refusal models, and Gemini Decision 1 ICM integration. |
| **Master Prompt** | Master Consultation Prompt for Gemini Argon | `docs/research/GDR38/04_master_argon_prompt.md` | Final consultation prompt to copy and paste into Gemini Argon with High Thinking enabled. |

---

## 3. Historical Research Corpus Ingested (`docs/research/`)

| Historical Package | Repository Path | Research Purpose |
| :--- | :--- | :--- |
| **GDR30** | `docs/research/GDR30 - Golden Benchmark State (GAIA, TAU-2)/` | Golden benchmark state and baseline evaluation evidence across GAIA and TAU-2. |
| **GDR31** | `docs/research/GDR31/` | Substrate synchronization and early harness contracts. |
| **GDR32** | `docs/research/GDR32/` | Telemetry harness and user systemd integration. |
| **GDR33** | `docs/research/GDR33/` | Gauntlet A netcode synchronization and jitter mitigations. |
| **GDR34** | `docs/research/GDR34/` | Gauntlet B OpenCV tracking and visual servoing. |
| **GDR35** | `docs/research/GDR35/` | Gauntlet C aquarium shader material diagnostics. |
| **GDR36** | `docs/research/GDR36/` | Certification roadmap and 4-tier skill precedence blueprint. |
| **GDR37** | `docs/research/GDR37/` | ICM repository reorganization, native Git migration, and `AGENTS.md` standardization. |
| **GDR38** | `docs/research/GDR38/` | Frontier 4B models, looped architectures (NVIDIA Dory), distillation, abliteration, and Gemini Decision 1 integration. |

---

## 4. The Seven Golden Research Mandates for Lead Architect Argon

1. **Golden Point 1 (Gemma 4 Exact 4B Enhancements)**: Research quantization improvements (Q4_K_M vs IQ4_NL), asymmetric KV caching (Q8_0 Key + Q4_0 Value), speculative drafter tuning, and sampling parameters to maximize code synthesis and tool precision.
2. **Golden Point 2 (NVIDIA Dory Looped Transformer)**: Analyze `NVIDIA-Nemotron-Labs-Dory1.0-4B` with 256K context. Evaluate trade-offs between $k=2$ loops (48 layers, high throughput for 20 Hz / 4 Hz loops) and $k=4$ loops (88 layers, frontier reasoning depth) under last-loop KV caching.
3. **Golden Point 3 (Latest Qwen & Gemma Evolutions)**: Survey Qwen 2.5/3/4 Coder variants and Gemma Argon/Carbon experimental 4B lines within our 6 GB VRAM budget.
4. **Golden Rule 4 (Distilled 4B Frontier-Beating Models)**: Identify distilled 4B parameter models that beat current small and frontier models across GAIA, SWE-bench Lite/Verified, TAU-2, and MATH-500.
5. **Golden Rule 5 (Production Upstream Flags & Sampling Values)**: Provide exact upstream `llama-server` runtime flags, sampling parameters (temperature, top-p, top-k, min-p, repetition penalty), and Jinja prompt templates for each candidate.
6. **Golden Point 6 (Abliterated & Zero-Denial Variants)**: Research uncensored, abliterated, and heretic fine-tunes to guarantee 0% refusals on systems programming, kernel debugging, and security workflows. Supply full hardware specs (dedicated 6 GB VRAM, CPU/16 GB RAM host).
7. **Golden Rule 7 (Google Gemini Decision 1 Integration)**: Evaluate `gemini-decision-1` (Gemini Decisions API, Nov 2026) for zero-token classification. Design its integration into Jake Van Clief's 5-Layer ICM as an automated Layer 1 router, invariant gate arbiter, and loop controller.

---

## 5. Executive Verification & Google Docs Safety Standard

All documents in this release adhere to strict standards:
- **ASD-STE100 Compliance**: Clear, active, unambiguous Simplified Technical English sentences under 25 words.
- **Even Code Fence Count**: Every opening code fence has a corresponding closing fence (`count % 2 == 0`).
- **Even Math Dollar Sign Parity**: Strict parity for inline and block LaTeX notation (`count % 2 == 0`).
- **Single-Line Tables**: Matching pipe counts per row with zero multi-line row wrapping.
- **Raw Web Endpoints**: Direct raw GitHub endpoints and direct Hugging Face links for headless web ingestion.
