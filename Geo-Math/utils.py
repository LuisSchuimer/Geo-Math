import curses

def draw_line(window, line, width):
    for i in range(width):
            window.addstr(line, i, "_")