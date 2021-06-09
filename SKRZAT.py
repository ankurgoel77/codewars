# https://www.codewars.com/kata/528a0762f51e7a4f1800072a

#pre-calculate all decimal to weird binary values:
dec_dict = {0: '0'}
weird_vals = [(-2)**k for k in range(0,15)]

for k in range (1, 32768):
    weird_bin_str  = format(k,'b')
    reverse_bin_str = weird_bin_str[::-1]
    dec_val = sum([weird_vals[i]*int(reverse_bin_str[i]) for i in range(0,len(reverse_bin_str))])
    dec_dict[dec_val] = weird_bin_str

def skrzat(base, number):
    if base == 'b':
        val = 0
        for k in range(0,len(number)):
            val += ((-2)**k) * int(number[(len(number)-k-1)])
        return f'From binary: {number} is {val}'
    else:
        return f'From decimal: {number} is {dec_dict[number]}'
    pass