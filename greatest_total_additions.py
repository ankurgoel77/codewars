# https://www.codewars.com/kata/568f2d5762282da21d000011

from itertools import permutations

def gta(limit, *args): # find the base_list first
    numbers = [str(i) for i in args]
    max_len = max([len(n) for n in numbers])
    digit_set = set()
    digit_list = []

    for i in range(0,max_len):
        for num in numbers:
            if i >= len(num):
                continue
            digit = int(num[i])
            if not digit in digit_set:
                digit_set.add(digit)
                digit_list.append(digit)
    digit_list = digit_list[:limit]

    total = 0
    for i in range(1, limit+1):
        p = permutations(digit_list, i)
        for tups in p:
            total += sum(tups)
    return total