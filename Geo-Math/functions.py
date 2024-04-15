import coordinate_system
from decimal import Decimal

def calcFunc(function):
    function_coordinates = []
    x_max, y_max = coordinate_system.get_max_indexes()

    start_x = int(float(x_max[1]))
    end_x = int(float(x_max[0]))

    for x_value in range(start_x, end_x-1, 1):
        x = x_value
        new_func = function.replace("x", str(x_value))
        y = eval(new_func)

        if not y < int(round(float(y_max[1]), 0))-1 or not y > int(round(float(y_max[0]), 0))-1:
            function_coordinates.append([x, y])

    
    return function_coordinates
