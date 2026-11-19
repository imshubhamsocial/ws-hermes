#!/usr/bin/env python3
"""Automated 8-Point ICM Walk Test and Workspace Contract Validator."""
import json, os, re, sys

def get_root() -> str:
    d = os.path.dirname(os.path.abspath(__file__))
    while d != "/" and not (os.path.isfile(f"{d}/CONTEXT.md") and os.path.isfile(f"{d}/AGENTS.md")):
        d = os.path.dirname(d)
    return d if d != "/" else os.getcwd()

ROOT = get_root()

def count_lines(path: str) -> int:
    with open(path, "r", encoding="utf-8") as f:
        return len(f.readlines())

def validate_workspace() -> int:
    errors = []
    core = [os.path.join(ROOT, p) for p in ["AGENTS.md", "CONTEXT.md",
            ".hermes/_config/invariants.md", "benchmarks/_config/invariants.md"]]
    errors.extend([f"Missing core file: {p}" for p in core if not os.path.isfile(p)])
    if os.path.isfile(core[0]) and count_lines(core[0]) > 60:
        errors.append("Layer 0 AGENTS.md exceeds 60-line limit")
    if os.path.isfile(core[1]) and count_lines(core[1]) > 80:
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
            if not os.path.exists(os.path.normpath(os.path.join(ROOT, sd, rel))):
                errors.append(f"Broken relative link in {sd}/CONTEXT.md: {rel}")
    report = {"walk_test_passed": len(errors) == 0, "error_count": len(errors), "errors": errors}
    print(json.dumps(report, indent=2))
    return 0 if len(errors) == 0 else 1

if __name__ == "__main__":
    sys.exit(validate_workspace())
