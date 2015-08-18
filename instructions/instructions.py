from modules import flipper
from modules import simulate
from modules import debug

def get_moves(new_grid,old_grid, block, coords):
    y, x = coords[0], coords[1]
    
    print("OLD:")
    debug.show(new_grid)
    
    r_left = simulate.place(y, x, old_grid, flipper.rotate_cclockwise(block), 1, "dc") != None
    r_right = simulate.place(y, x, old_grid, flipper.rotate_clockwise(block), 1, "dc") != None
    left = simulate.place(y, x-1, old_grid, block, 1, "dc") != None
    right = simulate.place(y, x+1, old_grid, block, 1, "dc") != None
    up = simulate.place(y-1, x+1, old_grid, block, 1, "dc") != None
    
    print("r_left", r_left)
    if r_left:
        debug.show(simulate.place(y, x, old_grid, flipper.rotate_cclockwise(block), 1, "dc"))
    print("r_right", r_right)
    if r_right:
        debug.show(simulate.place(y, x, old_grid, flipper.rotate_clockwise(block), 1, "dc"))
    print("l", left)
    print("r", right)
    print("u", up)
