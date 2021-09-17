# https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python

def last_digit(n1, n2):
    pdict = {
        0: [0,0,0,0],
        1: [1,1,1,1],
        2: [6,2,4,8],
        3: [1,3,9,7],
        4: [6,4,6,4],
        5: [5,5,5,5],
        6: [6,6,6,6],
        7: [1,7,9,3],
        8: [6,8,4,2],
        9: [1,9,1,9],
    }
    
    if n2 == 0:
        return 1
    
    return pdict[n1 % 10][n2 % 4]