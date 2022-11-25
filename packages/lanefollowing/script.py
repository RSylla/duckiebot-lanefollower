from smbus2 import SMBus
import os


message = f"Hello from {os.environ['VEHICLE_NAME']}"
print(message)

with SMBus(12) as bus:
    bus.pec = 1  # Enable PEC
    b = bus.read_byte_data(0x3e, 0x11)
    print(b)

