from curses import wrapper
import coordinate_system
import info_window
import curses
from curses.textpad import Textbox, rectangle
    

def main(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Initilise window for coordinate-system

    x = 100
    y = 47
    window = False

    while not window:
        # Try init
        window = coordinate_system.initScreen(x, y)

        if not window:
            if x != 20:
                y -= 1
                if y == 0:
                    x -= 1
                    y = 60
            else:
                # Trow a exception
                Exception("Could not initilise Coordinate-System screen")
    
    # Initilise the info-window
    remaining_width = 1 + x
    x = int(round(remaining_width / 2, 1))
    info_win = info_window.initWindow(height -2, x, remaining_width)


    coordinate_system.draw_coordinate_system(window, space_x=4, space_y=2)
    coordinate_system.new_coordinate([3, 5])
    coordinate_system.new_coordinate([2, 3])
    coordinate_system.new_coordinate([-2, 2])
    coordinate_system.new_coordinate([-7, 3])
    coordinate_system.draw(window)

    info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, info_win)

    window.border()
    window.refresh()
    info_win.border()
    info_win.refresh()
    window.getch()
    curses.endwin()

print("GEO-MATH | Coordinate-System | C2024 Luis Schuimer")
input("Please open Geo-Math in full screen mode and press 'Enter' to continue...")

wrapper(main)