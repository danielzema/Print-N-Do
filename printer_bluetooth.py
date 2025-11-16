import serial          
import time            

SERIAL_PORT = "COM4" # <- change to Bluetooth port

def send_to_printer(data: bytes):
    # Open the serial connection to the printer.
    # "with" automatically closes the port.

    # Create object
    with serial.Serial(
        SERIAL_PORT,     
        # Speed
        baudrate=9600,
        # Data size
        bytesize=8,      
        # No parity bits needed?
        parity="N",       
        # One stop bit to tell serial communication that session is over.
        # change to 2 if channel is noisy
        stopbits=1,       
        timeout=1    
    ) as ser:
        
        ser.write(data)   
        # Force data to leave buffer
        ser.flush()      
        
        # Printer needs delay or it wont work all the time...
        time.sleep(0.3) 

if __name__ == "__main__":
    # Have to send bytes.
    send_to_printer(b"\n\nHello\n\n")
