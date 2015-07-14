import copy

#places a block in a grid given the top left y and x coordinate
#returns that grid with said block
def place(y, x, grid, block, n=1):
    grid = copy.deepcopy(grid)
    for y_p in range(y, y-len(block), -1):
        for x_p in range(x, x+len(block[0])):
            y_b = len(block)-1-y+y_p
            if grid[y_p][x_p] != 0 and block[y_b][x_p-x] != 0:
                return
            if block[y_b][x_p-x] != 0:
                grid[y_p][x_p] = n
    return grid