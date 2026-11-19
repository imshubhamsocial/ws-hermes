# The 10 Non-Negotiable Compiler Rules

**Standard**: Interpretable Context Methodology (ICM) Invariants  
**Enforcement**: [AGENTS.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/AGENTS.md) and [.hermes/tools/icm/hermes_icm_validator.py](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/.hermes/tools/icm/hermes_icm_validator.py)  
**Language Standard**: ASD-STE100  
**Parent Index**: [docs/architecture/README.md](file:///var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/docs/architecture/README.md)

---

## The 10 Invariants

### Rule 1: One Stage, One Job
* **Rule**: Execute only the contract inside the target folder's `CONTEXT.md`.
* **Rationale**: Prevents multi-task hallucinations and keeps the agent focused on an atomic deliverable.

### Rule 2: Bounded Context (2,000 to 8,000 Tokens)
* **Rule**: Load only the exact file paths and sections listed in the stage's `Inputs`.
* **Rationale**: Minimizes prompt bloat, lowers TTFT, and guarantees high attention focus.

### Rule 3: One Fact, One Home
* **Rule**: Never duplicate rules from `.hermes/_config/invariants.md`. Link to them.
* **Rationale**: Eliminates rule drift and ensures a single canonical ground truth.

### Rule 4: Docs Over Outputs
* **Rule**: Learn patterns from Layer 3 (`.hermes/_config/`, `shared/`), never prior outputs.
* **Rationale**: Prevents synthetic error accumulation from previous faulty runs.

### Rule 5: Read Before Edit
* **Rule**: Always call `read_file` on a target file in the current session before editing it.
* **Rationale**: Guarantees string replacement tools receive exact character matches and line numbers.

### Rule 6: Atomic Scripts Under 60 Lines
* **Rule**: Author modular Python and shell scripts strictly under 60 physical lines ($\le 59$ lines).
* **Rationale**: Enforces single-responsibility modularity and prevents unmaintainable monolithic scripts.

### Rule 7: Browser Verification
* **Rule**: Use Playwright (`connect_over_cdp` or headless Chromium) to verify 0 runtime errors.
* **Rationale**: Verifies that graphical, DOM, and WebGL outputs render without console errors.

### Rule 8: Fresh Context Auditing
* **Rule**: Never grade your own output in the generating context; use `_tools/` check gates.
* **Rationale**: Eliminates self-grading bias and guarantees objective contract verification.

### Rule 9: Substrate Purity
* **Rule**: Never modify files inside upstream hermes-agent repository (`~/.hermes/hermes-agent`).
* **Rationale**: Ensures seamless upstream updates without merge conflicts or broken runtime core files.

### Rule 10: Mandatory ASD-STE100 & Google Docs Safety
* **Rule**: Use Simplified Technical English ($\le 25$ words per sentence) and even fence/dollar parity.
* **Rationale**: Maximizes clarity, avoids ambiguity, and prevents rendering glitches in markdown viewers.
