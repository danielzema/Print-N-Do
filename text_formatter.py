import time

MAX_WIDTH = 30
MAX_TEXT_SPACE = MAX_WIDTH - 2 

def top_bottom_border(): 
    return "+" + "-" * MAX_WIDTH + "+"

def empty_line():
    return "|" + " " * MAX_WIDTH + "|"

def padded_text_left(text, bold=False):
    lines = wrap_text(text)
    result = []
    for line in lines:
        if len(line) > MAX_TEXT_SPACE:
            result.append("| " + line[:MAX_TEXT_SPACE] + " |")
        else:
            padding = MAX_TEXT_SPACE - len(line)
            result.append("| " + line + " " * padding + " |")
    return ("\n".join(result), text if bold else None)

def padded_text_middle(text, bold=False):
    total_padding = MAX_WIDTH - len(text)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    formatted = "|" + " " * left_padding + text + " " * right_padding + "|"
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
        elif len(current_line) + 1 + len(word) <= MAX_TEXT_SPACE:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word 
    if current_line:
        lines.append(current_line)
    
    return lines

def format_single_task_header():
    lines = []
    lines.append(top_bottom_border())
    
    motivation_line, bold_word = padded_text_middle("MOTIVATION", bold=True)
    lines.append(motivation_line)
    
    lines.append(empty_line())
    date_line, _ = padded_text_left("Date: " + time.strftime("%A, " +"%d-%m-%Y"))
    lines.append(date_line)
    time_line, _ = padded_text_left("Time: " + time.strftime("%H:%M"))
    lines.append(time_line)
    lines.append(empty_line())

    full_text = "\n".join(lines)
    return (full_text, bold_word)

def format_single_task_body():
    lines = []
    task_line, bold_word = padded_text_left("Task information", bold=True)
    lines.append(task_line)
    separator_line, _ = padded_text_left(len("Task information") * "-")
    lines.append(separator_line)
    lines.append(empty_line())
    
    title_line, _ = padded_text_left("Lecture 25")
    lines.append(title_line)
    lines.append(empty_line())
    desc_line, _ = padded_text_left("Description: bla bla blab alblabalbalba balab ablabalab f fffe")
    lines.append(desc_line)
    lines.append(empty_line())
    due_line, _ = padded_text_left("Due: Tuesday 12-12/2025 at 19:25")
    lines.append(due_line)
    lines.append(empty_line())
    full_text = "\n".join(lines)
    return (full_text, bold_word)

def format_single_task_footer(): 
    lines = []
    lines.append(top_bottom_border())
    lines.append(empty_line())
    footer_line, bold_word = padded_text_left("Check when completed: " + "[ ]")
    lines.append(footer_line)
    lines.append(empty_line())
    lines.append(top_bottom_border())
 
    full_text = "\n".join(lines)
    return (full_text, bold_word)

def format_single_task():
    header_text, header_bold = format_single_task_header()
    body_text, body_bold = format_single_task_body()
    footer_text, footer_bold = format_single_task_footer()
    
    full_text = header_text + "\n" + body_text + "\n" + footer_text
    # List comprehension
    bold_words = [word for word in [header_bold, body_bold, footer_bold] if word]
    
    return (full_text, bold_words)

if __name__ == "__main__":
    text, bold_words = format_single_task()
    print(text)