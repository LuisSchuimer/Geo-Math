import curses
from utils import draw_line

def initWindow(x, y, x_start, y_start):
    try:
        console_win = curses.newwin(y, x, y_start, x_start)

        _, width = console_win.getmaxyx()
        console_win.addstr(1, 1, "CONSOLE", curses.A_STANDOUT)
        console_win.refresh()
        draw_line(console_win, 2, width)

        return console_win

    except Exception as e:
        return e

def display(window):
    height, width = window.getmaxyx()
    window.addstr(3, 1, ">")
    
    text_box_y = height - 3
    text_box_y = width - 1