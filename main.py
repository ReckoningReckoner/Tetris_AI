import builder
import debug
from random import randint
import best_move
import sys

def get_command():
        s = input('> ')
        if s == 'q': 
            sys.exit()
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
            
def main():
    WIDTH  = 8
    HEIGHT = 20
    # grid   = [[0 for w in range(WIDTH)] for h in range(HEIGHT)] ##Default 8x20 Grid
    grid = [[0, 0, 0, 0, 0, 0, 0, 0], #Custom grid for testing
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0], 
            [1, 0, 0, 0, 1, 1, 1, 0], 
            [1, 1, 0, 1, 1, 1, 1, 0]]

    print("Press any key to simulate a round with a random block")
    print("Pressing the lowercase name of a block will generate said block")
    print("Press /'q/' to exit")
    
    while True:          
        b = get_command()
        for r in b.rotations():
            bm = best_move.Best_Move(grid, r)
            debug.show(bm.simulate())


main()

