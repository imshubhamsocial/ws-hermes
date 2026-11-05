# Context
The continuous RSI dream loop (phase20-harness2) requires an 8-Point Walk Test, which depends on the `hermes_icm_validator.py` script. The previous run failed because this script was missing, leading to an UNVERIFIABLE status for ICM compliance checks.

# Invariants
The workspace must contain a functional `hermes_icm_validator.py` script located at `/var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/scripts/`. This script is mandatory for executing the ICM compliance check (Layers 0-4).

# Examples
Failure to find this script results in a critical failure in Step 1 of the Dream Cycle Workflow, blocking any rule promotion to `.hermes/rules/`.