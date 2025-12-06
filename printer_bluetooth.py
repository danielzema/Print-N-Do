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

# Convert string to bytes
def print_text(text: str):
    payload = text + "\n\n\n\n" 
    data = payload.encode("cp437", errors="replace")
    send_to_printer(data)

if __name__ == "__main__":
    print_text("Hello")