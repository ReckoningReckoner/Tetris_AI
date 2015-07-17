## Prints an array in an easier to view form for the console
def show(obj):
    for y in range(len(obj)):
        for x in range(len(obj[y])):
            if obj[y][x] == 0:
                print('_'),
            else:
                print(obj[y][x]),
        print("")
        
## Shows all rotations of a piece
def print_r(it):
    for r in it:
        show(r)
        print("")