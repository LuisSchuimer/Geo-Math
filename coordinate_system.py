import curses

def draw(middle_y, coordinates = None):
    try:

        coordinate_system = curses.newwin(60, 100, 0, middle_y)
        height, width = coordinate_system.getmaxyx()

        # Calculate the middle position
        middle_x = height // 2
        middle_y = width // 2

        coordinate_system.clear()
        coordinate_system.addstr(0, 0, f"{height}|{width}", curses.A_STANDOUT)

        # Start with the hightest possible Y-Value
        count = int(round(height /4, 0))

        # Render the Y-Axis
        for i in range(0, height):
            # Check if index is even
            if i % 2 == 0:
                coordinate_system.addstr(i, middle_y, f"{count}")

                # Check if coordinates are at the X Level
                if i > middle_x:
                    # If it is under subtract
                    count -= 1
                elif i == middle_x:
                    # Set it to -1
                    count = -1
                else:
                    count -= 1
            else:
                if  i == middle_x:
                    count = -1

                coordinate_system.addstr(i, middle_y, "|")


        # Render the X-Axis
        for i in range(0, width):
                coordinate_system.addstr(middle_x, i, f"-")
        

        coordinate_system.addstr(middle_x, middle_y, f"0", curses.A_STANDOUT)
        

        coordinate_system.refresh()
        coordinate_system.getkey()
    except Exception as e:
        print(e)
        input()