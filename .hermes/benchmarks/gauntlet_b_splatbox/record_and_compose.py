import json, os, subprocess, sys, time, urllib.request; from pathlib import Path
BENCH = Path(__file__).resolve().parent; OUT = BENCH / "output"; SAFE = [os.getpid(), os.getppid()]

def kill_t(keep_chrome=False):
    pats = ['konsole.*tabtitle=Hermes-Gauntlet-TUI', 'placeholder.py', 'hermes_cli.*chat']
    if not keep_chrome: pats.extend(['chrome.*hermes_chrome_gauntlet', 'chrome.*9222'])
    for pat in pats:
        try:
            for p in subprocess.check_output(['pgrep', '-f', pat], text=True).split():
                if int(p) not in SAFE: subprocess.run(['kill', '-9', str(p)], capture_output=True)
        except subprocess.CalledProcessError: pass

def wait_idle():
    for _ in range(45):
        try:
            d = json.loads(urllib.request.urlopen("http://127.0.0.1:8138/slots", timeout=2).read())
            if d and not d[0].get('is_processing', False): return True
        except Exception: pass
        time.sleep(1.0)
    return True

def launch_k(prompt, model):
    cmd = ['env', '__NV_PRIME_RENDER_OFFLOAD=0', '__GLX_VENDOR_LIBRARY_NAME=mesa', 'DRI_PRIME=0',
        'distrobox-host-exec', '/usr/bin/konsole', '--separate', '-p', 'tabtitle=Hermes-Gauntlet-TUI',
        '-p', 'Font=Liberation Mono,10', '--qwindowgeometry', '960x1080+0+0', '--workdir', str(BENCH),
        '-e', 'distrobox', 'enter', 'ws-hermes', '--', 'hermes', 'chat',
        '--in', str(BENCH), '-m', model, '--accept-hooks', '--tui', '--yolo', '-q', prompt]
    return subprocess.Popen(cmd)

def run_suite(model="gemma-4-E4B-it-qat-exact", out_mp4="splatbox_gemma4_exact.mp4"):
    sys.path.insert(0, str(BENCH)); from kwin_recorder import find_hid, record_dual
    kill_t(); wait_idle(); subprocess.run(['rm', '-rf', '/tmp/hermes_chrome_gauntlet'])
    for f in ['tracker_verified.json', 'gun_stats.json', 'telemetry.json']: (OUT / f).unlink(missing_ok=True); (BENCH / 'stages/02-controller/output' / f).unlink(missing_ok=True); (BENCH / 'stages/03-execute/output' / f).unlink(missing_ok=True)
    p1 = subprocess.Popen(['distrobox-host-exec', 'python3', str(BENCH / 'placeholder.py'), '1']); time.sleep(1.5)
    launch_k((BENCH / 'PROMPT_STAGE1.txt').read_text().strip(), model); time.sleep(2.5)
    record_dual(find_hid('Hermes-Gauntlet-TUI'), find_hid('Standby'), str(OUT / 'p1_fix.mp4'), str(OUT / 'p1_right.mp4'), duration=150.0, done_file=str(OUT / 'tracker_verified.json'))
    kill_t(); wait_idle()
    p2 = subprocess.Popen(['distrobox-host-exec', 'python3', str(BENCH / 'placeholder.py'), '2']); time.sleep(1.0)
    launch_k((BENCH / 'PROMPT_STAGE2.txt').read_text().strip(), model); time.sleep(2.5)
    record_dual(find_hid('Hermes-Gauntlet-TUI'), find_hid('Standby'), str(OUT / 'p2_calib.mp4'), str(OUT / 'p2_game.mp4'), duration=140.0, done_file=str(OUT / 'gun_stats.json'))
    kill_t(); wait_idle()
    p3 = subprocess.Popen(['distrobox-host-exec', 'python3', str(BENCH / 'placeholder.py'), '3']); time.sleep(1.0)
    launch_k((BENCH / 'PROMPT_STAGE3.txt').read_text().strip(), model); time.sleep(2.5)
    record_dual(find_hid('Hermes-Gauntlet-TUI'), find_hid('Standby'), str(OUT / 'p3_run.mp4'), str(OUT / 'p4_game.mp4'), duration=180.0, done_file=str(OUT / 'telemetry.json'))
    kill_t()
    flt = "scale=960:1080:force_original_aspect_ratio=decrease,pad=960:1080:(ow-iw)/2:(oh-ih)/2,setsar=1"
    fc = f"[0:v]{flt}[v0];[1:v]{flt}[v1];[2:v]{flt}[v2];[v0][v1][v2]concat=n=3:v=1[l];[3:v]{flt}[v3];[4:v]{flt}[v4];[5:v]{flt}[v5];[v3][v4][v5]concat=n=3:v=1[r];[l][r]hstack=inputs=2[out]"
    subprocess.run(['distrobox-host-exec', 'ffmpeg', '-y', '-i', str(OUT / 'p1_fix.mp4'), '-i', str(OUT / 'p2_calib.mp4'), '-i', str(OUT / 'p3_run.mp4'),
        '-i', str(OUT / 'p1_right.mp4'), '-i', str(OUT / 'p2_game.mp4'), '-i', str(OUT / 'p4_game.mp4'),
        '-filter_complex', fc, '-map', '[out]', '-c:v', 'libx264', '-threads', '4', '-preset', 'faster', '-crf', '20', '-pix_fmt', 'yuv420p', str(OUT / out_mp4)], check=True)
    print(f"Master benchmark certified: {OUT / out_mp4}")

if __name__ == '__main__':
    run_suite(sys.argv[1] if len(sys.argv) > 1 else "gemma-4-E4B-it-qat-exact", sys.argv[2] if len(sys.argv) > 2 else "splatbox_gemma4_exact.mp4")
