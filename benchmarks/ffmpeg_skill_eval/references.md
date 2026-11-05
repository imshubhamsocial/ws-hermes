# Layer 3 Reference Schemas: Gauntlet E (kajisho5/ffmpeg-skill SPEC Contract)

## 1. Upstream Repository & SPEC Architecture
* **Source**: https://github.com/kajisho5/ffmpeg-skill (SKILL.md, scripts/_contract.py, 42 tools)
* **Contract Inspection Command**: `python3 ~/.hermes/skills/ffmpeg-skill/scripts/_contract.py --json`
* **Canonical Step Order**: color -> cut -> join -> silence -> fit -> caption/overlay -> sync -> audio -> loudness -> export

## 2. Core Script Invocation Signatures (~/.hermes/skills/ffmpeg-skill/scripts/)
* **Probe**: `python3 "$SKILL_DIR/scripts/probe.py" input.mp4 --json`
* **Cut**: `python3 "$SKILL_DIR/scripts/cut.py" input.mp4 --segments 0:01-0:07 --accurate -o step1_cut.mp4 --json`
* **Fit (9:16 Vertical)**: `python3 "$SKILL_DIR/scripts/fit.py" step1_cut.mp4 --aspect 9:16 --fit crop -o step2_fit.mp4 --json`
* **Loudness (EBU R128)**: `python3 "$SKILL_DIR/scripts/loudness.py" step2_fit.mp4 -I -14 --tp -1 -o step3_loud.mp4 --json`
* **Platform Export**: `python3 "$SKILL_DIR/scripts/export.py" step3_loud.mp4 --preset reels -o final_reels.mp4 --json`
* **Delivery Check**: `python3 "$SKILL_DIR/scripts/check.py" final_reels.mp4 --platform reels --json`
* **Visual Contact Sheet**: `python3 "$SKILL_DIR/scripts/look.py" final_reels.mp4 --tiles 3x2 -o final_sheet.png --json`

## 3. Mandatory 5-Line Final Report Format (kajisho5/ffmpeg-skill/SKILL.md)
```
Done: output/final_reels.mp4 — 6.00 s, 1080x1920, 30 fps, H.264, AAC stereo, -14.0 LUFS
Steps: cut 0:01-0:07 -> fit 9:16 crop -> loudness -14 LUFS -> export reels
Check: reels — all checks pass (verified: true)
Look: output/final_sheet.png (9:16 vertical crop verified across 3x2 contact sheet)
Notes: source output/raw_source.mp4 preserved untouched; SPEC contract validated
```
