# https://www.codewars.com/kata/581ee0db1bbdd04e010002fd/train/python

import math
def interp(f, l, u, n):
    return [math.floor(f(l + x*(u-l)/n)*100.0)/100.0 for x in range(0,n)]


print(interp(lambda x : x, 0, 9.0, 4))