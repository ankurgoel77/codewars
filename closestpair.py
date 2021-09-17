# https://www.codewars.com/kata/5376b901424ed4f8c20002b7/python
# Use Rabin random algorithm described at https://rjlipton.wpcomstaging.com/2009/03/01/rabin-flips-a-coin/

import random
import math

def closest_pair(points):
    # first, loop through all points to get footprint of the points
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

    if (x_max-x_min) > (y_max-y_min):
        (w_max, w_min) = (x_max, x_min)
    else:
        (w_max, w_min) = (y_max, y_min)

    # get the minimum distance from a random sample of sqrt(n) of points
    k = math.ceil(math.sqrt(len(points)))
    s = random.sample(points,k)
    d = math.inf
    for i in range(0,len(s)):
        for j in range(i+1, len(s)):
            x = s[j][0] - s[i][0]
            y = s[j][1] - s[i][1]
            hyp = math.sqrt((x**2) + (y**2))
            if hyp < d:
                d = hyp
            if (x,y) == (0,0):  # points are the same, and hence distance is zero
                return ((s[i][0],s[i][1]),(s[j][0],s[j][1]))
    
    #assign all points to a checkerboard with squares of side d
    # the checkerboard will have a number of sides equal to (w_max-w_min) / d
    board = {}
    for p in points:
        index = (math.floor((p[0]-x_min) / d), math.floor((p[1]-y_min) / d))
        if index in board:
            board[index].append(p)
        else:
            board[index] = [p]

    d_min = math.inf
    pair = ((0,0),(0,0))

    # first,  for every filled square he computes the closest pair
    for index, points in board.items():
        for i in range(0,len(points)):
            for j in range(i+1, len(points)):
                x = points[j][0] - points[i][0]
                y = points[j][1] - points[i][1]
                d = math.sqrt((x**2) + (y**2))
                if d < d_min:
                    d_min = d
                    pair = ((points[i][0], points[i][1]), (points[j][0], points[j][1]))

    # second, for every filled square adjaced to a filled square, compute the closest pair (if they share a vertex), so we need to check 8 adjacent squares for each filled square
    for index, points in board.items():
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                if (index[0]+i, index[1]+j) in board :
                    for p1 in points:
                        for p2 in board[(index[0]+i, index[1]+j)]:
                            x = p1[0] - p2[0]
                            y = p1[1] - p2[1]
                            d = math.sqrt((x**2) + (y**2))
                            if d < d_min:
                                d_min = d
                                pair = ((p1[0],p1[1]),(p2[0],p2[1]))
    return pair



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

points =(
        (2, 2), # A
        (2, 8), # B
        (5, 5), # C
        (5, 5), # C
        (6, 3), # D
        (6, 7), # E
        (7, 4), # F
        (7, 9)  # G
)

print(closest_pair(points))

