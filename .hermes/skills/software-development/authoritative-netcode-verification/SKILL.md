---
name: authoritative-netcode-verification
description: "Verify authoritative, real-time WebSocket game servers."
---
# Procedure: Authoritative Netcode Verification
1. **Context Load**: Read `CONTEXT.md` and `invariants.md` to load operational bounds and contract requirements.
2. **Initial Verification**: Execute `bash ./contract.sh` to run deterministic AST checks, line-cap assertions, live 2-client WebSocket handshake on Port 8080, and NVML VRAM ceiling check (<= 5800 MiB).
3. **Failure Handling**: If `contract.sh` exits with code != 0, identify the specific failing assertion/contract violation (e.g., missing required JSON fields).
4. **Surgical Fix**: Apply a surgical patch (Karpathy U12 limit) to the specific failing file under the Two-Strike Tabu rule.
5. **Iterative Verification**: Re-run `bash ./contract.sh` until it exits with code 0.
6. **Seal**: Write the final signed verification receipt to `output/status.json` with `"status": "VERIFIED_AND_SEALED"`, `"contract_exit_code": 0`, and live VRAM telemetry.

# Pitfalls
* **Contract Completeness**: Never assume contract fields are present; always verify against `invariants.md` and `CONTEXT.md` before assuming implementation completeness.
* **Fix Strategy**: Only use surgical patches (Karpathy U12 limit) for causal fixes; avoid large refactors.
