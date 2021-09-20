# https://www.codewars.com/kata/5d98b6b38b0f6c001a461198/train/python

def code(strng):
    result = ""
    for c in strng:
        digit = ord(c)-ord("0")
        binary = format(f"{digit:b}")
        k = len(binary)
        result += "".join(["0"]*(k-1)) + "1" + binary
    return result
    
def decode(strng):
    current = 0
    i = strng.find("1",current)
    result = ""
    while i >= 0 :
        k = i-current + 1
        current = i+1
        binary = strng[current:current+k]
        digit = int(binary,2)
        result += str(digit)
        current += k
        i = strng.find("1",current)
    return result

print(decode("10001111"))