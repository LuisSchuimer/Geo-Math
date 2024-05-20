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

def display(coordinates, dimentions_c_s, info_win, rate, variables):
    # Clear screen
    info_win.clear()

    # Define color pair 1 with red text on black background
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    # Define color pair 2 with green text on black background
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # Define color pair 3 with yellow text on black background
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    RED = curses.color_pair(1)
    GREEN = curses.color_pair(2)
    YELLOW = curses.color_pair(3)

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
        if coordinate[2]:
            info_win.addstr(line, 2, f"X ({coordinate[0]}|{coordinate[1]})", GREEN)
        else:
            info_win.addstr(line, 2, f"X ({coordinate[0]}|{coordinate[1]})", RED)
        line += 1

    info_win.addstr(line+2, 1, f"Variables")
    line += 3
    draw_line(info_win, line, width)
    line +=1

    for variable in variables.keys():
        if variables[variable]:
            info_win.addstr(line, 2, f"{variable} = {variables[variable]}")
        else:
            info_win.addstr(line, 2, f"{variable} = ?", YELLOW)

        line += 1

    

    # Add Title
    info_win.addstr(line +2, 1, f"Functions")
    draw_line(info_win, line+3, width)

    line = line + 4
    functions = list(coordinates()['F'].keys())
    for function in functions:
        if not coordinates()['F'][function]:
            info_win.addstr(line, 2, f"f(x)={function}", RED)
        else:
            info_win.addstr(line, 2, f"f(x)={function}")
        draw_line(info_win, line+1, width)
        line += 2
        #for coordinate in coordinates()['F'][function]:
        #    if coordinate[2]:
        #        info_win.addstr(line, 4, f"X ({round(coordinate[0], 2)}|{round(coordinate[1], 2)})")
        #        line += 1 
        line += 1

    
    info_win.border()
    info_win.refresh()