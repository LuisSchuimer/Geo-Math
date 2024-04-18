import coordinate_system
import info_window
import functions

class command:
    def __init__(self, cs_window, info_window):
        self.coordinate_system_win = cs_window
        self.info_window = info_window
        self.default_x = 5
        self.default_y = 2
        self.last_x = self.default_x
        self.last_y = self.default_y
        self.offset = [0, 0]


    def runCommand(self, command):
        try:
        
            if "add" in command:
                if "add p" in command:
                    command_type, type, coordinates = command.split(" ")
                    x, y = coordinates.split(",")
                    coordinate_system.new_coordinate([str(x), str(y)])
                    coordinate_system.draw(self.coordinate_system_win)

                    info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window, coordinate_system.get_rate())
                
                elif "add f" in command:
                    command_type, type, func = command.split(" ")

                    coordinate_system.new_function(func)
                    
                    coordinate_system.draw(self.coordinate_system_win)

                    info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window, coordinate_system.get_rate())

            
            
            if "zoom" in command:
                if not "def" in command:
                    command_type, axis, scale = command.split(" ")

                    if axis == "x":
                        self.last_x = int(scale)+1
                        coordinate_system.draw_coordinate_system(self.coordinate_system_win, space_x=int(scale)+1, space_y=self.last_y)
                    elif axis == "y":
                        self.last_y = int(scale)+1
                        coordinate_system.draw_coordinate_system(self.coordinate_system_win, space_x=self.last_x, space_y=int(scale)+1)

                else:
                    self.last_x = self.default_x
                    self.last_y = self.default_y
                    coordinate_system.draw_coordinate_system(self.coordinate_system_win, space_x=self.default_x, space_y=self.default_y)
                
                info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window, coordinate_system.get_rate())

                coordinate_system.draw(self.coordinate_system_win)
            

        
        except Exception as e:
            self.coordinate_system_win.addstr(4,3, f"{e}")
            self.coordinate_system_win.refresh()



    def offset_coordinate_system(self, key):
            if key == 259: # ARROW UP
                self.offset[0] += 1 # Move up 
            elif key == 258: # ARROW DOWN
                self.offset[0] -= 1 # Move down
            elif key == 260: # ARROW LEFT
                self.offset[1] += 1 # Move left
            elif key == 261: # ARROW RIGHT
                self.offset[1] -= 1 # Move right
        
            coordinate_system.draw_coordinate_system(self.coordinate_system_win, space_x=self.last_x, space_y=self.last_y, offset=self.offset)
            coordinate_system.update()
            coordinate_system.draw(self.coordinate_system_win)
            info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window, coordinate_system.get_rate())