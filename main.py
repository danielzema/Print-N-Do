import printer_bluetooth
import text_formatter

def main(): 
    header_text, header_bold = text_formatter.format_reciept_header_quote()
    body_text, body_bold = text_formatter.format_single_task_body_user_input()
    footer_text, footer_bold = text_formatter.format_single_task_footer()
    
    full_text = header_text + "\n" + body_text + "\n" + footer_text
    bold_words = []
    if isinstance(header_bold, list):
        bold_words.extend(header_bold)
    elif header_bold:
        bold_words.append(header_bold)
    if body_bold:
        bold_words.append(body_bold)
    if footer_bold:
        bold_words.append(footer_bold)
    
    if bold_words:
        printer_bluetooth.print_text_with_bold(full_text, bold_words)
    else:
        printer_bluetooth.print_text(full_text)

if __name__ == "__main__":
    main()