# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b

import re

def last_coef_writer(coef):
    if coef > 0:
        return f"+{coef}"
    elif coef < 0:
        return f"{coef}"

def coef_writer(coef):
    if coef == 1:
        return "+"
    elif coef == -1:
        return "-"
    elif coef > 0:
        return f"+{coef}"
    elif coef < 0:
        return f"{coef}"

def first_coef_writer(coef):
    if coef == 1:
        return ""
    elif coef == -1:
        return "-"
    elif coef > 0:
        return f"{coef}"
    elif coef < 0:
        return f"{coef}"

def expand(expr):
    csplit = expr.split("^")
    bi = csplit[0]
    power = int(csplit[1])
    if power == 0:
        return "1"
    bi = bi.replace("(","").replace(")","")
    pattern = "([a-z])"
    split_list = re.split(pattern, bi)
    if split_list[0] == "":
        x = 1
    elif split_list[0] == "-":
        x = -1
    else:
        x = int(split_list[0])
    letter = split_list[1]
    y = int(split_list[2])
    
    #solve with Pascal's triangle
    coef_list = [0]*(power+1)

    pascal = 1
    coef_list[0] = (x**(power))
    for i in range(1,power+1):
        pascal = int(pascal*(power+1-i)/i)
        coef_list[i] = (x**(power-i)) * (y**i) * pascal

    # coef_list = [-9,0,-4,2]
    # power = 3
    termlist = [""]*(power+1)

    for i in range(0,power+1):
        coef = coef_list[i]
        if coef == 0:
            continue
        if i == 0:
            termlist[i] = f'{first_coef_writer(coef)}{letter}{"^" + str(power-i) if (power-i) > 1 else ""}'
        elif i == power:
            termlist[i] = f'{last_coef_writer(coef)}'
        elif coef > 0:
            termlist[i] = f'{coef_writer(coef)}{letter}{"^" + str(power-i) if (power-i) > 1 else ""}'
        elif coef < 0:
            termlist[i] = f'{coef_writer(coef)}{letter}{"^" + str(power-i) if (power-i) > 1 else ""}'
    
    return "".join(termlist)