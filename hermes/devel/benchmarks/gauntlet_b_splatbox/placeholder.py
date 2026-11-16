import gi, sys, urllib.request
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

stage = sys.argv[1] if len(sys.argv) > 1 else "1"
sub = {
    "1": "Stage 1: Hermes Analyzing Wall Occlusion & Vision Filtering...",
    "2": "Stage 2: Calibrating Weapon Angles & Ballistics Drop...",
}.get(stage, "Stage 3: Preparing Autonomous Match...")

app = Gtk.Application(application_id='com.hermes.gauntlet.standby')

def on_activate(a):
    win = Gtk.ApplicationWindow(application=a, title="Arena Standby - Awaiting Hermes Launch")
    win.set_default_size(960, 1080)
    win.override_background_color(Gtk.StateFlags.NORMAL,
        __import__('gi.repository.Gdk', fromlist=['RGBA']).RGBA(0.055, 0.067, 0.09, 1.0))
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
    box.set_margin_top(300)
    l1 = Gtk.Label(label="Gauntlet B: Splatbox 3D WebGPU Arena")
    l1.set_markup('<span foreground="#4285f4" font="24" weight="bold">Gauntlet B: Splatbox 3D WebGPU Arena</span>')
    l2 = Gtk.Label(label=sub)
    l2.set_markup(f'<span foreground="#9aa0a6" font="14">{sub}</span>')
    box.pack_start(l1, False, False, 0)
    box.pack_start(l2, False, False, 0)
    win.add(box)
    win.show_all()
    GLib.timeout_add(300, _poll, a)

def _poll(a):
    try:
        urllib.request.urlopen("http://127.0.0.1:9222/json/version", timeout=0.2)
        a.quit(); return False
    except Exception:
        return True

app.connect('activate', on_activate)
app.run(None)
