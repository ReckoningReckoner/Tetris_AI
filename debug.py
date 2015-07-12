#Put debugging related methods here

## Displays an array in an easier to view form for the console
def show(obj):
    for y in range(len(obj)):
        for x in range(len(obj[y])):
            print(obj[y][x], end="")
        print("\b")