from curses import wrapper
import coordinate_system
import curses
    

def main(stdscr):
    # Initilise window for coordinate-system

    x = 100
    y = 55
    window = False

    while not  window:
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

    coordinate_system.draw_coordinate_system(window, space_x=4, space_y=2)
    coordinate_system.new_coordinate([3, 6])
    coordinate_system.new_coordinate([4, -2])
    coordinate_system.new_coordinate([-3, -1])
    coordinate_system.new_coordinate([-2, 5])
    coordinate_system.draw(window)

    window.refresh()
    window.getch()
    curses.endwin()

print("GEO-MATH | Coordinate-System Test | Luis Schuimer 2024")
input("Please open Geo-Math in full screen mode and press 'Enter' to continue...")

wrapper(main)