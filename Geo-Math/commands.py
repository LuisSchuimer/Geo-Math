import coordinate_system
import info_window

class command:
    def __init__(self, cs_window, info_window):
        self.coordinate_system_win = cs_window
        self.info_window = info_window
        self.default_x = 5
        self.default_y = 2
        self.last_x = self.default_x
        self.last_y = self.default_y


    def runCommand(self, command):
        try:
        
            if "add p" in command:
                command_type, type, coordinates = command.split(" ")
                x, y = coordinates.split(",")
                coordinate_system.new_coordinate([int(x), int(y)])
                coordinate_system.draw(self.coordinate_system_win)

                info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window)
            
            
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
                    coordinate_system.draw_coordinate_system(self.coordinate_system_win, space_x=5, space_y=2)



                
                coordinate_system.draw(self.coordinate_system_win)
        
        except:
            pass