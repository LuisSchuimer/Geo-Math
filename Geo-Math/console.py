import curses
from utils import draw_line, get_input
from curses.textpad import Textbox
import commands

buffer_command = ""

def initWindow(x, y, x_start, y_start):
    try:
        console_win = curses.newwin(y, x, y_start, x_start)

        return console_win

    except Exception as e:
        return e

def display(window):
    # Get dimentions
    _, width = window.getmaxyx()
    # Display Title
    window.addstr(1, 1, "CONSOLE", curses.A_STANDOUT)
    draw_line(window, 2, width)

    # Display command win
    window.addstr(3, 1, f">")
    # Get pointer x and y
    y, x = window.getyx()

    # Display Pointer Information
    draw_line(window, 5, width)
    window.addstr(6, 1, f"Cursor POS: {x-2}|{y-3}", curses.A_STANDOUT)

    window.border()
    window.refresh()

def start_console(window, cs_window, info_window):
    global buffer_command
    # Initialise commands
    command_utils = commands.command(cs_window, info_window)

    window.keypad(True)
    # Writing loop
    typing = True
    while typing:
        # Get key from user
        key_ch = get_input(window)

        # If key is not 'Enter' continue
        if key_ch != 10 and key_ch != 259 and key_ch != 258 and key_ch != 260 and key_ch != 261:
            if key_ch == 8:
                buffer_command = buffer_command[:-1]
            else:
                # Add key to buffer
                buffer_command += chr(key_ch)

            # Clear screen info
            window.clear()

            # Update Screen info
            display(window)
            window.addstr(3, 1, f">{buffer_command}|")
            y, x = window.getyx()
            window.addstr(6, 1, f"Cursor POS: {x-2}|{y-3}", curses.A_STANDOUT)
            window.border()
            window.refresh()

        elif key_ch == 10:
            # If 'Enter' pressed process command
            command_utils.runCommand(buffer_command)

            # Reset screen for next
            buffer_command = ""
             # Clear screen info
            window.clear()

            # Update Screen info
            display(window)
        
        else:
            command_utils.offset_coordinate_system(key_ch)
    