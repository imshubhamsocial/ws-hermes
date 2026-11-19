import os, subprocess, sys, time; from pathlib import Path
BENCH = Path("hermes/devel/benchmarks/gauntlet_b_splatbox").resolve()
SAFE = [os.getpid(), os.getppid(), 44037, 350270]

def kill_targets():
    for pat in ['konsole.*tabtitle=Hermes-Gauntlet-TUI', 'chrome.*hermes_chrome_gauntlet', 'placeholder.py']:
        try:
            for p in subprocess.check_output(['flatpak-spawn', '--host', 'pgrep', '-f', pat], text=True).split():
                if int(p) not in SAFE: subprocess.run(['flatpak-spawn', '--host', 'kill', '-9', str(p)], capture_output=True)
        except subprocess.CalledProcessError: pass

def tile_windows():
    js = "var w=workspace.windowList();for(var i=0;i<w.length;i++){var c=(w[i].caption||'').toLowerCase();if(c.indexOf('hermes-gauntlet-tui')!==-1||c.indexOf('splatbox')!==-1||c.indexOf('awaiting')!==-1){w[i].keepBelow=true;}}"
    with open('/tmp/tile_pair.js', 'w') as f: f.write(js)
    subprocess.run(['flatpak-spawn', '--host', '/usr/bin/qdbus-qt6', 'org.kde.KWin', '/Scripting', 'org.kde.kwin.Scripting.loadScript', '/tmp/tile_pair.js', 'tile_pair'], capture_output=True)
    subprocess.run(['flatpak-spawn', '--host', '/usr/bin/qdbus-qt6', 'org.kde.KWin', '/Scripting/Script0', 'org.kde.kwin.Script.run'], capture_output=True)
    subprocess.run(['flatpak-spawn', '--host', '/usr/bin/qdbus-qt6', 'org.kde.KWin', '/Scripting', 'org.kde.kwin.Scripting.unloadScript', 'tile_pair'], capture_output=True)

def launch_session(model="gemma-4-E4B-it-qat-exact"):
    kill_targets(); subprocess.run(['rm', '-rf', '/tmp/hermes_chrome_gauntlet']); time.sleep(1)
    subprocess.Popen(['flatpak-spawn', '--host', 'python3', str(BENCH / 'placeholder.py')])
    p_text = (BENCH / 'PROMPT_ICM.txt').read_text()
    subprocess.Popen(['flatpak-spawn', '--host', '/usr/bin/konsole', '--separate',
        '-p', 'tabtitle=Hermes-Gauntlet-TUI', '-p', 'TerminalColumns=115', '-p', 'TerminalRows=50',
        '-p', 'Font=Liberation Mono,8', '--qwindowgeometry', '960x1080+0+0', '--workdir', str(BENCH),
        '-e', 'distrobox', 'enter', 'ws-hermes', '--', 'hermes', 'chat',
        '--in', str(BENCH), '-m', model, '--skills', 'icm-architect', '--accept-hooks', '--tui', '--yolo',
        '-q', p_text])
    time.sleep(2); tile_windows()

if __name__ == '__main__':
    act = sys.argv[1] if len(sys.argv) > 1 else 'status'
    if act == 'kill': kill_targets(); print("Cleaned Gauntlet windows.")
    elif act == 'launch': launch_session(sys.argv[2] if len(sys.argv) > 2 else 'gemma-4-E4B-it-qat-exact'); print("Launched session.")
    elif act == 'tile': tile_windows(); print("Tiled.")
