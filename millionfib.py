# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/train/python

# fib(2k) = fib(k)* (2*fib(k+1) - fib(k))
# fib(2k+1) = fib(k+1)**2 + fib(k)**2

import functools

@functools.lru_cache()
def fib(n):
    if n < 0:
        f = 1
        f_1 = 0
        for c in range(-1,n-1,-1):
            f_2 = f - f_1
            f = f_1
            f_1 = f_2
        return f_2
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2: 
        return 1
    elif n % 2 == 0:
        return fib(n//2)*(2*fib(n//2 + 1) - fib(n//2))
    else:
        return (fib(n//2 + 1) **2) + (fib(n//2)**2)

print(fib(-5))