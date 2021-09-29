#https://www.codewars.com/kata/59ccf051dcc4050f7800008f

from math import isqrt

sum_dict = {1:0, 2:1, 3:1, 4:3, 5:1, 6:6, 7:1, 8:7, 9:4, 10:8}

def s(n):
    if n in sum_dict:
        return sum_dict[n]
    else:
        total = 1
        root = isqrt(n)
        if root*root == n:
            total += root
            limit = root
        else:
            limit = root + 1
        for i in range(2,limit):
            if n % i == 0:
                total += i + n//i
        sum_dict[n] = total
        return total

def buddy (start,limit):
    for n in range(start,limit+1):
        m = s(n)-1
        if s(m) == n+1 and m > n:
            return [n,m]
    return "Nothing"

print(buddy(320,441))
print(s(48))
print(s(75))