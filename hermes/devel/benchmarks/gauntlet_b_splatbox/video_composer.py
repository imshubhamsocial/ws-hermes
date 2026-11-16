import subprocess, sys; from pathlib import Path
FONT = "/usr/share/fonts/adwaita-mono-fonts/AdwaitaMono-Bold.ttf"

def compose_split(raw_vid, final_vid, name, ctx, vram, sc):
    raw_p, fin_p = Path(raw_vid).resolve(), Path(final_vid).resolve()
    banner = f"{name} | Context: {ctx} | Active VRAM: {vram} | Gauntlet B Score: {sc}"
    vf = (f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,"
          f"drawbox=y=0:color=black@0.82:width=iw:height=64:t=fill,"
          f"drawtext=fontfile={FONT}:text='{banner}':fontcolor=white:fontsize=22:x=(w-text_w)/2:y=20")
    cmd = ["flatpak-spawn", "--host", "ffmpeg", "-y", "-i", str(raw_p),
           "-vf", vf, "-c:v", "libx264", "-crf", "20", "-preset", "faster", "-pix_fmt", "yuv420p", str(fin_p)]
    subprocess.run(cmd, check=True)
    print(f"[COMPOSER] Certified: {fin_p.name} (Score={sc})")

def concat_showcase(vid_paths, master_vid):
    m_path, list_file = Path(master_vid).resolve(), Path(master_vid).parent / "concat_list.txt"
    with open(list_file, "w") as f:
        for vp in vid_paths: f.write(f"file '{Path(vp).resolve()}'\n")
    cmd = ["flatpak-spawn", "--host", "ffmpeg", "-y", "-f", "concat", "-safe", "0",
           "-i", str(list_file), "-c", "copy", str(m_path)]
    subprocess.run(cmd, check=True)
    list_file.unlink(missing_ok=True)
    print(f"[COMPOSER] Master Showcase Generated: {m_path.name}")

if __name__ == "__main__":
    if len(sys.argv) >= 7 and sys.argv[1] == "split":
        compose_split(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7])
    elif len(sys.argv) >= 3 and sys.argv[1] == "concat":
        concat_showcase(sys.argv[3:], sys.argv[2])
