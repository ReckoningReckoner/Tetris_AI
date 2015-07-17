from modules import debug
from modules import builder
from modules import simulate
from modules.prioritize import final
from moves import best_move
from random import randint
import sys
show_debug = True

def get_command():
        s = raw_input('> ')
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
                   
def play():
    WIDTH  = 8
    HEIGHT = 20
    grid   = [[0 for w in range(WIDTH)] for h in range(HEIGHT)] ##Default 8x20 Grid
    # grid = [[0, 0, 0, 0, 0, 0, 0, 0], #Custom grid for testing
            # [0, 0, 0, 0, 0, 0, 0, 0],
          #   [0, 0, 0, 0, 0, 0, 0, 0],
          #   [0, 0, 0, 0, 0, 0, 0, 0],
          #   [0, 0, 0, 0, 0, 0, 0, 0],
          #   [0, 0, 0, 0, 0, 0, 0, 0],
          #   [0, 0, 0, 1, 1, 1, 1, 0],
          #   [1, 1, 1, 1, 1, 1, 1, 1],
          #   [1, 1, 1, 1, 1, 1, 1, 1]]

    print("Press any key to simulate a round with a random block")
    print("Pressing the lowercase name of a block will generate said block")
    print("Press 'q' to exit")
    c,removed = 0,0
    
    while True: 
        block = get_command()
                
        if float(HEIGHT-1-simulate.first_empty_row(grid))/float(HEIGHT-1) < 0.25:
            mode = 0
        else:
            mode = 1
            
        best = best_move.single_best_move(block, grid, mode)
        
        if best != None:
            grid = simulate.place(best[3][0], best[3][1], grid, best[4], block.type())

            if show_debug:
                print("Move:")
                print(best[0:4])
                print("Before fall:")
                debug.show(grid)

            grid = simulate.drop_lines(grid)

            if show_debug:
                print("After fall:")
                debug.show(grid)
                removed += best[2]            
                c +=1
                print"Combo", best[2]
                print"Removed", removed
                print"Height", best[0]
                print"Round",c
                # print"Percent full", percent_full
                print"Mode", mode 
        else:
            print "Game over"
            return
        
