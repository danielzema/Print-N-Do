import serial          
import time            

SERIAL_PORT = "COM4" # <- change to Bluetooth port

ESC_BOLD_ON = b'\x1b\x45\x01'   # Enable bold
ESC_BOLD_OFF = b'\x1b\x45\x00'  # Disable bold

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

# Print text with one word in bold
def print_text_with_bold(text: str, bold_word: str):
    """Print text with one word bolded."""
    if not bold_word or bold_word not in text:
        print_text(text)
        return
    
    # Split text around the bold word and build bytes with bold commands
    parts = text.split(bold_word)
    result = parts[0].encode("cp437", errors="replace")
    result += ESC_BOLD_ON + bold_word.encode("cp437", errors="replace") + ESC_BOLD_OFF
    result += parts[1].encode("cp437", errors="replace") if len(parts) > 1 else b""
    result += b"\n\n\n\n"
    send_to_printer(result)

if __name__ == "__main__":
    print_text("Hello")