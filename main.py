import printer_bluetooth
import text_formatter

def main(): 
    text, bold_word = text_formatter.format_single_task()
    if bold_word:
        printer_bluetooth.print_text_with_bold(text, bold_word)
    else:
        printer_bluetooth.print_text(text)

if __name__ == "__main__":
    main()