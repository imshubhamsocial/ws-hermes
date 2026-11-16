import cv2, dbus, os, subprocess, sys, time, numpy as np
OPTS = dbus.Dictionary({'include-decoration': dbus.Boolean(True), 'include-shadow': dbus.Boolean(False)}, signature='sv')

def find_hid(kw, timeout=10.0):
    t0 = time.time()
    while True:
        try:
            for m in dbus.Interface(dbus.SessionBus().get_object('org.kde.KWin', '/WindowsRunner'), 'org.kde.krunner1').Match(''):
                n = str(m[1]).lower()
                if (any(k in n for k in kw) if isinstance(kw, list) else (kw.lower() in n)) and '_{' in str(m[0]): return '{' + str(m[0]).split('_{')[1]
        except Exception: pass
        if time.time() - t0 >= timeout: return None
        time.sleep(0.2)

def cap_bytes(iface, hid):
    r, w = os.pipe()
    try:
        ret = iface.CaptureWindow(hid, OPTS, dbus.types.UnixFd(w)); os.close(w); d = b''
        while True:
            c = os.read(r, 65536)
            if not c: break
            d += c
        os.close(r); return d, int(ret['width']), int(ret['height'])
    except Exception: os.close(w); os.close(r); return None, 0, 0

def to_cv(d, w, h, tw=960, th=1080):
    if not d or w <= 0 or h <= 0: return None
    if w == tw and h == th: return d
    arr = np.frombuffer(d, dtype=np.uint8).reshape((h, w, 4))
    if w > tw or h > th: arr = cv2.resize(arr, (min(w, tw), min(h, th)))
    ch, cw = arr.shape[:2]; cv = np.zeros((th, tw, 4), dtype=np.uint8)
    cv[(th - ch) // 2:(th - ch) // 2 + ch, (tw - cw) // 2:(tw - cw) // 2 + cw] = arr; return cv.tobytes()

def spawn_ff(w, h, fps, out):
    return subprocess.Popen(['distrobox-host-exec', 'ffmpeg', '-y', '-f', 'rawvideo', '-pixel_format', 'rgba', '-video_size', f'{w}x{h}',
           '-framerate', str(fps), '-i', '-', '-c:v', 'libx264', '-preset', 'ultrafast', '-threads', '2', '-crf', '20', '-pix_fmt', 'yuv420p', str(out)], stdin=subprocess.PIPE)

def record_dual(hl, hr, out_l, out_r, duration=180.0, fps=8, done_file=None):
    iface = dbus.Interface(dbus.SessionBus().get_object('org.kde.KWin', '/org/kde/KWin/ScreenShot2'), 'org.kde.KWin.ScreenShot2')
    pl = spawn_ff(960, 1080, fps, out_l) if out_l else None; pr = spawn_ff(960, 1080, fps, out_r) if out_r else None
    last_l, last_r, box_found, t0, t_done = None, None, False, time.time(), None
    while time.time() - t0 < duration:
        t_f = time.time()
        if pl and hl:
            d, w, h = cap_bytes(iface, hl); b = to_cv(d, w, h)
            if b: last_l = b; pl.stdin.write(b)
            elif last_l: pl.stdin.write(last_l)
        if pr and out_r:
            if not box_found:
                h_box = find_hid(['paintball', 'splatbox'], timeout=0.0)
                if h_box: hr = h_box; box_found = True
            d, w, h = cap_bytes(iface, hr) if hr else (None, 0, 0); b = to_cv(d, w, h)
            if b: last_r = b; pr.stdin.write(b)
            elif last_r: pr.stdin.write(last_r)
        if done_file and os.path.exists(done_file) and t_done is None: t_done = time.time()
        if t_done and time.time() - t_done > 15.0: break
        rem = (1.0 / fps) - (time.time() - t_f)
        if rem > 0: time.sleep(rem)
    for p in [pl, pr]: (p.stdin.close(), p.wait()) if p else None
