#!/usr/bin/env python3
"""Automated 8-Point ICM Walk Test and Workspace Contract Validator."""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def count_lines(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        return len(f.readlines())

def validate_workspace() -> int:
    errors = []
    agents_md = os.path.join(ROOT, "AGENTS.md")
    context_md = os.path.join(ROOT, "CONTEXT.md")
    invariants_md = os.path.join(ROOT, ".hermes", "_config", "invariants.md")
    bench_invariants = os.path.join(ROOT, "benchmarks", "_config", "invariants.md")
    for req in [agents_md, context_md, invariants_md, bench_invariants]:
        if not os.path.isfile(req):
            errors.append(f"Missing core file: {req}")
    if os.path.isfile(agents_md) and count_lines(agents_md) > 60:
        errors.append("Layer 0 AGENTS.md exceeds 60-line limit")
    if os.path.isfile(context_md) and count_lines(context_md) > 80:
        errors.append("Layer 1 CONTEXT.md exceeds 80-line limit")
    stage_dirs = [
        "benchmarks/gauntlet_a_voxel_fps", "benchmarks/gauntlet_b_splatbox",
        "benchmarks/gauntlet_c_aquarium",
        "benchmarks/gauntlet_b_splatbox/stages/01-probe",
        "benchmarks/gauntlet_b_splatbox/stages/02-controller",
        "benchmarks/gauntlet_b_splatbox/stages/03-execute",
        "benchmarks/gauntlet_c_aquarium/stages/01-spec",
        "benchmarks/gauntlet_c_aquarium/stages/02-scaffold",
        "benchmarks/gauntlet_c_aquarium/stages/03-implement",
        "benchmarks/gauntlet_c_aquarium/stages/04-verify",
    ]
    for sd in stage_dirs:
        cpath = os.path.join(ROOT, sd, "CONTEXT.md")
        if not os.path.isfile(cpath):
            errors.append(f"Missing stage contract: {sd}/CONTEXT.md")
            continue
        if count_lines(cpath) > 80:
            errors.append(f"{sd}/CONTEXT.md exceeds 80-line limit")
        with open(cpath, "r", encoding="utf-8") as f:
            txt = f.read()
        for sec in ["Inputs", "Process", "Outputs", "Check"]:
            if not re.search(rf"^##\s+(\d+\.\s+)?{sec}", txt, re.MULTILINE):
                errors.append(f"{sd}/CONTEXT.md missing required section: ## {sec}")
        for rel in re.findall(r"`(\.\./[^`]+)`", txt):
            target = os.path.normpath(os.path.join(ROOT, sd, rel))
            if not os.path.exists(target):
                errors.append(f"Broken relative link in {sd}/CONTEXT.md: {rel}")
    report = {"walk_test_passed": len(errors) == 0, "error_count": len(errors), "errors": errors}
    print(json.dumps(report, indent=2))
    return 0 if len(errors) == 0 else 1

if __name__ == "__main__":
    sys.exit(validate_workspace())
