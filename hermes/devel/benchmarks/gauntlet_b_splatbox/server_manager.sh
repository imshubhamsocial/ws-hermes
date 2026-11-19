#!/usr/bin/env bash
# Modular Server Manager for Gauntlet B: Google Gemma 4 Exact
set -euo pipefail
ACTION="${1:-stop}"

if [[ "${ACTION}" == "start" ]]; then
    systemctl --user start llama-server.service
    for _ in {1..30}; do curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1 && break || sleep 1; done
    curl -sf http://127.0.0.1:8138/health >/dev/null 2>&1 || { echo "[ERROR] Server failed to start"; exit 1; }
    echo "[SERVER] Online: llama-server.service | VRAM: $(nvidia-smi --query-gpu=memory.used --format=csv,noheader 2>/dev/null || echo '0 MiB')"
else
    systemctl --user stop llama-server.service || true
    echo "[SERVER] Stopped llama-server.service."
fi
