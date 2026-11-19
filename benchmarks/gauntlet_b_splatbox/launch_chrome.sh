#!/usr/bin/env bash
pkill -9 -f 'chrome.*hermes_chrome_gauntlet' 2>/dev/null || true
rm -rf /tmp/hermes_chrome_gauntlet
google-chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/hermes_chrome_gauntlet \
  --no-first-run --no-default-browser-check --disable-fre \
  --disable-session-crashed-bubble --hide-crash-restore-bubble --disable-infobars \
  --window-position=960,0 --window-size=960,1080 \
  https://splatbox.alexdiaz.fyi/?autoplay >/dev/null 2>&1 &

for _ in $(seq 1 30); do
  if curl -sf http://127.0.0.1:9222/json/version >/dev/null 2>&1; then break; fi
  sleep 0.4
done
