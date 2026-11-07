---
name: icm-stage-compiler
description: Enforces Jake Van Clief's Interpretable Context Methodology (ICM) 5-layer stage compilation, selective line-range routing, and under-60-line modular code generation.
version: 1.0.0
platforms: [linux]
metadata:
  hermes:
    tags: [icm, architecture, compiler, van-clief]
    category: architecture
    requires_toolsets: [terminal, file]
---
# ICM Stage Compiler Skill

## When to Use
Invoke `/icm-stage-compiler` at the start of any benchmark stage execution or workspace scaffolding pass.

## Procedure
1. Read `CONTEXT.md` in the current working directory (must be under 80 lines).
2. Parse the `Inputs` table. Use `read_file` with exact `offset` and `limit` parameters matching the `Lines` column to load only the specified sections of Layer 3 blueprints and Layer 4 upstream outputs.
3. Execute the `Process` steps sequentially. Write modular scripts (under 60 lines each) to `output/`.
4. Run the command in `Checkpoints & Audits`. Do not proceed or claim success unless exit code is `0` and `output/` artifacts are non-empty.

## Pitfalls
- Never load files outside the `Inputs` table.
- Never patch a broken script more than once; re-compile the under-60-line module cleanly from the Layer 3 Code Blueprint.

## Verification
Confirm that all files listed in the `Outputs` table exist on disk and pass the stage audit command.
