import numpy as np
from utils import find_variable_names

def calcFunc(function, x_max, y_max, rate, defined_variables):

    function_coordinates = []
    start_x = int(float(x_max[1]))
    end_x = int(float(x_max[0]))

    count = 0
    for x_value in np.arange(start_x, end_x-1, float(rate[0])):
        x = x_value
        new_func = function.replace("x", str(x_value))

        for variable in defined_variables.keys():
            new_func = new_func.replace(variable, f"{defined_variables[variable]}")

        variables = find_variable_names(new_func)

        try: y = eval(new_func)
        except: return False, variables

        if count >= 5: function_coordinates.append([x, y, True]); count = 0
        else: function_coordinates.append([x, y, False])

        count += 1

    
    return function_coordinates, variables

