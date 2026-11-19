# Layer 3 ICM Operational Rules: Execution Lifecycles

## 1. Pre-Coding Socratic Spec Alignment
Before writing production code, run the stateless Elephant-Goldfish Model (EGM) gate (`_tools/egm_goldfish_gate.py`).
Verify zero blocker findings across Comprehension, Design Critic, and Readiness lenses.

## 2. Clean Session Resets
Execute multi-stage workflows in clean sessions using `/new --yes` or `hermes chat --oneshot -q`.
Wipe session context between stages to guarantee stateless execution and prevent context rot.

## 3. Fresh Context Auditing (Rule 8)
Never evaluate your own output within the generating conversation context.
Always evaluate artifacts through deterministic automated test runners (`contract.sh`, `verify_stage.py`).

## 4. Docs Over Outputs (Rule 4)
Learn domain patterns and invariants from Layer 3 documentation (`.hermes/rules/`, `shared/`), never from prior session conversational outputs.
