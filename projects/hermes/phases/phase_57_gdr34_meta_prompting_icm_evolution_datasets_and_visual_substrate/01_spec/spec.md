# Phase 57 Specification: GDR34 Blueprint Implementation & 128K ICM Integration

## 1. Problem Statement & Background

During GDR33 and Gauntlet B evaluations, Hermes exhibited "coding exam syndrome" when fed monolithic, complex multi-instruction prompts. Furthermore, Gauntlet B suffered from flat structure where the LLM skipped directly to Stage 3 blind execution without performing DOM/CDP coordinate probes or controller verification.

In GDR34, Argon provided an architectural blueprint across 7 Golden Points to solve this by:
1. Deconstructing monolithic tasks into strict ICM compiler pipelines.
2. Adopting Jake Van Clief's One Fact One Home paradigm (arXiv:2603.16021).
3. Importing upstream ICM evolution datasets from RinDig and ktncodes into local cache.
4. Restructuring Gauntlet B into a 3-stage pipeline (`01-probe/`, `02-controller/`, `03-execute/`).
5. Selecting Gemma 4 Exact with speculative drafting and adjusting context to 128k (`-c 131072`) with TurboQuant Q4_0 KV cache, which safely operates under the 5,800.0 MiB hardware ceiling.
6. Implementing deterministic visual target centroid tracking via OpenCV HoughCircles (CPU-based, zero VRAM, 60 Hz).
7. Incorporating enterprise ICM consulting practices (clean markdown contracts, <=60-line scripts, upstream purity).

## 2. Invariants & Ceilings

- **Active Hardware VRAM**: NVIDIA RTX 3050 Laptop GPU (6,144 MiB total GDDR6) active allocation must not exceed 5,800.0 MiB.
- **Context Length**: Full 128K context (`context_length: 131072`) enabled with `-c 131072`, `-ctk q4_0 -ctv q4_0`, `--flash-attn on`, and `--reasoning on`.
- **Upstream Purity**: Upstream submodule `~/.hermes/hermes-agent` must have 0 uncommitted changes.
- **Zero Bespoke Wrappers**: No custom python or shell scripts in `scripts/` or `plugins/`.
- **Line Discipline**: All `CONTEXT.md` files strictly <= 80 lines; all `rules/*.md` <= 200 lines.
