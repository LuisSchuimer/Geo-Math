from curses import wrapper
import coordinate_system
    

def main(stdscr):
    height, _ = stdscr.getmaxyx()

    coordinate_system.draw(middle_y=height // 2)

print("GEO-MATH | Coordinate-System Test | Luis Schuimer 2024")
input("Please open Geo-Math in full screen mode and press 'Enter' to continue...")

wrapper(main)