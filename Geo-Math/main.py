from curses import wrapper
import coordinate_system
import info_window
import console
import curses
    

def main(stdscr):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Initialise window for coordinate-system

    x = 100
    y = 47
    window = False

    while not window:
        # Try init
        window = coordinate_system.initScreen(x, y)
        # Adjust window size if to big
        if not window:
            # 
            if x != 20:
                y -= 1
                if y == 0:
                    x -= 1
                    y = 60
            else:
                # Trow a exception
                Exception("Could not initialise Coordinate-System screen")
    
    cs_x = x

    # Initialise the info-window
    remaining_width = 1 + cs_x
    info_x = int(round(remaining_width / 2, 1))
    info_win = info_window.initWindow(height -2, info_x, remaining_width)

    # Initialise Console Window
    remaining_width = 3 + cs_x + info_x
    width_left = width - remaining_width
    console_window = console.initWindow(width_left, 8, remaining_width, 1)

    # Draw coordinate-system and draw coordinates
    coordinate_system.draw_coordinate_system(window, space_x=5, space_y=2)

    # If info menu init display data
    if info_win:
        info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, info_win, coordinate_system.get_rate())
    
    if console_window:
        console.display(console_window)

    # Generate border and refresh c.s.
    window.border()
    window.refresh()
    # If info win init generate border and refresh
    if info_win:
        info_win.border()
        info_win.refresh()
    # If console init generate border and refresh
    if console_window:
        console_window.border()
        console_window.refresh()

    console.start_console(console_window, window, info_win)
    # Wait for user key press to stop program
    window.getch()
    curses.endwin()

print("GEO-MATH | Coordinate-System | C2024 Luis Schuimer")
input("Please open Geo-Math in full screen mode and press 'Enter' to continue...")

wrapper(main)