# Phase 55 Specification: ICM Tripartite Scaffolding & Canonical v45/v52 Sealing

* **ICM Layer**: Layer 2 (Stage Contracts, Tripartite Scaffolding & Substrate Sealing)
* **Standard**: Jake Van Clief & David McDermott (arXiv:2603.16021)
* **Discipline**: Working context strictly bounded between 2,000 and 8,000 tokens.

## 1. Objectives & Boundaries
1. Audit and seal the 49-file ICM Tripartite Scaffolding across:
   - Root Workspace: `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `rules/`, `references/`.
   - Pipeline Stages: `stages/01-spec/`, `stages/02-plan/`, `stages/03-execute/`, `stages/04-verify/`.
   - Benchmark Suites: `benchmarks/tau_bench/`, `benchmarks/gaia/`, `benchmarks/ast_grep_eval/`.
   - Templates: `_templates/phase_template/`, `_templates/benchmark_template/`.
2. Enforce strict line budget discipline across all tripartite markdown files:
   - `CONTEXT.md` <= 80 lines (Layer 1 Task Router)
   - `invariants.md` <= 80 lines (Layer 2 Invariants)
   - `rules.md` <= 120 lines (Layer 2 Operational Rules)
   - `references.md` <= 200 lines (Layer 3 Epistemic Reference)
3. Ensure 100% upstream purity of NousResearch/hermes-agent (`git status --porcelain` is empty).
4. Assert zero bespoke wrapper scripts in `scripts/` and `plugins/`.
5. Enforce discrete NVIDIA RTX 3050 Laptop GPU VRAM ceiling <= 5,800.0 MiB under 64K/128K context.
