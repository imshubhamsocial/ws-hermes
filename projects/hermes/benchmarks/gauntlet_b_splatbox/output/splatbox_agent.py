import asyncio
import json
import websockets
import time
import os
import urllib.request

# Configuration
CDP_HTTP_URL = "http://127.0.0.1:9222/json"
OUTPUT_TELEMETRY_PATH = "output/telemetry.json"
PLAY_BUTTON_SELECTOR = "#play"
SCORE_SELECTOR = "span#score"
TIMER_SELECTOR = "span#timer"
AMMO_SELECTOR = "span#ammo"
ROUND_DURATION = 60

async def get_websocket_url():
    """Fetches the webSocketDebuggerUrl and extracts the pageId for the Splatbox tab from the CDP HTTP endpoint."""
    try:
        with urllib.request.urlopen(CDP_HTTP_URL, timeout=5) as response:
            data = json.loads(response.read().decode())
            
            # Filter for the Splatbox tab
            splatbox_targets = [
                t for t in data if t.get('title') == "Splatbox: paintball in your browser"
            ]
            
            if splatbox_targets:
                # Use the first found Splatbox target
                url = splatbox_targets[0].get('webSocketDebuggerUrl')
                # Extract pageId from the URL: .../devtools/page/PAGE_ID
                page_id = url.split('/')[-1]
                return url, page_id
            else:
                print("Error: No Splatbox tab found in CDP targets.")
                return None, None
    except urllib.error.URLError as e:
        print(f"Error connecting to CDP HTTP endpoint at {CDP_HTTP_URL}. Ensure Chrome Dev Tools is running on 9222. Details: {e}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred during URL fetching: {e}")
        return None, None

async def run_splatbox_round(websocket_url, page_id):
    if not websocket_url or not page_id:
        return None
        
    print(f"Attempting to connect to CDP via WebSocket at {websocket_url}")
    try:
        async with websockets.connect(websocket_url) as websocket:
            print("Successfully connected to CDP.")
            
            # 3. Check for #play button existence and visibility
            print("Checking for #play button...")
            check_script = f"document.querySelector('{PLAY_BUTTON_SELECTOR}') !== null && window.getComputedStyle(document.querySelector('{PLAY_BUTTON_SELECTOR}')).display !== 'none'"
            await websocket.send(json.dumps({"id": 3, "method": "Runtime.evaluate", "params": {"expression": check_script, "contextId": page_id}}))
            response = await websocket.recv()
            print(f"CDP Response (Check #play): {response}")
            is_play_button_present = json.loads(response)['result']['result']['value']
            
            if not is_play_button_present:
                print(f"Error: Play button ({PLAY_BUTTON_SELECTOR}) is not visible or present on the page. Cannot proceed.")
                return None

            # 4. Engage PointerLock by dispatching native CDP mouse events
            print("Bringing tab to front...")
            await websocket.send(json.dumps({"id": 4, "method": "Page.bringToFront", "params": {}}))
            response = await websocket.recv()
            print(f"CDP Response (Page.bringToFront): {response}")
            
            # 5. Get #play button bounds dynamically
            print("Querying #play button bounds...")
            bounds_script = "document.querySelector('#play').getBoundingClientRect()"
            await websocket.send(json.dumps({"id": 5, "method": "Runtime.evaluate", "params": {"expression": bounds_script, "contextId": page_id}}))
            response = await websocket.recv()
            # Unpack using full nested path: response['result']['result']['value']
            play_bounds = json.loads(response)['result']['result']['value']
            
            # Calculate center coordinates
            center_x = play_bounds['left'] + play_bounds['width'] / 2
            center_y = play_bounds['top'] + play_bounds['height'] / 2
            print(f"Calculated play button center: ({center_x}, {center_y})")

            # 6. Engage PointerLock by dispatching native CDP mouse events
            print("Dispatching CDP mouse events to engage PointerLock.")
            
            # Mouse Pressed
            await websocket.send(json.dumps({"id": 6, "method": "Input.dispatchMouseEvent", "params": {"type": "mousePressed", "x": center_x, "y": center_y, "button": "left", "buttons": 1, "clickCount": 1}}))
            response = await websocket.recv()
            print(f"CDP Response (Input.dispatchMouseEvent - Pressed): {response}")

            # Mouse Released
            await websocket.send(json.dumps({"id": 7, "method": "Input.dispatchMouseEvent", "params": {"type": "mouseReleased", "x": center_x, "y": center_y, "button": "left", "buttons": 0, "clickCount": 1}}))
            response = await websocket.recv()
            print(f"CDP Response (Input.dispatchMouseEvent - Released): {response}")
            
            # 7. Run 60-second round (Simulated loop for capture/tracking/slewing)
            print(f"Starting {ROUND_DURATION} second round...")
            start_time = time.time()
            
            while time.time() - start_time < ROUND_DURATION:
                # Simulate action and capture
                await asyncio.sleep(1) 
                # Capture screenshot (example)
                await websocket.send(json.dumps({"id": 8, "method": "Page.captureScreenshot", "params": {"format": "png"}}))
                response = await websocket.recv()
                print(f"CDP Response (Page.captureScreenshot): {response}")
                
            print("Round finished.")
            
            # 8. Extract real telemetry from the live DOM nodes
            print("Extracting telemetry from DOM...")
            
            async def get_dom_text(selector):
                await websocket.send(json.dumps({"id": 9, "method": "Runtime.evaluate", "params": {"expression": f"document.querySelector('{selector}').innerText", "contextId": page_id}}))
                response = await websocket.recv()
                print(f"CDP Response (Runtime.evaluate for {selector}): {response}")
                return json.loads(response)['result']['result']['value']

            score = await get_dom_text(SCORE_SELECTOR)
            timer = await get_dom_text(TIMER_SELECTOR)
            ammo = await get_dom_text(AMMO_SELECTOR)
            
            telemetry = {
                "score": score,
                "timer": timer,
                "ammo": ammo,
                "timestamp": time.time()
            }
            
            # 9. Write telemetry to output/telemetry.json
            with open(OUTPUT_TELEMETRY_PATH, 'w') as f:
                json.dump(telemetry, f, indent=2)
            print(f"Telemetry written to {OUTPUT_TELEMETRY_PATH}")
            
            return telemetry

if __name__ == "__main__":
    # 1. Get the dynamic WebSocket URL and pageId
    websocket_url, page_id = asyncio.run(get_websocket_url())
    
    # 2. Run the round with the dynamic URL and pageId
    telemetry_data = asyncio.run(run_splatbox_round(websocket_url, page_id))
    
    if telemetry_data:
        print("--- Execution Complete ---")
        print(f"Final Telemetry: {telemetry_data}")
    else:
        print("--- Execution Failed ---")