#!/usr/bin/env python3
"""Stage 04 Headless CDP WebGL2 Telemetry Harvester (<60 lines)."""
import asyncio, http.server, json, pathlib, socketserver, threading
from playwright.async_api import async_playwright

class QuietServer(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args): pass

def run_server():
    server = socketserver.TCPServer(("127.0.0.1", 8899), QuietServer)
    server.serve_forever()

async def evaluate():
    threading.Thread(target=run_server, daemon=True).start()
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            args=["--use-gl=angle", "--use-angle=swiftshader"]
        )
        page = await browser.new_page()
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        await page.goto("http://127.0.0.1:8899/output/aquarium-sim/index.html")
        await page.wait_for_timeout(2000)
        telem = await page.evaluate("window.__AQUARIUM_TELEMETRY__")
        telem["consoleErrors"] = len(errors)
        await browser.close()
    out = pathlib.Path("stages/04-verify/output/cdp_telemetry.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(telem, indent=2), encoding="utf-8")
    print(f"TELEMETRY_RECORDED: {telem}")

if __name__ == "__main__":
    asyncio.run(evaluate())
