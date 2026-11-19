#!/usr/bin/env python3
"""Deterministic NVIDIA RTX 3050 VRAM Ceiling & Quiescence Verifier."""
import argparse
import json
import subprocess
import sys

def check_vram(mode: str, max_active_mib: float, max_quiescent_mib: float) -> int:
    cmd = ["nvidia-smi", "--query-gpu=memory.used,memory.total,temperature.gpu,power.draw",
           "--format=csv,noheader,nounits"]
    out = subprocess.check_output(cmd, text=True).strip().splitlines()[0]
    parts = [p.strip() for p in out.split(",")]
    used_mib = float(parts[0])
    total_mib = float(parts[1])
    temp_c = float(parts[2])
    power_w = float(parts[3]) if parts[3] != "[N/A]" else 0.0
    ceiling = max_quiescent_mib if mode == "quiescent" else max_active_mib
    passed = used_mib <= ceiling
    receipt = {
        "mode": mode,
        "vram_used_mib": used_mib,
        "vram_total_mib": total_mib,
        "ceiling_mib": ceiling,
        "headroom_mib": round(ceiling - used_mib, 1),
        "temperature_c": temp_c,
        "power_w": power_w,
        "passed": passed
    }
    print(json.dumps(receipt))
    return 0 if passed else 1

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["active", "quiescent"], default="quiescent")
    ap.add_argument("--max-active", type=float, default=5800.0)
    ap.add_argument("--max-quiescent", type=float, default=100.0)
    args = ap.parse_args()
    sys.exit(check_vram(args.mode, args.max_active, args.max_quiescent))
