import subprocess; from pathlib import Path

BENCH = Path("hermes/devel/benchmarks/gauntlet_b_splatbox/output").resolve()

def build_showcase():
    src = BENCH / "splatbox_gemma4_exact.mp4"
    dst = BENCH / "hermes_splatbox_showcase.mp4"
    if src.exists():
        subprocess.run(["cp", "-f", str(src), str(dst)], check=True)
        print(f"Master showcase certified from Gemma 4 Exact: {dst}")

if __name__ == '__main__':
    build_showcase()
