# Layer 1: Universal Workspace Routing Table (ws-hermes)

## 1. Keyword Triggers

* setup: Run workspace onboarding or verify directory scaffolding via python3 .hermes/skills/icm/icm-stage-compiler/scripts/hermes_icm_validator.py.
* status: Inspect pipeline completion state across benchmarks/*/stages/*/output/check.md and phases/status_ledger.json.
* walk-test: Execute the cold 8-point ICM Walk Test via python3 .hermes/skills/icm/icm-stage-compiler/scripts/hermes_icm_validator.py.
* icm-sync: Audit relative links and regenerate context graphs via python3 -I .hermes/skills/icm/icm-architect/scripts/audit_links.py .
* quiesce: Stop llama-server.service and verify GPU VRAM <= 100 MiB via python3 .hermes/tools/icm/check_vram_limit.py --mode quiescent.

## 2. Intent-to-Directory Routing Matrix

| Task Intent | Target Profile Bot | Entry Contract (Layer 2) | Verification Gate |
| :--- | :--- | :--- | :--- |
| Pre-Coding Spec & Socratic Review | icm-planner | benchmarks/gauntlet_c_aquarium/stages/01-spec/CONTEXT.md | ~/.hermes/tools/icm/egm_goldfish_gate.py |
| Greenfield Workspace Scaffolding | icm-scaffolder | setup/questionnaire.md | ~/.hermes/tools/icm/icm_scaffolder.py |
| Brownfield AST Repo Migration | icm-migrator | stages/00-migrate/CONTEXT.md | ~/.hermes/tools/icm/icm_repo_migrator.py |
| Multi-Stage Pipeline Execution | default | ~/.hermes/tools/icm/run_multi_stage.sh | verify_stage.py |
| Benchmark Suite & Frontier Gauntlets | default | benchmarks/CONTEXT.md | Makefile |
| Substrate & Token Hygiene Audit | icm-auditor | ~/.hermes/tools/icm/ | ~/.hermes/tools/icm/audit_hermes_home.sh |
| Full Suite Walk & Gauntlets | default | CONTEXT.md | Makefile |
| Run Gauntlet B (Splatbox CV) | default | benchmarks/gauntlet_b_splatbox/CONTEXT.md | benchmarks/gauntlet_b_splatbox/contract.sh |

## 3. Canonical Directory Map

* Layer 0 (Global Rules): .hermes/SOUL.md and IDENTITY.md (~800 tokens)
* Layer 1 (Task Router): CONTEXT.md (this file, read once at session entry)
* Layer 2 (Stage Contracts): benchmarks/<suite>/stages/<nn>/CONTEXT.md (200–500 tokens)
* Layer 3 (The Factory): .hermes/_config/, shared/, references/, and ~/.hermes/skills/
* Layer 4 (Working Artifacts): benchmarks/ and benchmarks/<suite>/output/
* System Documentation: docs/ (docs/bots/, docs/skills/, docs/tools/, docs/architecture/)

## 4. Cross-Agent Adapter Mapping

| Agent Harness | Layer 0 Adapter | Skill Directory | Profile Isolation Path |
| :--- | :--- | :--- | :--- |
| Hermes Agent | .hermes/SOUL.md | ~/.hermes/skills/ | ~/.hermes/profiles/<name>/ |
| Claude Code | CLAUDE.md | .claude/skills/ | Subagent clean context |
| OpenAI Codex | AGENTS.md | ~/.agents/skills/ | Fresh subagent spawn |
| Gemini CLI | IDENTITY.md | ~/.gemini/skills/ | Workspace session scope |

## 5. Non-Negotiable Safety Gates

* Verify git status --porcelain in ~/.hermes/hermes-agent returns empty before and after runs.
* Verify wc -l is strictly under 60 lines for every generated Python, Bash, or JS file.
* Verify nvidia-smi memory.used stays at or below 5,800 MiB during all inference and WebGL2 runs.
* Verify goldfish_review_report.json reports status PASS before running Stage 03.
