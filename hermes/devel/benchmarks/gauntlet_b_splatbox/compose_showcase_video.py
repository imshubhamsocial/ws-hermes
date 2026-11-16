import subprocess; from pathlib import Path
from video_composer import compose_split, concat_showcase

BENCH = Path("hermes/devel/benchmarks/gauntlet_b_splatbox/output").resolve()

def build_showcase():
    cmd = [
        "flatpak-spawn", "--host", "ffmpeg", "-y",
        "-i", str(BENCH / "splatbox_gemma4_exact.mp4"),
        "-i", str(BENCH / "splatbox_dory_k2.mp4"),
        "-i", str(BENCH / "splatbox_dory_k4.mp4"),
        "-filter_complex", "[0:v]fps=10,setpts=PTS-STARTPTS[v0];[1:v]fps=10,setpts=PTS-STARTPTS[v1];[2:v]fps=10,setpts=PTS-STARTPTS[v2];[v0][v1][v2]concat=n=3:v=1:a=0[outv]",
        "-map", "[outv]", "-c:v", "libx264", "-crf", "21", "-pix_fmt", "yuv420p",
        str(BENCH / "hermes_splatbox_showcase.mp4")
    ]
    subprocess.run(cmd, check=True)
    print(f"Master showcase certified: {BENCH / 'hermes_splatbox_showcase.mp4'}")

if __name__ == '__main__':
    build_showcase()
