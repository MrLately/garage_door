import time
import network
import uasyncio as asyncio
from machine import Pin
import ujson as json

led = Pin("LED", Pin.OUT, value=1)
pin_up = Pin(20, Pin.OUT, value=0)
pin_down = Pin(17, Pin.OUT, value=0)
pin_stop = Pin(18, Pin.OUT, value=0)

ssid = 'TODO'
password = 'TODO'

check_interval_sec = 0.25

wlan = network.WLAN(network.STA_IF)

def get_manifest_json():
    manifest = {
        "name": "Garage Door Controller",
        "short_name": "GarageDoor",
        "display": "standalone",
        "theme_color": "#4A90E2",
        "background_color": "#4A90E2",
        "icons": [
            {
                "src": "icon.png",
                "type": "image/png",
                "sizes": "192x192"
            }
        ]
    }
    return json.dumps(manifest)


html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        html {
            font-family: Helvetica;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }
        .button, .homeButton {
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        .buttonRed {
            background-color: #d11d53;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        .homeButton {
            background-color: #008cba;
            border: none; /* Different color for home button */
        }
    </style>
    <link rel="manifest" href="/manifest.json">
</head>
<body>
    <center>
        <h1>Garage Door Controller</h1>
    </center>
    <br><br>
    <form>
        <center>
            <button class="button" name="DOOR" value="UP" type="submit">Door UP</button><br><br>
            <button class="buttonRed" name="DOOR" value="STOP" type="submit">STOP</button><br><br>
            <button class="button" name="DOOR" value="DOWN" type="submit">Door DOWN</button><br><br>
            <a href="http://192.168.1.3:5000" class="homeButton">Home Dashboard</a>  <!-- Home button link -->
        </center>
    </form>
    <br><br>
    <p>Last command issued was %s</p>
</body>
</html>
"""

def blink_led(frequency=0.5, num_blinks=3):
    for _ in range(num_blinks):
        led.on()
        time.sleep(frequency)
        led.off()
        time.sleep(frequency)

def control_door(cmd):
    if cmd == 'stop':
        pin_stop.on()
        blink_led(0.1, 1)
        pin_stop.off()
        
    if cmd == 'up':
        pin_up.on()
        blink_led(0.1, 1)
        pin_up.off()
    
    if cmd == 'down':
        pin_down.on()
        blink_led(0.1, 1)
        pin_down.off()

async def connect_to_wifi():
    wlan.active(True)
    wlan.config(pm = 0xa11140)
    wlan.connect(ssid, password)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('waiting for connection...')
        time.sleep(1)

    if wlan.status() != 3:
        blink_led(0.1, 10)
        raise RuntimeError('WiFi connection failed')
    else:
        blink_led(0.5, 2)
        print('connected')
        status = wlan.ifconfig()
        print('ip = ' + status[0])

async def serve_client(reader, writer):
    print("Client connected")
    request_line = await reader.readline()
    print("Request:", request_line)
    while await reader.readline() != b"\r\n":
        pass

    request = str(request_line)
    if '/manifest.json' in request:
        manifest_data = get_manifest_json()
        writer.write('HTTP/1.0 200 OK\r\nContent-type: application/manifest+json\r\n\r\n')
        writer.write(manifest_data.encode())
    elif '/icon.png' in request:
        try:
            with open('icon.png', 'rb') as f:
                icon_data = f.read()
            writer.write(b'HTTP/1.0 200 OK\r\nContent-Type: image/png\r\n\r\n' + icon_data)
        except FileNotFoundError:
            writer.write(b'HTTP/1.0 404 Not Found\r\n\r\n')
    else:
        cmd_up = request.find('DOOR=UP')
        cmd_down = request.find('DOOR=DOWN')
        cmd_stop = request.find('DOOR=STOP')

        stateis = ""
        if cmd_stop == 8:
            stateis = "Door: STOP"
            control_door('stop')
        elif cmd_up == 8:
            stateis = "Door: UP"
            control_door('up')
        elif cmd_down == 8:
            stateis = "Door: DOWN"
            control_door('down')

        response = html % (stateis)
        writer.write('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        writer.write(response.encode())

    await writer.drain()
    await writer.wait_closed()

async def main():
    print('Connecting to WiFi...')
    asyncio.create_task(connect_to_wifi())

    print('Setting up webserver...')
    asyncio.create_task(asyncio.start_server(serve_client, "0.0.0.0", 80))

    while True:
        await asyncio.sleep(check_interval_sec)

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()
