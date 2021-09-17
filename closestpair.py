# https://www.codewars.com/kata/5376b901424ed4f8c20002b7/python
# Use Rabin random algorithm described at https://rjlipton.wpcomstaging.com/2009/03/01/rabin-flips-a-coin/

import random
import math



def get_min(points) :
    min_d = math.inf
    for i in range(0,len(points)):
        for j in range(i+1, len(points)):
            x = points[j][2] - points[i][2]
            y = points[j][3] - points[i][3]
            d = math.sqrt((x**2) + (y**2))
            if d < min_d:
                min_d = d
    return min_d

def closest_pair(points):
    # first, all points should be placed into a unit square
    (x_min, y_min, x_max, y_max) = (points[0][0], points[0][1], points[0][0], points[0][1])
    for p in points:
        if p[0] < x_min:
            x_min = p[0]
        elif p[0] > x_max:
            x_max = p[0]
        if p[1] < y_min:
            y_min = p[1]
        elif p[1] > y_max:
            y_max = p[1]

    scale = 1 / max((x_max-x_min), (y_max-y_min))

    # re-cast all points as tuple of points as (x, y, unit_x, unit_y)
    upoints = []
    for p in points:
        upoints.append((
            p[0],
            p[1],
            (p[0]-x_min)*scale,
            (p[1]-y_min)*scale
        ))

    k = math.ceil(math.sqrt(len(upoints)))
    s = random.sample(upoints,k)
    #print(get_min(s))
    d = get_min(s)
    
    num_sides = math.ceil(1 / d)  #not sure I need this yet

    

    #assign all points to a checkerboard with squares of side d


    pass



points = (
            (2, 2), # A
            (2, 8), # B
            (5, 5), # C
            (6, 3), # D
            (6, 7), # E
            (7, 4), # F
            (7, 9)  # G
        )

print(closest_pair(points))


