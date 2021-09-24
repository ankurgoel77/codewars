#https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

def is_valid_IP(strng):
    octets = strng.split(".")
    if len(octets) != 4 :
        return False
    for octet in octets:
        if len(octet) == 0:
            return False
        if len(octet) > 1 and octet[0] == '0':
            return False
        if octet != octet.strip():
            return False
        try:
            x = int(octet)
        except:
            return False
        if x < 0 or x > 255:
            return False
    return True