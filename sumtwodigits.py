#https://www.codewars.com/kata/52217066578afbcc260002d0/train/python

from math import isqrt
squares = {i**2:i for i in range(0,46341)}

# doesn't work for 1
def all_squared_pairs(n):
    if n == 1:
        return [[0,1]]
    result = []
    limit = isqrt((n+1) // 2) +1
    for i in range(0,limit):
        key = n - i**2
        if n - i**2 in squares:
            result.append([i,squares[key]])
    return result