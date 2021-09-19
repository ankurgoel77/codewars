#https://www.codewars.com/kata/5772382d509c65de7e000982/train/python

u_dict = {
    1:1,
    2:1,
        }

def u(n):
    if n in u_dict:
        return u_dict[n]
    else:
        t = u(n-u(n-1)) + u(n-u(n-2))
        u_dict[n] = t
        return t

def length_sup_u_k(n, k):
    count = 0
    for i in range(1,n+1):
        if u(i) >= k:
            count += 1
    return count

def comp(n):
    count = 0
    for i in range(2,n+1):
        if u(i) < u(i-1) :
            count += 1
    return count
    

print(length_sup_u_k(3332,973))
print(comp(74626))
