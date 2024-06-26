import curses
from decimal import Decimal, getcontext
import utils
import functions

getcontext().prec = 4  # Set the precision to 4 places

coordinates = {
    "P": [],
    "F": {}
}

indexes = {
    "X": {
        
    },

    "Y": {

    }
}


variables = {}

# Functions to give back data
def get_coordinates():
    return coordinates

def get_dimentions():
    return [width, height]

def get_rate():
    return [rate_x, rate_y]

def get_max_indexes():
    return [max_x_positive, max_x_negative], [max_y_positive, max_y_negative]

def get_variables():
    return variables


def initScreen(x, y):
    try:
        coordinate_system = curses.newwin(y, x, 1, 1)

        return coordinate_system
    except:
        return False
    

def draw_coordinate_system(coordinate_system, space_x:int, space_y:int, offset:list = [0, 0]):
    global middle_x
    global middle_y

    global height
    global width

    global rate_x
    global rate_y

    global max_x_positive
    global max_y_positive
    global max_x_negative
    global max_y_negative

    try:
        # Clear indexes of X, Y
        indexes["X"].clear()
        indexes["Y"].clear()

        coordinate_system.clear()
            
        # Get height and width of window
        height, width = coordinate_system.getmaxyx()

        if offset == [0, 0]:
            # Calculate the middle position
            middle_x = height // 2
            middle_y = width // 2
        else:
            middle_x = height // 2 + offset[0]
            middle_y = height // 2 + offset[1]

        # Using Decimal for precise division
        rate_y = Decimal('1') / Decimal(space_y)
        rate_x = Decimal('1') / Decimal(space_x)
        rate_y = rate_y.quantize(Decimal('0.1'))  # quantizing to 1 decimal place
        rate_x = rate_x.quantize(Decimal('0.01')) # quantizing to 2 decimal places


        # Clear
        coordinate_system.clear()

        # Render the Y-Axis (Without numbers)
        len_y = 0
        for i in range(0, height, 1):
            try:
                coordinate_system.addstr(i, middle_y,"|")
                len_y += 1
            except:
                continue
        
        # Render the X-Axis (without values)
        len_x = 0
        for i in range(0, width, 1):
            try:
                if middle_x <= height:
                    coordinate_system.addstr(middle_x, i, f"-")
                    len_x += 1
                else:
                    coordinate_system.addstr(height, i, f"-")
                    len_x += 1
            except:
                continue

        # Display and Index positive values (X-Axis)
        index = 0
        count = 0
        for i in range(middle_y, width, 1):
            if count >= space_x:
                try:
                    coordinate_system.addstr(middle_x, i, "#")
                    coordinate_system.addstr(middle_x -1, i, f"{round(index, utils.count_decimal_places(index))}")
                except:
                    pass
                count = 0

            indexes['X'][str(round(index, utils.count_decimal_places(index)))] = i
            count += 1
            index += round(rate_x, 1)
        
        max_x_positive = index
        

        # Display and Index negative values (X-Axis)
        index = 0
        count = 0
        for i in range(middle_y, 0, -1):
            if count >= space_x:
                try:
                    coordinate_system.addstr(middle_x, i, "#")
                    coordinate_system.addstr(middle_x -1, i-1, f"{round(index, utils.count_decimal_places(index))}")
                except:
                    pass
                count = 0
                
            indexes['X'][str(round(index, utils.count_decimal_places(index)))] = i
            count += 1
            index -= round(rate_x, 1)
        
        max_x_negative = index
        
        
        # Display and Index negative values (Y-Axis)
        index = 0
        count = 0
        for i in range(middle_x, height, 1):
            if count >= space_y:
                try: coordinate_system.addstr(i, middle_y, f"# {round(index, utils.count_decimal_places(index))}")
                except:
                    pass
                count = 0

            indexes['Y'][str(round(index, utils.count_decimal_places(index)))] = i
            count += 1
            index -= rate_y

        max_y_negative = index

        # Display and Index positive values (Y-Axis)
        index = 0
        count = 0
        for i in range(middle_x, 0, -1):
            if count >= space_y:
                try: coordinate_system.addstr(i, middle_y, f"# {round(index, utils.count_decimal_places(index))}")
                except:
                    pass
                count = 0
                
            indexes['Y'][str(round(index, utils.count_decimal_places(index)))] = i
            count += 1
            index += rate_y

            

        max_y_positive = index            

        try: coordinate_system.addstr(middle_x, middle_y, f"0", curses.A_STANDOUT) 
        except: 
            pass

        coordinate_system.border()
        coordinate_system.refresh()
    
    
    except:
        pass

def draw(coordinate_system):
    try:
        # Draw Points
        for coordinate in coordinates['P']:
            x_value = coordinate[0]
            y_value = coordinate[1]

            if x_value == 0:
                x = middle_y
            else:
                try: x = indexes['X'][str(x_value)]
                except KeyError: x = indexes['X'][str(utils.find_closest_key(indexes['X'], x_value))]

            if y_value == 0:
                y = middle_x

            else:
                try: y = indexes['Y'][str(y_value)]
                except KeyError: y = indexes['Y'][str(utils.find_closest_key(indexes['Y'], y_value))]

            if float(y_value) <= max_y_positive -1 and float(y_value) >= max_y_negative +1 and float(x_value) <= max_x_positive-1 and float(x_value) >= max_x_negative-1:
                try:
                    coordinate_system.addstr(y, x, f"X ({round(float(x_value), 2)}|{round(float(y_value), 2)})", curses.A_STANDOUT)
                    try: coordinate[2] = True 
                    except: coordinate.append(True)
                except Exception as err:
                    try: coordinate[2] = False
                    except: coordinate.append(False)


            else:
                try: coordinate[2] = False
                except: coordinate.append(False)


            coordinate_system.refresh()

        # Draw functions
        
        all_functions = list(coordinates['F'].keys())
        for function in all_functions:
            for coordinate in coordinates['F'][function]:
                x_value = coordinate[0]
                y_value = coordinate[1]

                if x_value == 0: x = middle_y
                else:
                    try: x = indexes['X'][str(x_value)]
                    except KeyError: x = indexes['X'][str(utils.find_closest_key(indexes['X'], x_value))]

                if y_value == 0: y = middle_x
                else:
                    try: y = indexes['Y'][str(y_value)]
                    except KeyError: y = indexes['Y'][str(utils.find_closest_key(indexes['Y'], y_value))]
                    
                if y_value <= max_y_positive -1 and y_value >= max_y_negative +1:
                    if coordinate[2]:
                        try: coordinate_system.addstr(y, x, f"X ({round(x_value, 2)}|{round(y_value, 2)})", curses.A_STANDOUT)
                        except: 
                            pass

                    else:
                        try: coordinate_system.addstr(y, x, f"#")
                        except: 
                            pass


        coordinate_system.refresh()
    
    except:
        pass



def new_coordinate(coordinate:list):
    x_value = coordinate[0]
    y_value = coordinate[1]
    coordinates["P"].append([x_value, y_value])


def new_function(function):
    coordinates["F"][function] = []
    max_x, max_y = get_max_indexes()
    func_coordinates, func_variables = functions.calcFunc(function, max_x, max_y, [rate_x, rate_y], variables)

    if func_coordinates:
        for coordinate in func_coordinates:
            coordinates["F"][function].append([coordinate[0], coordinate[1], coordinate[2]])

    for variable in func_variables:
        add_variable(variable)

# Update all functions
def update():
    all_functions = list(coordinates['F'].keys())
    for function in all_functions:
        coordinates["F"][function] = []
        max_x, max_y = get_max_indexes()
        func_coordinates, func_variables = functions.calcFunc(function, max_x, max_y, [rate_x, rate_y], variables)

        if func_coordinates:
            for coordinate in func_coordinates:
                coordinates["F"][function].append([coordinate[0], coordinate[1], coordinate[2]])


def add_variable(name, value=None):
    variables[name] = value


def save(name):
    import json

    info = [
        coordinates,
        [rate_x, rate_y],
        variables
    ]

    with open(f"{name}.gmf", "w") as save_file:
        json.dump(info, save_file, default=convert_decimal)

def convert_decimal(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


def load(name, coordinate_system):
    global coordinates, variables

    import json
    try:
        with open(f"{name}.gmf", "r") as load_file:
            info = json.load(load_file)

            coordinates = info[0]
            variables = info[2]

            update()
            draw(coordinate_system)

    except json.JSONDecodeError as e:
        raise e
    except FileNotFoundError:
        print(f"File {name}.gmf not found")
    except Exception as e:
        raise e
    