
#https://www.codewars.com/kata/5f134651bc9687000f8022c4
from collections import Counter
from pprint import pprint

def find(n):
    seq = [0,1,2,2]

    for i in range(3,n+1):
        seq.extend([i]*seq[i])
        if len(seq) > n:
            break
    pprint(seq)
    return seq[n]

def find2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 2

    count = 5
    i = 3
    seq = [[3,2]]
    current = 0
    while count < n:
        i += 1
        seq.append([i, seq[current][0]])
        count += seq[current][0]
        seq[current][1] -= 1
        if seq[current][1] == 0:
            current += 1
    return i

from collections import deque
def find3(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 2

    count = 5
    i = 3
    seq=deque()
    seq.append([3,2])
    while count < n:
        i += 1
        seq.append([i, seq[0][0]])
        count += seq[0][0]
        seq[0][1] -= 1
        if seq[0][1] == 0:
            seq.popleft()
    return i

def find4(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    count = 2
    x = 1  # loop counter
    i = 1  # seq(n)
    prev_i = i
    prev_count = count
    while count < n:
        x += 1
        prev_i= i
        prev_count = count
        i += x // 2 + 1
        count += x*(x // 2 + 1)
    return prev_i + (n-prev_count) // x + 1


#find(82668285)
n = 2000
#print (f"find: {find(n)}   find2:{find2(n)}")
#print(find3(n))
print(find2(n),find4(n))
find(100)