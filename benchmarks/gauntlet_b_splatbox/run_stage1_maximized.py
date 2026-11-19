import json, os, subprocess, sys, time, urllib.request; from pathlib import Path
BENCH = Path(__file__).resolve().parent; OUT = BENCH / "output"; SAFE = [os.getpid(), os.getppid()]

def prep():
    for pat in ['konsole.*tabtitle=Hermes-Gauntlet-TUI', 'placeholder.py', 'hermes_cli.*chat']:
        try:
            for p in subprocess.check_output(['pgrep', '-f', pat], text=True).split():
                if int(p) not in SAFE: subprocess.run(['kill', '-9', str(p)], capture_output=True)
        except subprocess.CalledProcessError: pass
    for _ in range(30):
        try:
            d = json.loads(urllib.request.urlopen("http://127.0.0.1:8138/slots", timeout=2).read())
            if d and not d[0].get('is_processing', False): break
        except Exception: time.sleep(1.0)
    (OUT / 'tracker_verified.json').unlink(missing_ok=True)

def maximize():
    js = "var w=workspace.windowList();for(var i=0;i<w.length;i++){if((w[i].caption||'').indexOf('Hermes-Gauntlet-TUI')!==-1){w[i].setMaximize(true,true);workspace.activeWindow=w[i];}}"
    Path('/tmp/max_k.js').write_text(js)
    for a in [('loadScript', ['/tmp/max_k.js', 'm']), ('run', []), ('unloadScript', ['m'])]:
        t = '/Scripting/Script0' if a[0] == 'run' else '/Scripting'
        subprocess.run(['distrobox-host-exec', '/usr/bin/qdbus-qt6', 'org.kde.KWin', t, f'org.kde.kwin.{"Script" if a[0]=="run" else "Scripting"}.{a[0]}', *a[1]], capture_output=True)

def record(hid, out_mp4, duration=150.0, fps=8, done=None):
    import cv2, dbus, numpy as np
    opts = dbus.Dictionary({'include-decoration': dbus.Boolean(True), 'include-shadow': dbus.Boolean(False)}, signature='sv')
    iface = dbus.Interface(dbus.SessionBus().get_object('org.kde.KWin', '/org/kde/KWin/ScreenShot2'), 'org.kde.KWin.ScreenShot2')
    p = subprocess.Popen(['distrobox-host-exec', 'ffmpeg', '-y', '-f', 'rawvideo', '-pixel_format', 'rgba', '-video_size', '1920x1080',
        '-framerate', str(fps), '-i', '-', '-c:v', 'libx264', '-preset', 'ultrafast', '-threads', '4', '-crf', '20', '-pix_fmt', 'yuv420p', str(out_mp4)], stdin=subprocess.PIPE)
    t0, td, last = time.time(), None, None
    while time.time() - t0 < duration:
        tf = time.time(); r, w = os.pipe()
        try:
            ret = iface.CaptureWindow(hid, opts, dbus.types.UnixFd(w)); os.close(w); d = b''
            while True:
                c = os.read(r, 65536); (d := d + c) if c else None
                if not c: break
            os.close(r); wd, ht = int(ret['width']), int(ret['height']); arr = np.frombuffer(d, dtype=np.uint8).reshape((ht, wd, 4))
            if wd != 1920 or ht != 1080: arr = cv2.resize(arr, (1920, 1080))
            last = arr.tobytes(); p.stdin.write(last)
        except Exception: (p.stdin.write(last) if last else None)
        if done and os.path.exists(done) and td is None: td = time.time()
        if td and time.time() - td > 15.0: break
        rem = (1.0 / fps) - (time.time() - tf); time.sleep(rem) if rem > 0 else None
    p.stdin.close(); p.wait()

def run():
    prep()
    cmd = ['env', '__NV_PRIME_RENDER_OFFLOAD=0', '__GLX_VENDOR_LIBRARY_NAME=mesa', 'DRI_PRIME=0',
        'distrobox-host-exec', '/usr/bin/konsole', '--separate', '-p', 'tabtitle=Hermes-Gauntlet-TUI',
        '-p', 'Font=Liberation Mono,11', '--qwindowgeometry', '1920x1080+0+0', '--workdir', str(BENCH),
        '-e', 'distrobox', 'enter', 'ws-hermes', '--', 'hermes', 'chat',
        '--in', str(BENCH), '-m', 'gemma-4-E4B-it-qat-exact', '--accept-hooks', '--tui', '--yolo', '-q', (BENCH / 'PROMPT_STAGE1.txt').read_text().strip()]
    proc = subprocess.Popen(cmd); time.sleep(2.5); maximize()
    sys.path.insert(0, str(BENCH)); from kwin_recorder import find_hid; hid = find_hid('Hermes-Gauntlet-TUI')
    (record(hid, OUT / 'splatbox_stage1_maximized.mp4', done=str(OUT / 'tracker_verified.json')) if hid else proc.wait())
    print("Stage 1 maximized completed.")

if __name__ == '__main__': run()
