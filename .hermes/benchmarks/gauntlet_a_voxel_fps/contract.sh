#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
APP_DIR="output/voxel-paintball-app"
test -f "$APP_DIR/package.json"
test -f "$APP_DIR/server/server.js"
test -f "$APP_DIR/client/index.html"
test -f "$APP_DIR/client/js/main.js"
test -f "$APP_DIR/client/js/engine/voxel_world.js"
test -f "$APP_DIR/client/js/engine/paintball.js"
test -f "$APP_DIR/client/js/net/socket_sync.js"
grep -q "InstancedMesh" "$APP_DIR/client/js/engine/voxel_world.js"
grep -q "PointerLockControls" "$APP_DIR/client/js/engine/camera_fps.js"
! grep -rnE "TODO|FIXME|placeholder" "$APP_DIR/server" "$APP_DIR/client"
node "$APP_DIR/server/server.js" &
SRV_PID=$!
trap 'kill $SRV_PID 2>/dev/null || true' EXIT
sleep 1.5
node -e '
const WebSocket = require("./output/voxel-paintball-app/node_modules/ws");
const c1 = new WebSocket("ws://127.0.0.1:8080");
const c2 = new WebSocket("ws://127.0.0.1:8080");
let gotSplat = false;
c2.on("message", (data) => {
  const msg = JSON.parse(data.toString());
  if (msg.type === "splat" || msg.type === "snapshot") gotSplat = true;
});
c1.on("open", () => {
  c1.send(JSON.stringify({type: "shoot", seq: 1, origin: [0,2,0], dir: [0,-0.2,-1], color: "#1A73E8", weapon: 1}));
});
setTimeout(() => { process.exit(gotSplat ? 0 : 1); }, 1500);
'
echo "[PASS] Gauntlet A Contract Verified"
