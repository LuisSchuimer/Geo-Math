
def draw_line(window, line, width):
    for i in range(width):
            window.addstr(line, i, "_")
        
def get_input(window):
      key_ch = window.getch()

      return key_ch

def count_decimal_places(number):
    # Convert the number to a string
    number_str = f"{number:.15f}"  # Convert float to string with enough precision
    
    # Strip trailing zeros to deal with floating-point imprecision
    number_str = number_str.rstrip('0')
    
    # Find the position of the decimal point
    decimal_point_index = number_str.find('.')
    
    # Calculate the number of decimal places
    if decimal_point_index == -1:
        # No decimal point means 0 decimal places
        return 0
    else:
        # Subtract the index of the decimal point from the length of the string
        # minus one (since the index is zero-based)
        return len(number_str) - decimal_point_index - 1
    
import re

def find_variable_names(expression):
    characters = re.findall(r'[a-zA-Z]', expression)
    return characters


def find_closest_key(d, current_key):
    # Convert current_key to float for comparison
    try:
        current_key_value = float(current_key)
    except ValueError:
        current_key_value = int(current_key)  # current_key is not a valid number

    closest_key = None
    minimum_distance = float('inf')

    # Process and sort the keys based on their float values
    sorted_keys = sorted(d.keys(), key=lambda x: float(x))

    # Find the closest bigger key
    for key in sorted_keys:
        key_value = float(key)
        if key_value > current_key_value:
            distance = key_value - current_key_value
            if distance < minimum_distance:
                minimum_distance = distance
                closest_key = key
            break  # Stop after finding the first bigger key
    
    # Find the closest smaller key
    for key in reversed(sorted_keys):
        key_value = float(key)
        if key_value < current_key_value:
            distance = current_key_value - key_value
            if distance <= minimum_distance:  # Prefer smaller key in case of a tie
                minimum_distance = distance
                closest_key = key
            break  # Stop after finding the first smaller key

    return closest_key
