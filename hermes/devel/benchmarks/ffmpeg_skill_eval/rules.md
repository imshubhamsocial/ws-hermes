# Procedural Rules: Gauntlet E — ffmpeg-skill Local Video Editor

> 1. **Step 0 — Contract & Environment Verification**:
   * Query `python3 ~/.hermes/skills/ffmpeg-skill/scripts/_contract.py --json` to verify SPEC schema availability; run `_contract.py doctor` only if a tool reports a missing encoder/filter.
> 2. **Step 1 — Input Probing (probe.py --json)**:
   * Run `python3 ~/.hermes/skills/ffmpeg-skill/scripts/probe.py output/raw_source.mp4 --json` and record baseline resolution (1920x1080), fps (30), duration (10.0s), and audio channels.
> 3. **Step 2 — Chained Execution (cut -> fit -> loudness -> export)**:
   * Cut segment 0:01-0:07 to output/step1_cut.mp4.
   * Reframe to vertical 9:16 (1080x1920) at output/step2_fit.mp4.
   * Normalize integrated loudness to -14 LUFS (--tp -1.0) at output/final_reels.mp4.
> 4. **Step 3 — Compliance Check & Contact Sheet (check.py & look.py)**:
   * Run `check.py output/final_reels.mp4 --platform reels --json` and `look.py output/final_reels.mp4 --tiles 3x2` (producing output/final_sheet.png).
   * Save the consolidated ffprobe and SPEC verification receipt to output/contract_receipt.json.
