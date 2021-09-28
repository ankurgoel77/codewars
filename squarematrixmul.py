#https://www.codewars.com/kata/5263a84ffcadb968b6000513/train/python

def matrix_mult(a, b):
    n = len(a)
    c = [[0]*n for i in range(0,n)]
    for i in range(0,n):
        for j in range(0,n):
            total = 0
            for k in range(0,n):
                total += a[i][k] * b[k][j]
            c[i][j] = total
    return c