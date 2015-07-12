import copy
import debug


class Best_Move:
    def __init__(self, grid, block):
        self.grid = grid
        self.block = block
                
    ##Find the first empty row
    def first_empty_row(self):
        for y in range(len(self.grid)-1, -1, -1):
            count = 0
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 1:
                    count += 1
                    break
            if count == 0:
                return y
        
    ##Simulates moves
    #Simulates moves up to the point where a row is empty
    #Starting from the bottom, a block is placed in a grid, moving right each time
    #Stoms simulating after the first empty row
    def simulate(self):
        scores = []
        print("First empty row",self.first_empty_row())
        for y in range(len(self.grid)-1, self.first_empty_row()-1, -1):
            for x in range(len(self.grid[y])-len(self.block[0])+1):
                s = self.place(y, x, copy.deepcopy(self.grid))
                if s != False:
                    scores.append(s)

        return scores
        
    #Places a block
    #If move is illegal it returns False
    #If a move is legal, place the block at the given y and x coordinate
    #Count the cells occupied per row, and return the value plus the 
    def place(self, y, x, grid):
        lowest = False
        for y_p in range(y, y-len(self.block), -1):
            for x_p in range(x, x+len(self.block[0])):
                y_b = len(self.block)-1-y+y_p
                if grid[y_p][x_p] != 0 and self.block[y_b][x_p-x] != 0:
                    return False
                if self.block[y_b][x_p-x] != 0:
                    grid[y_p][x_p] = 2

        if (self.check_lowest(y, x, grid)):
            print(True)
            debug.show(grid)
            print("")
            return self.count_lines(grid)
        else:
            return False

        
    ##Check if the current block placement is floaty
    def check_lowest(self, y, x, grid):
        if y < len(self.grid)-1:
            for x_p in range(x, x+len(self.block[0])):
                for y_p in range(y, y-len(self.block), -1):
                    y_b = len(self.block)-1-y+y_p
                    if self.block[y_b][x_p-x] != 0 :
                        if grid[y_p+1][x_p] != 0: return True
                        break
            return False
        else:
            return True        
        
    #Count the number of occupied cells after a block is placed
    def count_lines(self, grid):
        counts = []
        for y in range(len(grid)-1, -1, -1):
            c = 0
            for x in range(len(grid[y])):
                if grid[y][x] != 0:
                    c += 1
            if c == 0:
                break
            else:
                counts.append([y, c])
                
        return counts