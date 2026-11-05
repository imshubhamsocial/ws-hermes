# Layer 3: ICM Core Conventions and Invariants

## The 15 Conventions
1. Stage Contracts: Every stage has Inputs, Process, Outputs, and Check.
2. Stage Handoffs: Output folders connect stages directly.
3. One-Way References: Dependencies flow in one direction only.
4. Selective Section Routing: Load only needed sections from reference files.
5. Canonical Sources: Every fact has one authoritative home.
6. Specs Are Contracts: Specs state WHAT and WHEN; build defines HOW.
7. Checkpoints: Pause execution for human review at major milestones.
8. Stage Audits: Automated verification before saving final outputs.
9. Value Validation: Explicit schema and type validation.
10. Docs Over Outputs: Learn patterns from Layer 3 references, never previous outputs.
11. Questionnaire Design: Fast, all-at-once onboarding configuration.
12. Shared Constants: Centralized constants prevent scattered magic values.
13. Strict Line Limits: CONTEXT.md < 80 lines; references < 200 lines.
14. Clean Output State: Do not commit generated run artifacts.
15. System-Level Setup: Configure the production factory once.
