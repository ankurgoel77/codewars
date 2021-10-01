#https://www.codewars.com/kata/60aa29e3639df90049ddf73d/python

def binarray(s)->int:
    n = len(s)
    start = 0
    end = 0
    start_dict = {0:[0]}
    end_dict = {}

    if s[0] == 0:
        end = -1
        end_dict[-1] = [0]
    else:
        end = 1
        end_dict[1] = [0]

    for i in range(1,n):
        start = end
        if start in start_dict:
            start_dict[start].append(i)
        else:
            start_dict[start] = [i]

        if s[i]==0:
            end = start - 1
        else:
            end = start + 1

        if end in end_dict:
            end_dict[end].append(i)
        else:
            end_dict[end] = [i]

    longest = 0
    for k in end_dict:
        if k in start_dict:
            val = end_dict[k][-1] - start_dict[k][0] + 1
            if val > longest:
                longest = val
    return longest
