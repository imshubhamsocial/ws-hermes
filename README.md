# Hermes Agent OS (ws-hermes) — GDR37 5-Layer ICM Software Factory

> **Substrate**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Engine**: Gemma 4 Exact (`gemma-4-E4B-it-q4_0-exact.gguf` + MTP Drafter) on Port 8138  
> **Context Window**: 131,072 tokens (128K context, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Envelope**: NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB GDDR6, ceiling <= 5,800.0 MiB)  
> **Methodology**: Jake Van Clief's Interpretable Context Methodology (ICM, arXiv:2603.16021)  

## 1. Five-Layer ICM Architecture

* **Layer 0 (`AGENTS.md`, `IDENTITY.md`, `.hermes/SOUL.md`)**: Workspace map and 10 non-negotiable compiler rules (< 60 lines).
* **Layer 1 (`CONTEXT.md`)**: Task router and keyword triggers (< 80 lines).
* **Layer 2 (`stages/*/CONTEXT.md`, `benchmarks/*/CONTEXT.md`)**: Bounded single-job stage contracts (< 80 lines).
* **Layer 3 (`_config/`, `shared/`, `_templates/`, `_tools/`, `skills/`)**: System invariants, domain schemas, and deterministic validators (< 200 lines).
* **Layer 4 (`stages/*/output/`, `benchmarks/*/output/`, `phases/`)**: Inspectable plain-text deliverables and sealed verification receipts.

## 2. Quickstart Verification Commands

```bash
cd hermes/devel
python3 _tools/hermes_icm_validator.py
make all
make phase-58-seal
```
