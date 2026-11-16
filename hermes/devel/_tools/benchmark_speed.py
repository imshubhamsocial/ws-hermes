#!/usr/bin/env python3
"""Deterministic Multi-Model Token Speed Benchmark for Port 8138."""
import json
import sys
import urllib.request

PROMPT = (
    "Write a complete, optimized Python function to solve the Traveling "
    "Salesperson Problem using dynamic programming with bitmasking. "
    "Include time complexity analysis."
)


def run_benchmark(tokens: int = 200, temp: float = 1.0, top_p: float = 0.95):
    url = "http://127.0.0.1:8138/v1/chat/completions"
    payload = {
        "messages": [{"role": "user", "content": PROMPT}],
        "max_tokens": tokens,
        "temperature": temp,
        "top_p": top_p,
        "stream": False,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    timings = data.get("timings", {})
    usage = data.get("usage", {})
    msg = data.get("choices", [{}])[0].get("message", {})
    content = msg.get("content", "")
    reasoning = msg.get("reasoning_content", "")

    return {
        "prompt_tokens": usage.get("prompt_tokens", 0),
        "completion_tokens": usage.get("completion_tokens", 0),
        "prompt_tok_per_sec": round(timings.get("prompt_per_second", 0.0), 2),
        "gen_tok_per_sec": round(timings.get("predicted_per_second", 0.0), 2),
        "predicted_ms": round(timings.get("predicted_ms", 0.0), 2),
        "total_chars": len(content) + len(reasoning),
    }


if __name__ == "__main__":
    c = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    t = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
    p = float(sys.argv[3]) if len(sys.argv) > 3 else 0.95
    res = run_benchmark(c, t, p)
    print(json.dumps(res, indent=2))
