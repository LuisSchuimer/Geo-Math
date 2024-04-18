def calcFunc(function, x_max, y_max):

    function_coordinates = []
    start_x = int(float(x_max[1]))
    end_x = int(float(x_max[0]))

    for x_value in range(start_x, end_x-1, 1):
        x = x_value
        new_func = function.replace("x", str(x_value))
        y = eval(new_func)

        function_coordinates.append([x, y])

    
    return function_coordinates
