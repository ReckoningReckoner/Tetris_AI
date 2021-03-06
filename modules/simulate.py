import copy

#places a block in a grid given the top left y and x coordinate
#returns that grid with said bloc

def place(y, x, grid, block, n=1, mode =''):
    if mode == 'dc':
        grid = copy.deepcopy(grid)
    for y_p in range(y, y-len(block), -1):        
        for x_p in range(x, x+len(block[0])):
            if y_p < -2 or y_p >= len(grid) or x_p < 0 or x_p >= len(grid[y]):
                return None
            else:
                y_b = len(block)-1-y+y_p
                if grid[y_p][x_p] != 0 and block[y_b][x_p-x] != 0:
                    return None
                if block[y_b][x_p-x] != 0:
                    grid[y_p][x_p] = n
    return grid


##Find the first empty row
def first_empty_row(grid):
    for y in range(len(grid)-1,-1,-1):
        count = 0
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                count += 1
                break
        if count == 0:
            return y
    else:
        return -1


def find_full_rows(grid):
    removed = 0
    for y in range(len(grid)-1,-1,-1):
        c = 0
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                c+=1    
                            
        if c == len(grid[y]):
            removed += 1
        
    return removed
    
    
def drop_lines(grid):
    removed = 0
    for y in range(len(grid)-1,-1,-1):
        c = 0
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                c+=1
                
        if c == len(grid[y]):
            grid.pop(y)
            removed += 1
    for i in range(removed):
        grid.insert(0,[0 for w in range(len(grid[0]))])
        
    return grid