import debug
import copy

show_debug = False

##Counts the number of holes in a grid
#Used for prioritizing block placement

class Tracer:

    def __init__(self, grid):
        self.grid        = copy.deepcopy(grid)
        self.count       = 0
        self.h           = 0
        self.first_empty = 0

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
            
                    
    def trace(self, y, x):
        if  (0 <= y < len(self.grid) and 
             0 <= x < len(self.grid[0])):
            
            if (self.grid[y][x] == 0 and 
                (self.grid[y-1][x] != 0 or y-1 == -1)):
                
                self.grid[y][x] = 'a'
                return True
                            
    def run(self):
        self.first_empty = self.first_empty_row()
        for y in range(self.first_empty+2, len(self.grid), 1):
            for x in range(len(self.grid[y])):
                if self.trace(y, x) == True:
                    self.count += 1
                    if show_debug:
                        print("\n")
                        debug.show(self.grid)
                    
        return self.count
                

# grid = [[0, 0, 0, 0, 0, 0, 0, 0], #Custom grid for testing
#         [0, 0, 1, 0, 1, 0, 0, 0],
#         [0, 0, 1, 0, 1, 1, 1, 1],
#         [0, 0, 1, 0, 1, 1, 1, 1],
#         [1, 1, 1, 1, 1, 1, 1, 1]]
#
# print(Tracer(grid).run())
#
#

#Old slow and dumb recursive method
# def trace(self, y, x):
#     if  (0 <= y < len(self.grid) and
#             0 <= x < len(self.grid[0])):
#         if self.grid[y][x] == 0 and self.grid[y][x]:
#             self.h +=1
#             self.grid[y][x] = 'a'
#             self.trace(y+1, x)
#             self.trace(y-1, x)
#             self.trace(y, x+1)
#             self.trace(y, x-1)
#         if y <= self.first_empty or self.grid[y][x] == 'b':
#             return -1
#
#    def run(self):
#         self.first_empty = self.first_empty_row()
#         for y in range(self.first_empty+1, len(self.grid)):
#             for x in range(len(self.grid[y])):
#                 self.h = 0
#                 tr = self.trace(y, x)
#                 if tr == -1:
#                     self.reassign()
#                 elif self.h > 0:
#                     if show_debug:
#                         print("\n")
#                         print(tr)
#                         debug.show(self.grid)
#                     self.count += self.h