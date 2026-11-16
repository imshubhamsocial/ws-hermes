#!/usr/bin/env bash
# Modular Server Manager for Gauntlet B: Google Gemma 4 Exact
set -euo pipefail
ACTION="${1:-stop}"
BIN="${HOME}/.local/bin/llama-server"
[[ -x "$BIN" ]] || BIN="/var/home/imshubhamsocial/.local/bin/llama-server"

stop_srv() {
    pkill -9 -x llama-server 2>/dev/null || pkill -9 -f llama-server.bin 2>/dev/null || true
    for _ in {1..15}; do ! curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1 && break || sleep 0.5; done
    for _ in {1..20}; do [[ $(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null || echo 0) -lt 500 ]] && break || sleep 0.5; done
    echo "[SERVER] Stopped. Quiescent VRAM: $(nvidia-smi --query-gpu=memory.used --format=csv,noheader 2>/dev/null || echo '0 MiB')"
}

start_srv() {
    stop_srv
    echo "[SERVER] Starting Google Gemma 4 Exact (128K TurboQuant + MTP Drafter)..."
    "$BIN" >"/tmp/llama_gemma4_exact.log" 2>&1 &
    for _ in {1..40}; do curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1 && break || sleep 1; done
    curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1 || { echo "[ERROR] Server failed to start"; exit 1; }
    echo "[SERVER] Online: gemma4_exact | VRAM: $(nvidia-smi --query-gpu=memory.used --format=csv,noheader 2>/dev/null || echo '0 MiB')"
}

[[ "${ACTION}" == "start" ]] && start_srv || stop_srv
