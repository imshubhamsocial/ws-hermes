# Stage Invariants (Layer 2)

> Architectural Standard: Jake Van Clief's ICM (arXiv:2603.16021)
> Line Cap: <= 80 lines

1. **Sub-8K Context Ceiling**: Active working context must remain strictly between 2,000 and 8,000 tokens.
2. **Deterministic Output**: Stage outputs must be written as structured JSON/Markdown artifacts inside `output/`.
3. **Hardware Realism**: Memory consumption on discrete NVIDIA RTX 3050 must not exceed 5,800.0 MiB.
