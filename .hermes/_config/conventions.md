# Layer 3 ICM Conventions: Code & Communication Standards

## 1. Atomic Script Ceiling (Rule 6)
Every authored script (`.py`, `.sh`, `.js`) must strictly contain fewer than 60 lines (maximum 59 lines).
Never create monoliths; decompose execution logic into modular, single-responsibility atomic scripts.

## 2. ASD-STE100 Prose Discipline (Rule 10)
Communicate technical reports, plans, and summaries in Simplified Technical English (ASD-STE100).
Enforce short declarative sentences, active verbs, and unambiguous terminology.

## 3. Bounded Context Budget (Rule 2)
Keep prompt context strictly bounded between 2,000 and 8,000 tokens per stage invocation.
Load only explicitly declared inputs specified in the stage's `CONTEXT.md`.

## 4. One Stage, One Job (Rule 1)
Each numbered stage folder (`stages/XX-*/`) must perform exactly one bounded task.
All stage outputs must be written directly to `stages/XX-*/output/`.

## 5. Mathematical Parity & Notation
Enforce even parity on code fences (triple backticks) and LaTeX math delimiters (dollar signs).
Prevent syntax parsing corruption in rendering environments and downstream tooling.
