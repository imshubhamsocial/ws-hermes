import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

out = Path("output")
out.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
    # Locate tab containing splatbox
    page = next(pg for ctx in browser.contexts for pg in ctx.pages if "splatbox" in pg.url)
    page.bring_to_front()
    
    # Step 1: Initial Screenshot
    page.screenshot(path=str(out / "menu_frame.png"))
    
    # Step 2: Attempt to engage PointerLock
    play_btn = page.locator("#play")
    if play_btn.is_visible():
        play_btn.click() # Dispatches native trusted CDP mouse gesture
        time.sleep(0.5)
        
    # Step 3: Evaluate state and extract HUD
    state = page.evaluate("""() => ({
        pointer_lock_active: document.pointerLockElement !== null,
        viewport: {width: window.innerWidth, height: window.innerHeight},
        hud: {
            score: document.querySelector('#score')?.innerText || '0',
            timer: document.querySelector('#timer')?.innerText || '60',
            ammo: document.querySelector('#ammo')?.innerText || '40 / 40'
        }
    })""")
    
    # Step 4: Post-game screenshot and state saving
    page.screenshot(path=str(out / "playing_frame.png"))
    (out / "probe_state.json").write_text(json.dumps(state, indent=2))