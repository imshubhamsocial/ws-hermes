# Layer 3 Substrate Invariants: System Integrity & Purity

## 1. Upstream Substrate Purity (Rule 9)
The core runtime repository at `/var/home/imshubhamsocial/.hermes/hermes-agent` is strictly immutable.
Never edit, rename, stage, or commit files within the upstream submodule.
All user customizations, skills, profiles, and tools must reside exclusively in user overlay paths (`~/.hermes/`) or workspace directories.

## 2. Zero Fake Green
Never hardcode mock responses, bypass test assertions, or forge exit code 0.
If an external physical daemon, GPU context, or DOM handle is unavailable, report the failure directly in `output/` and halt execution.

## 3. Empirical Grounding
Ground all assertions in inspectable artifacts and deterministic telemetry receipts.
Verify visual state and DOM trees using real CDP headless browser evaluation and accessibility trees before issuing state-mutating actions.

## 4. One Fact, One Home
Never duplicate invariant definitions across multiple files.
Maintain one canonical source file for each rule and link to it from stage contracts and documentation.

## 5. Read Before Edit (Rule 5)
Always invoke `read_file` on a target file in the active conversation session before proposing or applying modifications.
