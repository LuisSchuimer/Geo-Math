import curses
from utils import draw_line


def initWindow(y:int, x:int, end_x:int):
    global width, height
    try:
        # Init Info-Window
        info_win = curses.newwin(y, x, 1, end_x)

        # Get width
        height, width = info_win.getmaxyx()


        # Return info_win object
        return info_win
    except:
        # Return false if error
        return False

def display(coordinates, dimentions_c_s, info_win, rate):
    # Clear screen
    info_win.clear()

    # Define page-end
    page_end = height-4

    # Title
    info_win.addstr(1, 1, "INFO-WINDOW", curses.A_STANDOUT)
    draw_line(info_win, 2, width)

    draw_line(info_win, height-4, width)
    info_win.addstr(height-3, 2, f"RATE X/Y: {rate[0]}|{rate[1]} units", curses.A_STANDOUT)
    info_win.addstr(height-2, 2, f"COORDINATE-SYSTEM WINDOW: {dimentions_c_s()[0]}x{dimentions_c_s()[1]}", curses.A_STANDOUT)

    # Add Title
    info_win.addstr(5, 1, f"Points")
    draw_line(info_win, 6, width)

    # Display all coordinates
    line = 7
    for coordinate in coordinates()['P']:
        info_win.addstr(line, 2, f"X ({coordinate[0]}|{coordinate[1]})")
        line += 1
    
    info_win.border()
    info_win.refresh()