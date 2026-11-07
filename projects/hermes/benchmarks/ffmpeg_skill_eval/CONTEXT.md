# Stage Contract: Gauntlet E — ffmpeg-skill Local Video Editor & SPEC Contract

## Inputs
* Workspace Root Map: ../../AGENTS.md
* Installed Upstream Skill: ~/.hermes/skills/ffmpeg-skill/SKILL.md
* Hard Operational Bounds: ./invariants.md
* Procedural Step-Chaining Rules: ./rules.md
* Upstream SPEC Contract & Script Schemas: ./references.md

## Process
> 1. Read ./invariants.md, ./rules.md, and ./references.md and inspect the machine-readable contract via python3 ~/.hermes/skills/ffmpeg-skill/scripts/_contract.py --json | head -n 40.
> 2. Generate a synthetic 10-second 1920x1080 30 fps H.264 + stereo sine/speech audio source clip at output/raw_source.mp4 using local ffmpeg (testsrc2 + sine), preserving output/raw_source.mp4 untouched (mutates_input: false).
> 3. Execute the 4-step kajisho5/ffmpeg-skill pipeline: probe.py -> cut.py (trim 0:01-0:07) -> fit.py (--aspect 9:16 --fit crop) -> loudness.py (-I -14 --tp -1) -> export.py (--preset reels) -> check.py (--platform reels) -> look.py (--tiles 3x2), producing output/final_reels.mp4, output/final_sheet.png, and output/contract_receipt.json.
> 4. Run bash ./contract.sh and emit the mandatory 5-line ffmpeg-skill report (Done:, Steps:, Check:, Look:, Notes:).

## Outputs
* Edited Deliverable: output/final_reels.mp4
* Visual Contact Sheet: output/final_sheet.png
* SPEC Contract Receipt: output/contract_receipt.json

## Verify
* Run bash ./contract.sh and confirm exit code 0.
