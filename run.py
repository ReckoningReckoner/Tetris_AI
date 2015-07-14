import builder
import debug
import best_move
import placer
import sys
from random import randint

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
    
    while True: 
        b = get_command()        
        try: 
            a = []
            for r in b.rotations():
                bpm = best_move.Best_Possible_Moves(grid, r)
                sim = bpm.simulate()
                if sim == None: 
                    return
                else:
                    a.append(sim)
                
            best = best_move.final(a)
            grid = placer.place(best[2][0], best[2][1], grid, best[3], b.type())
            
            if show_debug:
                print("Run best moves:")
                print(best[0:3])
                debug.show(grid)
                
        except:
            print(Exception)