---
name: icm-stage-compiler
description: Use when you compile, execute, or verify 5-layer ICM stage contracts and atomic scripts.
version: 1.0.0
platforms: [linux]
metadata:
  author: "Hermes Harness Team"
  tags: [icm, compiler, verification, architecture, stage-runner]
  category: icm
  requires_toolsets: [terminal]
---

# ICM Stage Compiler Skill

## Purpose

The ICM Stage Compiler provides deterministic compilation, execution, and verification of numbered stage directories (stages/01-spec through stages/04-verify). It enforces the 5-layer Interpretable Context Methodology (ICM), atomic script line limits (<60 lines), and bounded context budgets (2,000–8,000 tokens).

## When to Use

Use this skill when you need to:
- Validate workspace topology and stage contracts against the cold 8-point Walk Test.
- Execute an ICM stage with llama-server KV-cache slot isolation and automatic checkpoint generation.
- Verify stage deliverables against deterministic POSIX assertions before inter-stage handoff.
- Distill verified multi-step workflows into reusable 5-layer skills.

## Prerequisites

- Linux operating system (Fedora Kinoite / Silverblue or containerized Distrobox).
- Python 3.11+ standard library.
- Local inference server active at `http://127.0.0.1:8138` (for KV cache slot reset).

## Available Scripts

| Script | Purpose | Arguments |
| :--- | :--- | :--- |
| `scripts/hermes_icm_validator.py` | Runs the cold 8-point ICM Walk Test across workspace contracts | None (discovers workspace root automatically) |
| `scripts/hermes_stage_runner.py` | Executes an isolated stage with KV-slot reset and check logging | `--stage-dir <path> [--gate-mode autonomous] [--verify-only]` |
| `scripts/verify_stage.py` | Verifies stage contract sections and enforces the <60 line script limit | `<stage_directory>` |

## Procedure

1. Verify that the target stage folder contains `CONTEXT.md`, `references/`, and `output/`.
2. Confirm `CONTEXT.md` contains explicit `## Inputs`, `## Process Steps`, and `## Outputs` sections.
3. Load strictly the declared inputs within the 2,000–8,000 token budget.
4. Synthesize stage deliverables into `output/`, keeping every script strictly under 60 lines.
5. Execute the stage runner or validator script:
   ```bash
   python3 .hermes/skills/icm/icm-stage-compiler/scripts/hermes_stage_runner.py --stage-dir <stage_dir> --verify-only
   python3 .hermes/skills/icm/icm-stage-compiler/scripts/hermes_icm_validator.py
   ```
6. Wipe session context via `/new --yes` before entering the next numbered stage.

## Examples

Execute via CLI or `run_script`:
```bash
# Execute Walk Test via terminal or run_script("scripts/hermes_icm_validator.py")
python3 .hermes/skills/icm/icm-stage-compiler/scripts/hermes_icm_validator.py

# Verify stage contract via terminal or run_script("scripts/verify_stage.py", "benchmarks/gauntlet_b_splatbox/stages/01-probe")
python3 .hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py benchmarks/gauntlet_b_splatbox/stages/01-probe

# Execute stage runner via terminal or run_script("scripts/hermes_stage_runner.py", "--stage-dir benchmarks/gauntlet_b_splatbox/stages/01-probe")
python3 .hermes/skills/icm/icm-stage-compiler/scripts/hermes_stage_runner.py --stage-dir benchmarks/gauntlet_b_splatbox/stages/01-probe --gate-mode autonomous
```

## Limitations

- Enforces single-stage isolation; never combines multiple stages in one unsegmented turn.
- Hard script line ceiling: rejects any `.py`, `.sh`, or `.js` file with 60 or more lines.
- Does not run cloud APIs; 100% local execution only.

## Troubleshooting

| Error Symptom | Root Cause | Solution |
| :--- | :--- | :--- |
| `ATOMIC_LIMIT_EXCEEDED` | Script contains >= 60 physical lines | Refactor script into modular helper functions under 60 lines |
| `MISSING_SECTION` | Stage `CONTEXT.md` lacks Inputs, Process, or Outputs | Add standard markdown headers to `CONTEXT.md` |
| `KV_SLOT_FAILED` | Local inference server unreachable | Start `llama-server.service` on port 8138 |

## Layer Mapping Reference

| ICM Layer | Artifact | Max Token Budget |
| :--- | :--- | :--- |
| Layer 0 | IDENTITY.md / SOUL.md | 800 tokens |
| Layer 1 | Root CONTEXT.md | 300 tokens |
| Layer 2 | Stage CONTEXT.md | 500 tokens |
| Layer 3 | _config/ & references/ | 2,000 tokens |
| Layer 4 | Stage output/ artifacts | Dynamic (Total <= 8,000) |
