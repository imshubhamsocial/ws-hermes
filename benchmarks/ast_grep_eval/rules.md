# Benchmark Rules (Layer 2)

> Line Cap: <= 120 lines

1. **Ground-Truth Preservation**: Compare results directly with ground-truth test vectors.
2. **Cold Determinism**: Run evaluations in isolated sessions without leaking prior turn state.
3. **Receipt Generation**: Write pass/fail telemetry to `output/status.json`.
