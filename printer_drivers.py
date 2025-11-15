import win32print

PRINTER_NAME = "POS-58 Printer"   # <- Change to printer name as stated in device manager

def print_text(text: str):
    hPrinter = win32print.OpenPrinter(PRINTER_NAME)

    try:
        win32print.StartDocPrinter(
            hPrinter,
            1,
            ("Python print_text", None, "RAW")
        )
        win32print.StartPagePrinter(hPrinter)

        data = text.encode("cp437", errors="replace")
        win32print.WritePrinter(hPrinter, data)

        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)

if __name__ == "__main__":
    print_text("Trust")