import curses


coordinates = {
    "P": []
}

indexes = {
    "X": {
        
    },

    "Y": {

    }
}

def get_coordinates():
    return coordinates

def get_dimentions():
    return [width, height]

def initScreen(x, y):
    try:
        coordinate_system = curses.newwin(y, x, 1, 1)

        return coordinate_system
    except:
        return False
    

def draw_coordinate_system(coordinate_system, space_x:int, space_y:int):
    global middle_x
    global middle_y

    global height
    global width
    try:
            
        # Get height and width of window
        height, width = coordinate_system.getmaxyx()

        # Calculate the middle position
        middle_x = height // 2
        middle_y = width // 2

        rate_y = 1 / space_y
        rate_x = 1 / space_x 


        # Clear
        coordinate_system.clear()

        # Render the Y-Axis (Without numbers)
        len_y = 0
        for i in range(0, height, 1):
            coordinate_system.addstr(i, middle_y, "|")
            len_y += 1
            

        # Render negative values (Y-Axis)
        index = 0
        for i in range(middle_x, height, space_y):
            coordinate_system.addstr(i, middle_y, f"# {index}")
            indexes["Y"][index] = i
            index -= 1
        
        # Render positive values (Y-Axis)
        index = 0
        for i in range(middle_x, 0, -space_y):
            coordinate_system.addstr(i, middle_y, f"# {index}")
            indexes["Y"][index] = i
            index += 1



        # Render the X-Axis (without values)
        len_x = 0
        for i in range(0, width, 1):
            coordinate_system.addstr(middle_x, i, f"-")
            len_x += 1
        
        # Render positive values (X-Axis)
        index = 1
        for i in range(middle_y +space_x, width, space_x):
            coordinate_system.addstr(middle_x, i, "#")
            coordinate_system.addstr(middle_x -1, i, f"{index}")
            indexes["X"][index] = i
            index += 1
        
        # Render negative values (X-Axis)
        index = -1
        for i in range(middle_y -space_x, 0, -space_x):
            coordinate_system.addstr(middle_x, i, "#")
            coordinate_system.addstr(middle_x -1, i, f"{index}")
            indexes["X"][index] = i
            index -= 1
        
            

        coordinate_system.addstr(middle_x, middle_y, f"0", curses.A_STANDOUT)
    
    
    except Exception as e:
        print(e)
        input()

def draw(coordinate_system):
    for coordinate in coordinates['P']:
        x_value = coordinate[0]
        y_value = coordinate[1]

        if x_value == 0:
            x = middle_y
        else:
            x = indexes["X"][x_value]
        
        if y_value == 0:
            y = middle_x

        else:
            y = indexes["Y"][y_value]

        coordinate_system.addstr(y, x, f"X ({x_value}|{y_value})", curses.A_STANDOUT)
    coordinate_system.refresh()


def new_coordinate(coordinate:list):
    x_value = coordinate[0]
    y_value = coordinate[1]
    coordinates["P"].append([x_value, y_value])