##This module finds the best possible move
#The best move is the one that results in the lowest new tower height and the fewest number of "holes"
#The best move is prioritized in this order
# 1.Smallest tower height
# 2.Fewest number of holes
# Example of hole:
# xxxxx The "x"'s represent occupied slots (a piece is found here)
# x---x The "-"'s in this row represent holes because no falling piece can displace it
# xxxxx


import debug
import simulate
import tracer
from prioritize import final
show_debug = False

def single_best_move(block, grid):
    a = []
    for r in block.rotations():
        p = Possible_Moves(grid, r).get_best_moves()
        if p == None: 
            return
        else:
            a.append(p)

    return final(a)
    
#Finds the best possible move based on a particular rotation of a peice
#Each piece rotation creates an instance of this class (from run.py)
class Possible_Moves:
    
    def __init__(self, grid, block):
        self.grid = grid
        self.block = block

    ##Simulates moves
    #Simulates moves up to the point where a row is empty
    #Starting from the bottom, a block is placed in a grid, moving right each time
    #Stoms simulating after the first empty row
    def get_best_moves(self):
        scores = []
        first_empty = simulate.first_empty_row(self.grid)
        
        if first_empty == -1:
            return
            
        if show_debug:
            print("Simulate First empty row",first_empty)
        
        for y in range(len(self.grid)-1, -1, -1):
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
            print(scores)
            
        return final(scores)
            
    #Temporarily places a block in any position
    #If move is illegal it returns False
    #If a move is legal, place the block at the given y and x coordinate
    #Count the cells occupied per row, and return the value plus the 
    def try_place(self, y, x, grid):
        grid = simulate.place(y, x, grid, self.block, 2, 'dc')
        if grid != None and self.check_lowest(y, x, grid) != None:
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
                if x_p >= len(self.grid[0]):
                    return
                for y_p in range(y, y-len(self.block)-1, -1):
                    if y_p < 0:
                        return 
                    y_b = len(self.block)-1-y+y_p
                    if self.block[y_b][x_p-x] != 0 and grid[y_p+1][x_p] != 0:
                        return True
                    else:
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
            
        removed_rows = simulate.find_full_rows(grid)
        return [columns-removed_rows, tracer.Tracer(grid).run(), removed_rows, [y_c,x_c]]
        
