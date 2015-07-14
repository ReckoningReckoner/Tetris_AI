import builder
import debug
import best_move
import placer
from random import randint


def get_command():
        s = input('> ')
        if s == 'q': 
            return -1
        elif s == 'l':
            return builder.L_Block()
        elif s == 'o':
            return builder.O_Block()
        elif s == 'i':
            return builder.I_Block()
        elif s == 's':
            return builder.S_Block()
        elif s == 't':
            return builder.T_Block()
        elif s == 'z':
            return builder.Z_Block()
        elif s == 'j':
            return builder.J_Block()
        else: 
            return builder.blocks[randint(0, len(builder.blocks)-1)]
            
def play():
    WIDTH  = 8
    HEIGHT = 20
    grid   = [[0 for w in range(WIDTH)] for h in range(HEIGHT)] ##Default 8x20 Grid
    # grid = [[0, 0, 0, 0, 0, 0, 0, 0], #Custom grid for testing
  #           [0, 0, 0, 0, 0, 0, 0, 0],
  #           [0, 0, 0, 0, 0, 0, 0, 0],
  #           [0, 0, 0, 0, 0, 0, 0, 0],
  #           [0, 0, 0, 0, 0, 0, 0, 0],
  #           [0, 0, 0, 0, 0, 0, 0, 0],
  #           [0, 0, 0, 1, 1, 1, 1, 0],
  #           [1, 0, 0, 0, 1, 1, 1, 0],
  #           [1, 1, 0, 1, 1, 1, 1, 0]]

    print("Press any key to simulate a round with a random block")
    print("Pressing the lowercase name of a block will generate said block")
    print("Press 'q' to exit")
    
    c = 0
    
    while True: 
        c+=1
        if c == 9: c = 1        
        b = get_command()
        if b == -1: break
        
        a = []
        for r in b.rotations():
            bpm = best_move.Best_Possible_Moves(grid, r)
            if bpm.simulate() == None: 
                return
            else:
                a.append(bpm.simulate())
                
    
        best = best_move.final(a)
        print(best[0:3])
        grid = placer.place(best[2][0], best[2][1], grid, best[3], c)
        debug.show(grid)