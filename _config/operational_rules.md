# Root Operational Rules (Layer 2)

> Architectural Standard: Jake Van Clief's ICM (arXiv:2603.16021)
> Strict Line Budget: <= 120 lines

1. **Deterministic Sequential Stage Execution**:
   - Every complex engineering requirement must traverse the 4-stage pipeline sequentially:
     `01-spec` -> `02-plan` -> `03-execute` -> `04-verify`.
   - Never skip directly to execution without an approved specification and signed contract.

2. **Contract-First Verification**:
   - Each operational directory must contain a deterministic `contract.sh` with `set -euo pipefail`.
   - All tests must run headlessly and verify syntax, AST structure, and exit code 0.

3. **Two-Strike Tabu Rule**:
   - If an agent generates code that fails verification twice, it must revert to the last green checkpoint and try an alternative architecture.

4. **Normalized Output Rule**:
   - Autonomous verification evaluations must emit exact ground-truth values without conversational conversational prefixes.

5. **Tool Call Protocol**:
   - All tool calls must be emitted in structured JSON format; plain text leaks are strictly forbidden.
