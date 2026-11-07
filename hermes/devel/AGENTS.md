# Layer 0: Hermes Agent OS Development Operating Protocol

## 1. Identity & Scope

You operate inside Hermes Agent OS Development (`hermes/devel/`).
This workspace contains the 3-stage sequential compiler pipeline, Frontier Gauntlets A-C, and sealed phase verification ledger.

## 2. Directory Map

* `CONTEXT.md`: Development task router (< 80 lines).
* `stages/`: 3-stage sequential compiler pipeline (01-probe/, 02-controller/, 03-execute/).
* `benchmarks/`: Frontier Gauntlets A (3D FPS Netcode), B (Splatbox CV), and C (Aquarium WebGL).
* `phases/`: Sealed verification registry and master ledger (Phases 1 to 58).
* `docs/`: Historical GDR research corpus (GDR30 to GDR37).
* `../../_config/`: Root system invariants, hardware ceilings, and port registries.
* `../../_tools/`: Root deterministic Python/POSIX validators and stage runners.
* `../../shared/`: Root cross-stage mathematical and vision schemas.

## 3. Project Directives

> 1. One Stage, One Job: Execute strictly through local stage CONTEXT.md contracts.
> 2. Bounded Context: Load only the inputs declared in the active stage contract.
> 3. Zero Cross-Talk: Never import execution code across independent testbeds.
> 4. Verification Check: Every stage must conclude at a verified check receipt (`output/check.md`).
