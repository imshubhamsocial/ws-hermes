---
name: icm-stage-compiler
description: Compile and verify 5-layer ICM stage contracts and scripts
version: 1.0.0
platforms: [linux]
metadata:
  hermes:
    tags: [icm, compiler, verification, architecture]
    category: icm
    requires_toolsets: [terminal]
---

# ICM Stage Compiler Skill

## When to Use

Invoke this skill when scaffolding, executing, or auditing a numbered ICM stage folder (stages/01-spec through stages/04-verify) or distilling a completed workflow via /learn.

## Procedure

> 1. Verify that the active stage folder contains CONTEXT.md, references/, and output/.  
> 2. Confirm CONTEXT.md declares explicit Inputs, Process Steps, and Outputs tables.  
> 3. Load strictly the files and line ranges specified in the stage Inputs table.  
> 4. Synthesize stage outputs into output/, keeping every script strictly under 60 lines.  
> 5. Run the deterministic verification script before concluding the stage:
>    python3 ~/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py stages/01-spec  
> 6. Wipe session context via /new --yes before entering the next numbered stage.

## Pitfalls

* **Monolithic Context Bleed**: Never read upstream stages earlier than N-1.  
* **Line Ceiling Violation**: Any .py, .sh, or .js file with 60 or more lines fails the gate.  
* **Unverified Goal Loop**: Never run /goal without first attaching a deterministic /goal gate add.  
* **Substrate Mutation**: Never write files inside ~/.hermes/hermes-agent.

## Verification

Run the bundled unit test suite and static verifier to confirm zero defects:

> 1. python3 ~/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py stages/01-spec  
> 2. python3 -m unittest ~/.hermes/skills/icm/icm-stage-compiler/tests/test_skill.py  
> 3. skillevaluator quality-check ~/.hermes/skills/icm/icm-stage-compiler

## Layer Mapping Reference

| ICM Layer | Artifact | Max Token Budget |
| :---- | :---- | :---- |
| Layer 0 | IDENTITY.md / SOUL.md | 800 tokens |
| Layer 1 | Root CONTEXT.md | 300 tokens |
| Layer 2 | Stage CONTEXT.md | 500 tokens |
| Layer 3 | _config/ & references/ | 2,000 tokens |
| Layer 4 | Stage output/ artifacts | Dynamic (Total <= 8,000) |
