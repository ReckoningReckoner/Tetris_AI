## Rotates an array n number of times
# returns array of rotations
def all(obj, n):
    rots = []
    for i in range(n):
        rots.append(obj)
        obj = rotate_clockwise(obj)
        
    return rots

##rotates an clockwise left 90 degrees
def rotate_clockwise(obj):
    return transpose(reverse_row(obj))
    
##reverses each individual array in an array of arrays
# ex:
# [[1,2,3],[4,5,6]]
# => [[3,2,1],[6,5,4]]
def reverse_row(obj):
    for i in range(len(obj)):
        obj[i] = list(reversed(obj[i]))
    
    return obj


##flips x, y coordinates of array of arrays
def transpose(obj):
    transpose = []
    for i in range(len(obj[0])):
        t = []
        for j in range(len(obj)):
            t.append(0)
        transpose.append(t)
    
    for y in range(len(obj)):
        for x in range(len(obj[y])):
            transpose[x][y] = obj[y][x]
            
    return transpose
        

