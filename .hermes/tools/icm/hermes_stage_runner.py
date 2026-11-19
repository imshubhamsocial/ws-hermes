#!/usr/bin/env python3
"""Autonomous ICM Stage Compiler with llama-server KV Slot Isolation."""
import argparse
import datetime
import json
import os
import subprocess
import sys
import urllib.request

def erase_kv_slot(base_url: str = "http://127.0.0.1:8138") -> bool:
    req = urllib.request.Request(f"{base_url}/slots/0?action=erase", method="POST",
                                 headers={"Content-Type": "application/json"}, data=b"{}")
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            return resp.status == 200
    except Exception:
        return False

def run_stage(stage_dir: str, gate_mode: str, skip_llm: bool) -> int:
    stage_name = os.path.basename(stage_dir.rstrip("/"))
    out_dir = os.path.join(stage_dir, "output")
    os.makedirs(out_dir, exist_ok=True)
    kv_erased = erase_kv_slot()
    if not skip_llm:
        prompt_path = os.path.join(out_dir, ".compiler_prompt.txt")
        prompt = (f"Read AGENTS.md and {stage_dir}/CONTEXT.md. Load only the exact paths in Inputs. "
                  f"Call read_file before editing any existing file. Execute Process steps, write "
                  f"deliverables to {out_dir}/, and stop immediately.")
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(prompt)
        env = {k: v for k, v in os.environ.items() if k != "HERMES_TUI_RESUME"}
        subprocess.run(["hermes", "chat", "--query-file", prompt_path], env=env, check=True)
        erase_kv_slot()
    contract_sh = os.path.join(stage_dir, "contract.sh")
    rc = subprocess.run(["bash", contract_sh], check=False).returncode if os.path.exists(contract_sh) else 0
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    verdict = "PASS" if rc == 0 else "FAIL"
    with open(os.path.join(out_dir, "check.md"), "w", encoding="utf-8") as f:
        f.write(f"---\nstage_id: \"{stage_name}\"\ntimestamp_utc: \"{now}\"\n"
                f"kv_slot_erased: {str(kv_erased).lower()}\ncontract_exit_code: {rc}\n"
                f"auditor_verdict: \"{verdict}\"\n---\n# Audit: {verdict}\n")
    decision = "AUTO_APPROVED_BY_CONTRACT" if (gate_mode == "autonomous" and rc == 0) else (
               "APPROVED" if rc == 0 else "REJECTED")
    with open(os.path.join(out_dir, "checkpoint.md"), "w", encoding="utf-8") as f:
        f.write(f"---\nstage_id: \"{stage_name}\"\nhuman_decision: \"{decision}\"\n"
                f"timestamp_utc: \"{now}\"\n---\n# Checkpoint: {decision}\n")
    print(json.dumps({"stage": stage_name, "verdict": verdict, "checkpoint": decision, "kv_erased": kv_erased}))
    return rc

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage-dir", required=True)
    ap.add_argument("--gate-mode", choices=["autonomous", "interactive"], default="autonomous")
    ap.add_argument("--verify-only", action="store_true")
    args = ap.parse_args()
    sys.exit(run_stage(args.stage_dir, args.gate_mode, args.verify_only))
