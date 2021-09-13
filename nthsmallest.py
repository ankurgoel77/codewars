# https://www.codewars.com/kata/57a03b8872292dd851000069/train/python

def nth_smallest(arr, n):
    sorted_list = sorted(list(set(arr)))
    if n > len(sorted_list):
        return None
    else :
        return sorted_list[n-1]
