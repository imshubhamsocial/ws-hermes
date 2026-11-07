# Hard Invariants: Gauntlet E — ffmpeg-skill Local Video Editor

> 1. **100% Local Execution & Zero Cloud Egress**: Use only local ffmpeg (6.1+), ffprobe, and Python 3.10+ standard library scripts in ~/.hermes/skills/ffmpeg-skill/scripts/. Never call external cloud video APIs.
> 2. **Source Immutability (mutates_input: false)**: Never overwrite or modify output/raw_source.mp4. All intermediate and final files must write to distinct output paths.
> 3. **Mandatory Step-Chain Ordering (kajisho5/ffmpeg-skill)**: Frame-size and aspect-ratio adjustments (fit.py --aspect 9:16) MUST occur after cut.py and strictly before any caption/overlay, loudness normalization (loudness.py -I -14 --tp -1), and final platform export (export.py --preset reels).
> 4. **Mandatory ffprobe / check.py / look.py Verification**: Never report task completion without verifying output stream metadata (1080x1920, H.264, AAC, duration ~6.0s) via ffprobe/check.py and generating a contact sheet (look.py --tiles 3x2) whenever the visual frame changes.
> 5. **5-Line Summary Output Contract**: The final response MUST conclude with the exact 5-line Done: / Steps: / Check: / Look: / Notes: report format defined in kajisho5/ffmpeg-skill/SKILL.md.
