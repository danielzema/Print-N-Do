import time

MAX_WIDTH = 30
MAX_TEXT_SPACE = MAX_WIDTH - 1 

def format_test_width():
    lines = []
    for i in range(30, MAX_WIDTH + 1):
        lines.append("-" * i)
    return "\n".join(lines)

def test_printer_width():
    return format_test_width()

def top_bottom_border(): 
    return "+" + "-" * MAX_WIDTH + "+"

def empty_line():
    return "|" + " " * MAX_WIDTH + "|"

def padded_text_left(text):
    lines = wrap_text(text)
    result = []
    for line in lines:
        if len(line) > MAX_TEXT_SPACE:
            result.append("| " + line[:MAX_TEXT_SPACE] + "|")
        else:
            padding = MAX_TEXT_SPACE - len(line)
            result.append("| " + line + " " * padding + "|")
    return "\n".join(result)

def padded_text_middle(text, bold=False):
    total_padding = MAX_WIDTH - len(text)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    formatted = "|" + " " * left_padding + text + " " * right_padding + "|"
    # Return tuple for printer: (formatted_text, word_to_bold)
    return (formatted, text if bold else None)

# TODO Add error handling for text longer than MAX_WIDTH
def wrap_text(text):
    if not text:
        return [""]
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if not current_line:
            current_line = word
        elif len(current_line) + 1 + len(word) <= MAX_WIDTH:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word 
    if current_line:
        lines.append(current_line)
    
    return lines

def format_single_task():
    """Build the complete task receipt as strings. Returns (text, bold_word)."""
    lines = []
    lines.append(top_bottom_border())
    
    # Header with bold MOTIVATION
    motivation_line, bold_word = padded_text_middle("MOTIVATION", bold=True)
    lines.append(motivation_line)
    
    lines.append(empty_line())
    lines.append(padded_text_left("Date: " + time.strftime("%A, " +"%d-%m-%Y")))
    lines.append(padded_text_left("Time: " + time.strftime("%H:%M")))
    lines.append(empty_line())
    
    # Body
    lines.append(padded_text_left("Task"))
    lines.append(padded_text_left(len("Task") * "-"))
    lines.append(empty_line())
    
    lines.append(top_bottom_border())
    
    full_text = "\n".join(lines)
    return (full_text, bold_word)

if __name__ == "__main__":
    text, bold_word = format_single_task()
    print(text)