import serial
import time

SERIAL_PORT = "COM4"   # <- change to Bluetooth port

def send_to_printer(data: bytes):
    with serial.Serial(
        SERIAL_PORT,
        baudrate=9600, 
        bytesize=8,
        parity="N",
        stopbits=1,
        timeout=1
    ) as ser:
        ser.write(data)
        ser.flush()
        time.sleep(0.3)

if __name__ == "__main__":
    # convert to bytes
    send_to_printer(b"Hello\n\n")
