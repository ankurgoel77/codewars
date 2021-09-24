#https://www.codewars.com/kata/51f082ba7297b8f07f000001

def find_in_array(seq, predicate): 
    for count, value in enumerate(seq):
        if predicate(value,count) :
            return count
    return -1