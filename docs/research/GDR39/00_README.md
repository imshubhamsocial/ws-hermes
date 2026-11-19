# GDR39 Master Release: ICM Pedagogy, Context Rot Auditing, Isolated Profile Bots, and Gauntlet C Simulation Architecture

> **Release Package**: GDR39  
> **Date**: November 15, 2026  
> **Substrate Target**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Substrate**: Dual-Track (Google Gemma 4 Exact 4B + NVIDIA Nemotron Dory 1.0 Looped 4B)  
> **Context Window Enforced**: 131,072 to 262,144 tokens (128K–256K, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Status**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB physical GDDR6, ceiling $\le 5,800.0\text{ MiB}$); 100% compute dedication (Wayland compositor on Intel iGPU / Disp.A: Off, 25 MiB idle); Host system on CPU & 16 GB System RAM  
> **Execution Status**: Gauntlet B (Splatbox 3D CV) 100% Certified (Score: 1,149, 220 Frames, 0 Repeat Wall Shots) | Advancing to Gauntlet C (Aquarium 3D WebGL) & ICM Factory Automation  

---

## 1. Master GitHub Repositories (Raw Endpoints)

The table below provides direct raw HTTPS endpoints for headless web crawlers and Google Deep Research ingestion:

| Repository Role | Canonical Raw Base URL | Target Branch | Local Workspace Directory |
| :--- | :--- | :--- | :--- |
| **Hermes Workspace & Code (ws-hermes)** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/` | `master` | `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes` |
| **Hermes Evaluation & Tests** | `https://raw.githubusercontent.com/imshubhamsocial/hermes-tests/main/` | `main` | `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/benchmarks` / `.../logs` |
| **Upstream Hermes Substrate** | `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/` | `main` | `~/.hermes/hermes-agent` (100% clean) |
| **Jake Van Clief ICM Repo** | `https://raw.githubusercontent.com/RinDig/Interpretable-Context-Methodology/main/` | `main` | `~/.cache/icm-datasets/Interpretable-Context-Methodology` |
| **ICM Template Repository** | `https://raw.githubusercontent.com/ktncodes/icm-template/main/` | `main` | `~/.cache/icm-datasets/icm-template` |
| **ICM Architect Skill** | `https://raw.githubusercontent.com/RinDig/icm-architect/main/` | `main` | `~/.agents/skills/icm-architect` |
| **Content Agent Routing** | `https://raw.githubusercontent.com/RinDig/Content-Agent-Routing-Promptbase/main/` | `main` | `~/.cache/icm-datasets/Content-Agent-Routing-Promptbase` |
| **Clief Notes Foundations** | `https://raw.githubusercontent.com/donroy26/Clief-Notes-Foundations-Tutor/main/` | `main` | `~/.cache/icm-datasets/Clief-Notes-Foundations-Tutor` |

---

## 2. Core Repository Files (Raw Ingestion Endpoints)

| File Purpose | Canonical Raw URL | Local Workspace Path |
| :--- | :--- | :--- |
| **Layer 0 Operating Protocol** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/AGENTS.md` | `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/AGENTS.md` |
| **Layer 1 Umbrella Router** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/CONTEXT.md` | `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/CONTEXT.md` |
| **Devel Layer 0 Protocol** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/AGENTS.md` | `hermes/devel/AGENTS.md` |
| **Devel Layer 1 Router** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/CONTEXT.md` | `hermes/devel/CONTEXT.md` |
| **Hermes Soul & Epistemics** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/.hermes/SOUL.md` | `.hermes/SOUL.md` |
| **Gauntlet B Contract Router** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/CONTEXT.md` | `hermes/devel/benchmarks/gauntlet_b_splatbox/CONTEXT.md` |
| **Gauntlet B Audit Gate** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/contract.sh` | `hermes/devel/benchmarks/gauntlet_b_splatbox/contract.sh` |
| **Gauntlet B Invariants** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/invariants.md` | `hermes/devel/benchmarks/gauntlet_b_splatbox/invariants.md` |
| **Gauntlet B Domain Rules** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/rules.md` | `hermes/devel/benchmarks/gauntlet_b_splatbox/rules.md` |
| **Stage 1 Probe Contract** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/stages/01-probe/CONTEXT.md` | `stages/01-probe/CONTEXT.md` |
| **Stage 2 Controller Contract**| `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/stages/02-controller/CONTEXT.md` | `stages/02-controller/CONTEXT.md` |
| **Stage 3 Execute Contract** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/stages/03-execute/CONTEXT.md` | `stages/03-execute/CONTEXT.md` |
| **Certified Match Telemetry** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/output/telemetry.json` | `output/telemetry.json` |
| **Ballistic Statistics** | `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/output/gun_stats.json` | `output/gun_stats.json` |
| **Tracker Verification Receipt**| `https://raw.githubusercontent.com/imshubhamsocial/ws-hermes/master/hermes/devel/benchmarks/gauntlet_b_splatbox/output/tracker_verified.json` | `output/tracker_verified.json` |

---

## 3. Release Documents Index (GDR39)

| Document Number | Document Title | Path | Description |
| :--- | :--- | :--- | :--- |
| **Briefing** | Master GDR39 Consultation Brief | `docs/research/GDR39/01_master_gdr39_brief.md` | Executive consultation briefing for Google Deep Research / Lead Architect Argon on ICM pedagogy, context rot auditing, isolated profile bots, and Gauntlet C simulation. |
| **Document 01** | Gauntlet B ICM Execution Review & Architectural Retrospective | `docs/research/GDR39/02_doc1_icm_execution_review_gauntlet_b.md` | Complete architectural review of Gauntlet B from an ICM perspective: contract isolation, bounded token contexts, zero fake green auditing, and state machine validation. |
| **Document 02** | ICM Pedagogy, Auditing Tools, Isolated Bots & Gauntlet C Specification | `docs/research/GDR39/03_doc2_icm_pedagogy_tools_bots_spec.md` | Comprehensive specifications across the 5 Golden Directives: curriculum for self-learning ICM, context rot mitigation (NVIDIA SkillEvaluator, Google AQUA, Auto Ontology), Hermes bot blueprints, Gauntlet C tutorial, loop orchestration, and Socratic planning. |
| **Master Prompt** | Master Consultation Prompt for Google Deep Research | `docs/research/GDR39/04_master_gdr39_prompt.md` | Final, copy-pasteable prompt formatted for Google Deep Research / Gemini Argon with High Thinking enabled. |

---

## 4. Historical Research Corpus Ingested (`docs/research/`)

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
| **GDR39** | `docs/research/GDR39/` | ICM self-learning pedagogy, context rot auditing, isolated profile bots, Gauntlet C simulation factory, and Socratic planning loops. |

---

## 5. The Eight Golden Research Directives for Lead Architect Argon

1. **Golden Directive 1 (ICM Pedagogy, Official Tooling & Context Rot Mitigation)**:
   Author a comprehensive, step-by-step educational plan ("TEACH ME") enabling the user to master ICM independently from scratch. Detail how to scaffold fresh projects, repair degraded states, and migrate raw third-party repositories into compliant 5-layer ICM architectures. Catalog official ICM binaries, templates, skills, and promptbases. Research context rot (markdown and folder degradation after two or more weeks) and evaluate **NVIDIA SkillEvaluator**, **Google AQUA**, and **NVIDIA Auto Ontology** for automated context auditing, duplicate instruction pruning, and taxonomy preservation.
2. **Golden Directive 2 (Hermes Bots & Isolated Profiles Blueprint)**:
   Evaluate establishing dedicated Hermes bots utilizing isolated profiles (`--profile`) to manage ICM operations cleanly. Provide complete architectural blueprints (folder structures, configuration schemas, system prompts, and tool sets) for specialized bots: Scaffolder, Migrator, and Auditor.
3. **Golden Directive 3 (Comprehensive Gauntlet C Aquarium Simulation Tutorial)**:
   Provide an end-to-end guided learning tutorial for Frontier Gauntlet C (3D WebGL / GPGPU Aquarium Simulation). Teach the user how to translate high-level visual goals into intermediate ICM stages (GPGPU wave PDE ping-pong, differential caustics, soft shadows, buoyancy physics, and boid flocking) matching simulations produced by Claude 3.5 Sonnet and Opus.
4. **Golden Directive 4 (Hermes Slash Command Orchestration & Professional Prompting)**:
   Examine Hermes native commands (`/goal`, `/loop`, `/new`, `/clear`, `/compact`). Design an orchestration model that uses these commands to advance through ICM stages while strictly preserving Jake Van Clief's "one task, one clean session" rule. Train the user on authoring concise, professional prompts that steer autonomous execution effectively without micromanagement or spoon-feeding.
5. **Golden Directive 5 (Socratic Sifting & Pre-Coding Alignment — Google Elephant & Fish Paradigm)**:
   Analyze the Google "Elephant & Fish" interactive interview model (adversarial requirements deconstruction and pre-coding plan refinement). Design its integration into the ICM lifecycle as an upfront Socratic alignment gate or dedicated planning bot to eliminate architectural bugs before code generation.
6. **Golden Directive 6 (Substrate Harmonization, Self-Learned Skills & Direct Auditing of .hermes)**:
   Reconcile and absorb the development environment (`hermes/devel/`) into native upstream Hermes directories (`~/.hermes/skills/`, `~/.hermes/rules/`, `~/.hermes/tools/`) structured in strict ICM style. Specify how native skills incorporate internal routing and atomic Python helper scripts (`scripts/`). Ensure NVIDIA SkillEvaluator and Google AQUA can audit native `~/.hermes/` directories directly. Standardize the ICM Self-Learned Skill Protocol so autonomous skill acquisition via `/learn` produces upstream-compatible skills with deterministic test gates. Update `.hermes/SOUL.md` to govern autonomous skill distillation.
7. **Golden Directive 7 (Universal Inter-Agent CONTEXT.md Specification)**:
   Author a comprehensive master `CONTEXT.md` designed to be shared with any new or external autonomous agent (subagents, swarm workers, Claude, ChatGPT, Gemini, Cursor). Provide complete, instantaneous onboarding covering host infrastructure, dedicated GPU ceilings ($\le 5,800.0\text{ MiB}$), port maps, the 10 Non-Negotiable Compiler Rules, workspace task routing, canonical research references (GDR30–GDR39), and inter-agent contract protocols.
8. **Golden Directive 8 (Cloudflare Decision Models for High-Speed ICM Routing & Verification)**:
   Research the integration of Cloudflare decision models (such as Cloudflare Workers AI classification, routing, and fast decision micro-models) into the ICM architecture. Evaluate replacing slow, token-heavy autoregressive text generation with microsecond decision and choice models for discrete operations: task routing in `CONTEXT.md`, stage verification check gates, and categorical branch choices. Detail how to integrate these decision endpoints into ICM stages, CLI tools, and automated compiler workflows.

---

## 6. Executive Verification & Google Docs Safety Standard

All documents in this release package strictly adhere to the following safety criteria:
* **ASD-STE100 Compliance**: Formatted in Simplified Technical English with active voice, concise sentences, and clear technical terminology.
* **Even Code Fence Count**: Every code fence is paired (`count % 2 == 0`).
* **Even Math Dollar Sign Parity**: Strict parity for inline and block LaTeX notations (`count % 2 == 0`).
* **Single-Line Tables**: Matching column counts per row with zero multi-line cell breaks.
* **Direct Raw Endpoints**: Headless crawlers and LLM research engines can ingest all linked files without JavaScript rendering barriers.
