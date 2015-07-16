from random import randint


def prioritize_lines_removed(a):
    a = sorted(a, key=lambda x: x[2])
    most_removed = a[-1][2]

    for i in range(len(a)-1,-1,-1):
        if a[i][2] > most_removed:
            a.pop(i)
    return a
            

def prioritize_smallest_tower(a):
    a.sort(key=lambda x: x[0])
    lowest_height = a[0][0]
    
    for i in range(len(a)-1, -1, -1):
        if a[i][0] > lowest_height:
            a.pop(i)
    return a
            
def prioritize_number_of_holes(a):
    a = sorted(a, key=lambda x: x[1])
    lowest_holes = a[0][1]
    
    for i in range(len(a)-1, -1, -1):
        if a[i][1] > lowest_holes:
            a.pop(i)
    return a
    
def prioritize_closest_left(a):
    a = sorted(a, key=lambda x: x[3][1])
    return a
 
#Finds the absolute best move from a list of possible moves
def final(a):
    # For setting up combos
    # a = prioritize_number_of_holes(a)
    # a = prioritize_smallest_tower(a)
    # a = prioritize_lines_removed(a)

    
    # For clearing lines when combos are too high
    # a = prioritize_lines_removed(a)
    # a = prioritize_smallest_tower(a)
    # a = prioritize_number_of_holes(a)


    a = prioritize_closest_left(a)
    return a[0]