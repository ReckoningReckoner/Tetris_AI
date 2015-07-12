#Put debugging related methods here
#Many more to come

## Prints an array in an easier to view form for the console
def show(obj):
    for y in range(len(obj)):
        for x in range(len(obj[y])):
            if obj[y][x] == 0:
                print('-', end='')
            else:
                print(obj[y][x], end="")
        print("")
        
## Shows all arrays in an iterable
def print_r(it):
    for r in it:
        show(r)
        print("")