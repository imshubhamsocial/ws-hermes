#!/usr/bin/env bash
set -euo pipefail
test -f "output/raw_source.mp4"
test -f "output/final_reels.mp4"
test -f "output/final_sheet.png"
test -f "output/contract_receipt.json"
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height -of json "output/final_reels.mp4" > /tmp/ffprobe_v.json
python3 -c '
import json
v = json.load(open("/tmp/ffprobe_v.json"))["streams"][0]
assert v["codec_name"] == "h264", f"Expected h264, got {v}"
assert int(v["width"]) == 1080 and int(v["height"]) == 1920, f"Expected 1080x1920, got {v}"
rec = json.load(open("output/contract_receipt.json"))
assert rec.get("verified") is True, f"Contract receipt not verified: {rec}"
print("[PASS] Gauntlet E ffmpeg-skill Stream & SPEC Contract Verified:", v)
'
