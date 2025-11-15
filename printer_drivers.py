import win32print

PRINTER_NAME = r"POS-58 Printer"  # <- replace with printers name in device manager

def print_text(text: str):
    print(f"Opening printer.")
    hPrinter = win32print.OpenPrinter(PRINTER_NAME)

    try:
        doc_info = ("Python POS Test", None, "RAW")
        win32print.StartDocPrinter(hPrinter, 1, doc_info)
        win32print.StartPagePrinter(hPrinter)

        payload = text + "\n\n\n"
        data = payload.encode("cp437", errors="replace")

        win32print.WritePrinter(hPrinter, data)

        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
        print("Done sending to printer.")
    finally:
        win32print.ClosePrinter(hPrinter)

if __name__ == "__main__":
    print_text("Trust")
