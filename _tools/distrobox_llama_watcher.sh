#!/usr/bin/env bash
# Synchronize llama-server.service lifecycle with ws-hermes container
set -euo pipefail

CONTAINER="ws-hermes"
PODMAN="podman"
command -v podman >/dev/null 2>&1 || PODMAN="distrobox-host-exec podman"

sync_state() {
    local status
    status="$($PODMAN inspect --type container --format '{{.State.Status}}' "$CONTAINER" 2>/dev/null || echo "stopped")"
    if [[ "$status" == "running" ]]; then
        systemctl --user is-active --quiet llama-server.service || systemctl --user start llama-server.service || true
    else
        systemctl --user is-active --quiet llama-server.service && systemctl --user stop llama-server.service || true
    fi
}

sync_state

exec $PODMAN events --filter container="$CONTAINER" --filter event=start --filter event=stop --filter event=died --format '{{.Status}}' | while read -r event; do
    case "$event" in
        start)
            systemctl --user restart llama-server.service || true
            ;;
        stop|died)
            systemctl --user stop llama-server.service || true
            ;;
    esac
done
