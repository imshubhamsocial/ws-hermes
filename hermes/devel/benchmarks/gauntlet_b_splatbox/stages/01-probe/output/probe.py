import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

out = Path("output")
out.mkdir(exist_ok=True)

with sync_playwright() as p:
    # Connect to CDP
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    
    # Find tab and bring to front
    page = next(pg for ctx in browser.contexts for pg in ctx.pages if "splatbox" in pg.url)
    page.bring_to_front()
    
    # Screenshot menu
    page.screenshot(path=str(out / "menu_frame.png"))
    
    # Click play
    play_btn = page.locator("#play")
    if play_btn.is_visible():
        play_btn.click()
        time.sleep(0.6)
        
    # Evaluate state and extract HUD
    state = page.evaluate("""() => ({
        pointer_lock_active: document.pointerLockElement !== null,
        viewport: {width: window.innerWidth, height: window.innerHeight},
        hud: {
            score: document.querySelector('#score')?.innerText || '0',
            timer: document.querySelector('#timer')?.innerText || '60',
            ammo: document.querySelector('#ammo')?.innerText || '40 / 40'
        }
    })""")
    
    # Screenshot playing
    page.screenshot(path=str(out / "playing_frame.png"))
    
    # Write state JSON
    (out / "probe_state.json").write_text(json.dumps(state, indent=2))
