import debug
import placer
from random import randint

show_debug = False

##The "best move" is the one that creates the least number of holes and rows
#If there are multiple possible "best moves", it randomly picks the best and lowest
def final(a):    
    lowest_height = sorted(a, key=lambda x: x[0])[0][0]
    for i in range(len(a)-1, -1, -1):
        if a[i][0] != lowest_height:
            a.pop(i)
            
    if len(a) > 1:
        return a[randint(0,len(a)-1)]
    else: 
        return  a[0]         


class Best_Possible_Moves:
    
    def __init__(self, grid, block):
        self.grid = grid
        self.block = block
                
    ##Find the first empty row
    def first_empty_row(self):
        for y in range(len(self.grid)-1, -1, -1):
            count = 0
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != 0:
                    count += 1
                    break
            if count == 0:
                return y
        else:
            return -1
        
    ##Simulates moves
    #Simulates moves up to the point where a row is empty
    #Starting from the bottom, a block is placed in a grid, moving right each time
    #Stoms simulating after the first empty row
    def simulate(self):
        scores = []
        first_empty = self.first_empty_row()
        
        if first_empty == -1:
            return
            
        if show_debug:
            print("First empty row",first_empty)
        
        for y in range(len(self.grid)-1, first_empty-1, -1):
            for x in range(len(self.grid[y])-len(self.block[0])+1):
                s = self.try_place(y, x, self.grid)
                if s != None:
                    s.append(self.block)
                    scores.append(s)
                if show_debug:
                    print("Printing s")
                    print(s)
                    
        return sorted(scores, key=lambda x: x[0])[0]
            
    #Temporarily places a block in any position
    #If move is illegal it returns False
    #If a move is legal, place the block at the given y and x coordinate
    #Count the cells occupied per row, and return the value plus the 
    def try_place(self, y, x, grid):
        grid = placer.place(y, x, grid, self.block, 2)
        if grid != None and self.check_lowest(y, x, grid):
            if show_debug:
                print("Block and grid")
                debug.show(self.block)
                print("")
                debug.show(grid)
            return self.count_lines(grid, y, x)

        
    ##Check if the current block placement is floaty
    def check_lowest(self, y, x, grid):
        if y < len(self.grid)-1:
            for x_p in range(x, x+len(self.block[0])):
                for y_p in range(y, y-len(self.block), -1):
                    y_b = len(self.block)-1-y+y_p
                    if self.block[y_b][x_p-x] != 0 :
                        if grid[y_p+1][x_p] != 0: return True
                        break
        else:
            return True        
        
    #Count the columns each cell occupies
    def count_lines(self, grid, y_c, x_c):
        columns = 0
        holes = 0
        for y in range(len(grid)-1, -1, -1):
            has_stuff = False
            h = 0
            for x in range(len(grid[y])):
                if grid[y][x] != 0:
                    has_stuff = True
                else:
                    h += 1
            if has_stuff == True:
                columns += 1
                holes += h
            
        return [columns, holes, [y_c,x_c]]
        
        
 