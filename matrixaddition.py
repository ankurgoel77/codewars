#https://www.codewars.com/kata/526233aefd4764272800036f/train/python

def matrix_addition(a, b):
    n = len(a)
    result = [0]*n
    for i in range(0,n):
        result[i] = [0]*n
        for j in range(0,n):
            result[i][j] = a[i][j] + b[i][j]
    return result