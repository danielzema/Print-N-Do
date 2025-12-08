MAX_WIDTH = 30

def format_test_width():
    lines = []
    for i in range(30, MAX_WIDTH + 1):
        lines.append("-" * i)
    return "\n".join(lines)

def test_printer_width():
    return format_test_width()

def top_bottom_bordet(): 
    print("+" + "-" * MAX_WIDTH + "+")

def empty_line():
    print("|" + " " * MAX_WIDTH + "|")

def padded_text_left(text):
    print("| " + text + " " * (MAX_WIDTH - len(text) - 1) + "|")

def padded_text_middle(text):
    total_padding = MAX_WIDTH - len(text)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    print("|" + " " * left_padding + text + " " * right_padding + "|")

def print_header_single_task():
    top_bottom_bordet()
    empty_line()
    padded_text_left("Hello")
    padded_text_middle("Hello")



if __name__ == "__main__":
    print_header_single_task()
    # print(len(""))