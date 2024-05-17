import numpy as np

def calcFunc(function, x_max, y_max, rate):

    function_coordinates = []
    start_x = int(float(x_max[1]))
    end_x = int(float(x_max[0]))

    count = 0
    for x_value in np.arange(start_x, end_x-1, float(rate[0])):
        x = x_value
        new_func = function.replace("x", str(x_value))
        y = eval(new_func)

        if count >= 5: function_coordinates.append([x, y, True]); count = 0
        else: function_coordinates.append([x, y, False])

        count += 1

    
    return function_coordinates
