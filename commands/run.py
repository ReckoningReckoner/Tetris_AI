from modules import debug
from modules import builder
from modules import simulate
from modules.prioritize import final
from moves import best_move
from random import randint
from instructions import instructions
import sys
show_debug = False

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
    
    while True: 
        c,removed = 0,0
        block = get_command()
            
        #BEST IS IN THE FORM OF:
        #[columns-removed_rows, HOLES, removed_rows, [y_c,x_c]]
        best = best_move.single_best_move(block, grid, float(HEIGHT-1-simulate.first_empty_row(grid))/float(HEIGHT-1))
        
        if best != None:
            new_grid = simulate.place(best[3][0], best[3][1], grid, best[4], block.type(), "dc")
            instructions.get_moves(new_grid, grid,best[4], best[3])            
            if show_debug:
                print("Move:")
                print(best[0:4])
                print("Before fall:")
                debug.show(new_grid)
            
            grid = simulate.drop_lines(new_grid)
            
            

            # if show_debug:
     #            print("After fall:")
     #            debug.show(grid)
     #            removed += best[2]
     #            c +=1
     #            print"Combo", best[2]
     #            print"Removed", removed
     #            print"Height", best[0]
     #            print"Round",c
        else:
            print "Game over"
            return
        
