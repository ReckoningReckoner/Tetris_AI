import debug
import placer
import tracer
from random import randint

show_debug = False

##The "best move" is the one that creates the least number of holes and rows
#If there are multiple possible "best moves", it randomly picks the best and lowest
def final(a):    
    a.sort(key=lambda x: x[0])
    lowest_height = a[0][0]
    
    for i in range(len(a)-1, -1, -1):
        if a[i][0] > lowest_height:
            a.pop(i)
            
    a = sorted(a, key=lambda x: x[1])
    lowest_holes = a[0][1]
    
    for i in range(len(a)-1, -1, -1):
        if a[i][1] > lowest_holes:
            a.pop(i)
                
    
    return a[randint(0, len(a)-1)]


class Best_Possible_Moves:
    
    def __init__(self, grid, block):
        self.grid = grid
        self.block = block
                
    ##Find the first empty row
    def first_empty_row(self):
        for y in range(len(self.grid)):
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
            print("Simulate First empty row",first_empty)
        
        for y in range(len(self.grid)-1, first_empty-1, -1):
            for x in range(len(self.grid[y])-len(self.block[0])+1):
                s = self.try_place(y, x, self.grid)
                if s != None:
                    s.append(self.block)
                    scores.append(s)
                    if show_debug:
                        print("Simulate Printing s")
                        print(s)
        if show_debug:
            print("Simulate These are the scores:")
            for i in scores:
                print(i[0:2])
            print('Simulate This is what is being returned')
            print(final(scores))
            
        return final(scores)
            
    #Temporarily places a block in any position
    #If move is illegal it returns False
    #If a move is legal, place the block at the given y and x coordinate
    #Count the cells occupied per row, and return the value plus the 
    def try_place(self, y, x, grid):
        grid = placer.place(y, x, grid, self.block, 2, 'dc')
        if grid != None and self.check_lowest(y, x, grid):
            if show_debug:           
                print("try_place Block")
                debug.show(self.block)
                print("try_place Grid")
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
        for y in range(len(grid)-1, -1, -1):
            for x in range(len(grid[y])):
                if grid[y][x] != 0:
                    columns += 1
                    break
            
        return [columns, tracer.Tracer(grid).run(), [y_c,x_c]]
        
