# Benchmark Invariants (Layer 2)

> Line Cap: <= 80 lines

1. **Normalized Output**: Evaluate cold; emit normalized final integer/string without conversational prefixes.
2. **Context Horizon**: Do not exceed 8,000 tokens per evaluation turn.
3. **Hardware Ceiling**: GPU VRAM <= 5,800.0 MiB on discrete RTX 3050.
