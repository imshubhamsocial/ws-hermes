# GDR37 Master Release: Autonomous ICM Repository Organization & Verification Blueprint

> **Release Package**: GDR37  
> **Date**: November 6, 2026  
> **Substrate Target**: Hermes Agent OS on Fedora Kinoite 44 (x86_64, rpm-ostree)  
> **Inference Substrate**: Gemma 4 Exact (`gemma-4-E4B-it-q4_0-exact.gguf` + MTP Speculative Drafter)  
> **Context Window Enforced**: 131,072 tokens (128K context, Google TurboQuant Q4_0 KV Cache)  
> **Hardware Status**: Discrete NVIDIA GeForce RTX 3050 Laptop GPU (6,144 MiB GDDR6, VRAM active at 4,997 MiB, 861 MiB free headroom)  
> **Status**: Phase 58 Verified & Sealed | 5-Layer ICM Architecture Deployed | Gauntlets A, B, C Operational | Native Git Repository Operational  

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

## 2. Release Documents Index (GDR37)

| Document Number | Document Title | Path | Description |
| :--- | :--- | :--- | :--- |
| **Document 01** | GDR35 Input Files, Research Context, and Issues | `docs/research/GDR37/01_doc1_gdr35_original_inputs_and_issues.md` | Full raw contents of GDR35 inputs and issues identified during research. |
| **Document 02** | GDR36 Certification Blueprint & Forensic Analysis | `docs/research/GDR37/02_doc2_gdr36_certification_blueprint_and_forensic_analysis.md` | Full synthesis of GDR36 certification blueprint and verified analytical findings. |
| **Document 03** | Physical Implementation, Telemetry, and Audit Report | `docs/research/GDR37/03_doc3_physical_implementation_and_verification_report.md` | Implementation records, Gauntlets A/B/C repairs, Gemma 4 daemon flags, and test receipts. |
| **Document 04** | Jake Van Clief ICM Specifications & Tooling | `docs/research/GDR37/04_doc4_jake_icm_commands_and_workspace_reorganization_spec.md` | ICM tool commands, Keep-Out Inventory, 4-category triage, and non-breaking migration rules. |
| **Document 05** | Master Consultation Directive for Gemini Argon | `docs/research/GDR37/05_master_argon_consultation_prompt.md` | Executive prompt for Gemini Argon with exhaustive pre-migration safety directives. |
| **Inventory** | Chezmoi Migration Inventory | `docs/research/GDR37/CHEZMOI_MIGRATION_INVENTORY.md` | Exhaustive catalog of all 1,288 files tracked prior to native Git migration. |

---

## 3. Historical Research Corpus Ingested (`docs/research/`)

| Historical Package | Repository Path | Research Purpose |
| :--- | :--- | :--- |
| **GDR30** | `docs/research/GDR30 - Golden Benchmark State (GAIA, TAU-2)/` | Golden benchmark state and baseline evaluation evidence. |
| **GDR31** | `docs/research/GDR31/` | Substrate synchronization and early harness contracts. |
| **GDR32** | `docs/research/GDR32/` | Telemetry harness and user systemd integration. |
| **GDR33** | `docs/research/GDR33/` | Gauntlet A netcode synchronization and jitter mitigations. |
| **GDR34** | `docs/research/GDR34/` | Gauntlet B OpenCV tracking and visual servoing. |
| **GDR35** | `docs/research/GDR35/` | Gauntlet C aquarium shader material diagnostics. |
| **GDR36** | `docs/research/GDR36/` | Certification roadmap and 4-tier skill precedence blueprint. |
| **GDR37** | `docs/research/GDR37/` | Repository reorganization and native Git migration specification. |

---

## 4. Mission Objectives for Lead Architect Argon

1. **Verify Implementation**: Review the physical deployment of Phase 58 and the 5-layer ICM structure.
2. **Execute Non-Breaking Safety Audit**: Enforce the Keep-Out Inventory to protect daemons (Ports 8138, 1933, 8642, 9222), upstream purity (`.hermes/hermes-agent`), and the 58 sealed phases.
3. **Classify All Repository Files**: Apply the 4-Category Triage framework (Retain, Consolidate, Archive, Prune) to all 1,288 cataloged files.
4. **Deliver Structured Migration Table**: Provide an actionable mapping table (`Source -> Destination | Rationale | Exact Git Command | Verification | Rollback`).
5. **Output Standard**: Deliver instructions in strict ASD-STE100 format with zero Google Docs export errors.
