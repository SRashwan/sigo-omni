import asyncio
import websockets
import serial
import serial.tools.list_ports
import sys

# Configuration
PORT = 8765
BAUD_RATE = 115200

print(f"--- SIGO OMNI HARDWARE BRIDGE ---")
print(f"1. Connect your Arduino via USB.")
print(f"2. Keep this window open.")
print(f"---------------------------------")

# 1. Auto-detect Arduino
arduino_port = None
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if "Arduino" in p.description or "CH340" in p.description or "USB Serial" in p.description:
        arduino_port = p.device
        print(f"[+] Found Arduino on {arduino_port}")
        break

if not arduino_port:
    print("[-] Arduino not found automatically.")
    print("Available ports:")
    for p in ports: print(f" - {p.device} ({p.description})")
    arduino_port = input("Enter COM port manually (e.g., COM3): ").strip()

try:
    ser = serial.Serial(arduino_port, BAUD_RATE, timeout=0.1)
    print(f"[+] Serial connection established on {arduino_port}")
except Exception as e:
    print(f"[!] Error opening serial: {e}")
    sys.exit(1)

connected_clients = set()

async def handler(websocket):
    print(f"[+] Web Client Connected")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Web -> Arduino (Output Control)
            if ser.is_open:
                # Expecting value 0-100 or byte
                try:
                    val = int(float(message)) # Clean input
                    ser.write(bytes([val]))
                except:
                    pass
    except:
        pass
    finally:
        connected_clients.remove(websocket)
        print("[-] Web Client Disconnected")

async def serial_reader():
    print(f"[+] Bridge Ready: ws://localhost:{PORT}")
    while True:
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8').strip()
                if line.startswith("D:"):
                    # Broadcast to all web clients
                    val = line.split(":")[1]
                    if connected_clients:
                        # Create tasks for all sends to avoid blocking
                        await asyncio.gather(
                            *[ws.send(val) for ws in connected_clients],
                            return_exceptions=True
                        )
            except Exception as e:
                print(f"Serial Read Error: {e}")
        await asyncio.sleep(0.01)

async def main():
    async with websockets.serve(handler, "localhost", PORT):
        await serial_reader()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Stopping Bridge...")