---
artifact_type: icm_human_checkpoint_gate
stage_id: "{NN}-{stage_name}"
u_curve_tier: "high_leverage_boundary"
human_decision: "APPROVED"
reviewer: "imshubhamsocial"
timestamp_utc: "{timestamp_utc}"
---

# Human Review Checkpoint: {NN}-{stage_name}

## Human Check Instructions

> 1. Inspect the primary deliverable inside output/ and the audit receipt in output/check.md.
> 2. Edit the deliverable in output/ if adjustments are needed before the downstream stage reads it.
> 3. Set human_decision in the YAML frontmatter above to APPROVED (or EDITED) to release the next stage, or REJECTED to halt and re-compile this stage.
