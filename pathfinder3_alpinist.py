#https://www.codewars.com/kata/576986639772456f6f00030c/solutions/python

from math import inf
from heapq import *

def path_finder(area):
    print(area)
    lines = area.split("\n")
    n = len(lines) 

    visited = [[False for x in range(0,n)] for y in range(0,n)]
    distance = [[inf for x in range(0,n)] for y in range(0,n)]
    weights = [[0 for x in range(0,n)] for y in range(0,n)]
    distanceq = []

    for i in range(0,n):
        for j in range(0,n):
            weights[i][j] = int(lines[i][j])

    x,y = 0,0
    distance[0][0] = 0
    heappush(distanceq,(distance[x][y],x,y))
    while True:
        v = heappop(distanceq)
        while visited[v[1]][v[2]] and len(distanceq) > 0:
            v = heappop(distanceq)
        if (v[1]==n-1) and (v[2]==n-1):
            return distance[v[1]][v[2]]
        else:
            #calculate tentative distance to all unvisited neighbors:
            cur_dist, x,y = v[0], v[1], v[2]
            if x>0 and not visited[x-1][y]:
                test_distance = cur_dist + abs(weights[x-1][y] - weights[x][y])
                if test_distance < distance[x-1][y]:
                    heappush(distanceq, (test_distance, x-1, y))
                    distance[x-1][y] = test_distance
            if x<n-1 and not visited[x+1][y]:
                test_distance = cur_dist + abs(weights[x+1][y] - weights[x][y])
                if test_distance  < distance[x+1][y]:
                    heappush(distanceq, (test_distance , x+1, y))
                    distance[x+1][y] = test_distance 
            if y>0 and not visited[x][y-1]:
                test_distance = cur_dist + abs(weights[x][y-1] - weights[x][y])
                if test_distance < distance[x][y-1]:
                    heappush(distanceq, (test_distance,x,y-1))
                    distance[x][y-1] = test_distance
            if y<n-1 and not visited[x][y+1]:
                test_distance = cur_dist + abs(weights[x][y+1] - weights[x][y])
                if test_distance < distance[x][y+1]:
                    heappush(distanceq, (test_distance,x,y+1))
                    distance[x][y+1] = test_distance
            visited[x][y] = True

        if len(distanceq) == 0:
            return False