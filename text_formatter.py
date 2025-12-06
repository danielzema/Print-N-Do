MAX_WIDTH = 32

def format_test_width():
    lines = []
    for i in range(30, MAX_WIDTH + 1):
        lines.append("-" * i)
    return "\n".join(lines)

def test_printer_width():
    return format_test_width()