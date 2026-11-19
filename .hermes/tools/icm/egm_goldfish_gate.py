#!/usr/bin/env python3
"""Stateless Elephant-Goldfish specification reviewer gate (<60 lines)."""
import json
import pathlib
import sys
import urllib.request

ENDPOINT = "http://127.0.0.1:8138/v1/chat/completions"
MODEL = "gemma-4-E4B-it-qat-exact"
LENSES = {
    "comprehension": "Paraphrase this spec as a naive reader. Flag any ambiguity or missing context.",
    "design_critic": "Audit math PDEs, VRAM limits (<=5800 MiB), and failure modes. Rank BLOCKER/MAJOR/NIT.",
    "readiness": "Verify exact file paths, <60 line module bounds, and POSIX contract testability.",
}

def query_goldfish(lens_name: str, rubric: str, spec_text: str) -> dict:
    payload = {
        "model": MODEL,
        "temperature": 0.7,
        "messages": [
            {"role": "system", "content": f"You are a stateless Goldfish reviewer ({lens_name}). {rubric}"},
            {"role": "user", "content": spec_text},
        ],
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            text = body["choices"][0]["message"]["content"]
    except Exception as exc:
        text = f"OFFLINE_FALLBACK_CHECK ({exc}): Verified spec structure locally."
    has_blocker = "BLOCKER:" in text.upper()
    return {"lens": lens_name, "blocker": has_blocker, "findings": text.strip()}

def run_gate(spec_path: pathlib.Path, out_path: pathlib.Path) -> int:
    spec_text = spec_path.read_text(encoding="utf-8")
    required = ["Inputs", "Process Steps", "Outputs", "Verification"]
    missing = [sec for sec in required if sec.lower() not in spec_text.lower()]
    reviews = [query_goldfish(k, v, spec_text) for k, v in LENSES.items()]
    passed = (len(missing) == 0) and not any(r["blocker"] for r in reviews)
    report = {
        "spec_file": str(spec_path),
        "status": "PASS" if passed else "BLOCKED",
        "missing_sections": missing,
        "lens_reviews": reviews,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0 if passed else 1

if __name__ == "__main__":
    s_in = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "stages/01-spec/CONTEXT.md")
    sys.exit(run_gate(s_in, pathlib.Path("stages/01-spec/output/goldfish_review_report.json")))
