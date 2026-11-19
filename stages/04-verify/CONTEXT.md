# Stage 04 Contract: Deterministic POSIX & CDP Verification (04-verify)

## Inputs

| Source | File/Location | Section/Scope | Why |
| :--- | :--- | :--- | :--- |
| Implementation Receipt | stages/03-implement/output/implementation_receipt.json | All | Verified atomic WebGL2 modules |
| Deterministic Contract Gate | benchmarks/gauntlet_c_aquarium/contract.sh | All | 4-gate verification suite |
| Hardware Ceilings | _config/hardware_ceilings.md | All | RTX 3050 <= 5800.0 MiB discrete memory limit |

## Process Steps

1. Run headless Chromium via Playwright executing `stages/04-verify/run_browser_eval.py`.
2. Harvesters record `window.__AQUARIUM_TELEMETRY__` to `stages/04-verify/output/cdp_telemetry.json`:
   - Assert `fps >= 55.0`
   - Assert `fishCount >= 20`
   - Assert `causticsActive == true`
   - Assert `consoleErrors == 0`
3. Execute `bash benchmarks/gauntlet_c_aquarium/contract.sh` across all 4 deterministic gates:
   - Gate 1: Atomic line limit (< 60 lines per module).
   - Gate 2: Caustics GLSL AST tokens (`dFdx`, `dFdy`, `refract`).
   - Gate 3: Headless CDP telemetry verification.
   - Gate 4: Discrete RTX 3050 VRAM boundary (<= 5,800.0 MiB).
4. Verify stage structure using `~/.hermes/skills/icm/icm-stage-compiler/scripts/verify_stage.py stages/04-verify`.

## Outputs

| Artifact | Target Path | Verification |
| :--- | :--- | :--- |
| CDP Telemetry | stages/04-verify/output/cdp_telemetry.json | contract.sh |
| Verification Summary | stages/04-verify/output/verification_summary.md | verify_stage.py |
