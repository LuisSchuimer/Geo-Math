# Geo-Math

A coordinate-system in your Terminal

## Commands
### 1. Add Point
- Enter `add p x,y` (Replace x,y with your coordinates) into the 'Commands' Tab
    - 'add' tells the program, to add something
    - 'p' tells the program, that a point is adressed
    - 'x,y' tells the programm, where to put the point in the coordinate-system
- Press 'Enter'

### 2. Adding Functions
- Enter `add f (func)` (Replace '(func)' with your function) into the 'Commands' Tab
    - 'add' tells the program, to add something
    - 'f' tells the program, to add a function
    - '(func)' tells the program, what function to add
- Press 'Enter'

f. e. `x*2` or `x*3*y`

### 3. Zooming
- Tell the coordinate-system, how big the spaces between full numbers should be
- Enter `zoom x/y (scale)` into the 'Commands' Tab
    - 'zoom' tells the program, that you want to edit the coordinate-system
    - 'x/y' tells the program, which axis to edit
    - 'scale' tells the program, how big the spaces between full numbers should be
- Press 'Enter'

- Enter `zoom def` to return to the default zoom into the 'Commands' Tab
    - 'zoom' tells the program, that you want to edit the coordinate-system
    - 'def' tells the program, that you want to return to the defauld zoom
- Press 'Enter'

### 4. Set Variables
- Enter `set (name) (value)`
    - 'set' tells the program, to set something
    - '(name)' tells the program, which variable you want to set
    - '(value)' tells the program, which value the variable should have
- INFO: `x` is a invalid variable name and is not used when set

### Save/Load .gmf Files
- Enter `save (name)` (Replace name with your custom name)
    - 'save' tells the program, that you wnat to save the current workspace
    - 'name' tells the program, what name the file should have

  f. e. `save main`, saves the current workspace in 'main.gmf'

- Enter `load (name)` (Replace name with the filename without the extention)
    - 'load' tells the program, to load data out of a file
    - 'name' tells the program, what file you want to load from

  f. e. `load main`, loads a workspace out of a .gmf file (in this case: main.gmf)
 
