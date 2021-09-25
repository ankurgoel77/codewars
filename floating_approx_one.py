# https://www.codewars.com/kata/58184387d14fc32f2b0012b2/python

# Use taylor series at https://math.stackexchange.com/questions/732540/taylor-series-of-sqrt1x-using-sigma-notation

from math import *

def f(x):
    total = (x/2) - (x**2)/8
    for n in range(3,10):
        term = (x**n) * ((-1)**(n-1))
        term *= factorial(2*n-3) / factorial(n) / factorial(n-2)
        term /= 2**(2*n-2)
        total += term
    return total

print(f(5.0e-06))