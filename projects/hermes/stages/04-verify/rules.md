# Stage Operational Rules (Layer 2)

> Architectural Standard: Jake Van Clief's ICM (arXiv:2603.16021)
> Line Cap: <= 120 lines

1. **Clean Stage Handoff**: Read the input contract and previous stage output before mutating state.
2. **Zero Monolithic Bloat**: Never perform multi-stage work in a single turn; terminate after generating the stage artifact.
3. **Pre-Commit Verification**: Run local AST and linter checks (`ruff check`) before committing or closing the stage.
