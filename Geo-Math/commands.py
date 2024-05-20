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

                    info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window, coordinate_system.get_rate(), coordinate_system.get_variables())
                
                elif "add f" in command:
                    command_type, type, func = command.split(" ")

                    coordinate_system.new_function(func)
                    
                    coordinate_system.draw(self.coordinate_system_win)

                    info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window, coordinate_system.get_rate(), coordinate_system.get_variables())


            if "save" in command:
                command_type, name = command.split(" ")

                coordinate_system.save(name)
            
            if "load" in command:
                command_type, name = command.split(" ")

                coordinate_system.load(name, self.coordinate_system_win)

            if "set" in command:
                if "set range" in command:
                    pass
            
                else: 
                    command_type, variable, value = command.split(" ")
                    coordinate_system.add_variable(variable, value)


                    coordinate_system.draw_coordinate_system(self.coordinate_system_win, space_x=self.default_x, space_y=self.default_y, offset=self.offset)
                    coordinate_system.update()
                    coordinate_system.draw(self.coordinate_system_win)
                    info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window, coordinate_system.get_rate(), coordinate_system.get_variables())

            
            if "zoom" in command:
                if not "def" in command:
                    command_type, axis, scale = command.split(" ")

                    if axis == "x":
                        self.last_x = int(scale)+1
                        coordinate_system.draw_coordinate_system(self.coordinate_system_win, space_x=int(scale)+1, space_y=self.last_y, offset=self.offset)
                    elif axis == "y":
                        self.last_y = int(scale)+1
                        coordinate_system.draw_coordinate_system(self.coordinate_system_win, space_x=self.last_x, space_y=int(scale)+1, offset=self.offset)

                else:
                    self.last_x = self.default_x
                    self.last_y = self.default_y
                    coordinate_system.draw_coordinate_system(self.coordinate_system_win, space_x=self.default_x, space_y=self.default_y, offset=self.offset)
                
                info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window, coordinate_system.get_rate(), coordinate_system.get_variables())

                coordinate_system.draw(self.coordinate_system_win)
            

        
        except Exception as e:
            self.coordinate_system_win.addstr(4,3, f"{e}")
            self.coordinate_system_win.refresh()

            raise e



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
            info_window.display(coordinate_system.get_coordinates, coordinate_system.get_dimentions, self.info_window, coordinate_system.get_rate(), coordinate_system.get_variables())