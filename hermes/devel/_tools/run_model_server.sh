#!/usr/bin/env bash
# Hermes Production Model Server Launcher (Google Gemma 4 Exact)
set -euo pipefail
BIN="${HOME}/.local/bin/llama-server"
[[ -x "$BIN" ]] || BIN="/var/home/imshubhamsocial/.local/bin/llama-server"

echo "[SERVER] Launching Google Gemma 4 Exact via production wrapper..."
exec "$BIN" "$@"
