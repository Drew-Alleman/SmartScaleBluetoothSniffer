import asyncio
from bleak import BleakScanner

TARGET_MAC = "A8:0B:6B:F4:23:38"
STEPPED_ON_HEX = "00000000000024000000000000"

async def discover_scale(timeout: float = 5.0) -> str | None:
    """
    Scans for BLE advertisers and returns the MAC of the first device that
    broadcasts manufacturer data matching STEPPED_ON_HEX.
    """
    while True:
        devices = await BleakScanner.discover(timeout=timeout)

        for d in devices:
            # bleak exposes advertisement details via metadata (best-effort)
            md = (d.metadata or {})
            mfg = md.get("manufacturer_data") or {}

            for _company_id, payload in mfg.items():
                if payload.hex() == STEPPED_ON_HEX:
                    print(f"[+] Found scale: {d.address} ({d.name})")
                    return d.address

def get_weight_from_bytes(data: bytes) -> tuple[float, float]:
    weight_raw = int.from_bytes(data, byteorder="big") 
    weight_kg = weight_raw / 100.0 
    weight_lb = weight_kg * 2.2046226218  
    return weight_kg, weight_lb  

def detection_callback(device, advertisement_data):
    if device.address.upper() != TARGET_MAC:
        return

    mfg = advertisement_data.manufacturer_data
    if not mfg:
        return

    for _, data in mfg.items():
        hex_data = data.hex()
        if hex_data == STEPPED_ON_HEX:
            print("[+] Scale has been stepped on")
            continue

        kg, lb = get_weight_from_bytes(data[0:2])
        print(f"[+] User weighed in at {kg}kgs {lb}lbs")

async def main():
    scanner = BleakScanner(detection_callback)
    print("[+] Listening for scale updates... (ctrl+C to stop)")

    try:
        await scanner.start()
        while True:
            await asyncio.sleep(1)
    except (KeyboardInterrupt, asyncio.CancelledError):
        print("\n[-] Stopping scanner...")
    finally:
        await scanner.stop()
        print("[+] Scanner stopped cleanly")

asyncio.run(main())

