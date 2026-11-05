# Root Operational Invariants (Layer 2)

> Architectural Standard: Jake Van Clief's ICM (arXiv:2603.16021)
> Strict Line Budget: <= 80 lines

1. **Hardware VRAM Hard Ceiling**:
   - Active GPU memory on discrete NVIDIA RTX 3050 Laptop GPU (6,144 MiB physical GDDR6) must NEVER exceed 5,800.0 MiB under any workload.
   - Enforce via continuous NVML polling (`nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits`).

2. **Upstream Substrate Purity**:
   - `.hermes/hermes-agent` submodule must remain 100% pure and untouched (`git status --porcelain` returns 0 lines).
   - Zero monkey-patches, monkey-patching decorators, or vendor overrides.

3. **Zero Bespoke Wrappers Invariant**:
   - Never author bespoke Python wrappers or custom plugins in `scripts/` or `plugins/`.
   - All customizations must be achieved via declarative `config.yaml` or portable skills in `~/.hermes/skills/`.

4. **Working Context Window Discipline**:
   - Maintain active conversation working context strictly between 2,000 and 8,000 tokens per stage.
   - Never run unbounded monolithic multi-turn sessions that exceed 12 turns.
