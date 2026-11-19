#!/usr/bin/env python3
"""Deterministic ICM Stage Contract & Atomic Script Verifier (34 lines)."""
import pathlib
import sys

REQUIRED_HEADERS = ("## Inputs", "## Process", "## Outputs")
MAX_SCRIPT_LINES = 59

def verify_stage(stage_dir: pathlib.Path) -> tuple[bool, list[str]]:
    errors: list[str] = []
    ctx = stage_dir / "CONTEXT.md"
    if not ctx.is_file():
        return False, [f"MISSING_CONTRACT: {ctx}"]
    text = ctx.read_text(encoding="utf-8")
    for hdr in REQUIRED_HEADERS:
        if hdr not in text:
            errors.append(f"MISSING_SECTION: {hdr} in {ctx}")
    if not (stage_dir / "output").is_dir():
        errors.append(f"MISSING_OUTPUT_DIR: {stage_dir / 'output'}")
    for ext in ("*.py", "*.sh", "*.js"):
        for script in stage_dir.rglob(ext):
            lines = len(script.read_text(encoding="utf-8", errors="ignore").splitlines())
            if lines > MAX_SCRIPT_LINES:
                errors.append(f"ATOMIC_LIMIT_EXCEEDED: {script} has {lines} lines (max 59)")
    return len(errors) == 0, errors

if __name__ == "__main__":
    target = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    ok, errs = verify_stage(target)
    if not ok:
        for err in errs:
            print(err, file=sys.stderr)
        sys.exit(1)
    print(f"STAGE_VERIFIED: {target}")
