# https://www.codewars.com/kata/562c94ed7549014148000069/train/python

# pre-generate all triples with p up to 1000000
triples = {}
for m in range(1,1000):
    for n in range(1,m):
        a1 = m**2 - n**2
        b1 = 2*m*n
        c1 = m**2 + n**2
        k = 1
        a = a1*k
        b = b1*k
        c = c1*k
        p = a+b+c
        while p <= 1000000:
            if p in triples:
                triple=tuple(sorted([a,b,c]))
                triples[p].add(triple)
            else:
                triple=tuple(sorted([a,b,c]))
                triples[p] = set()
                triples[p].add(triple)
            k += 1
            a = a1*k
            b = b1*k
            c = c1*k
            p = a+b+c

def integer_right_triangles(p):
    if p in triples:
        return sorted([list(v) for v in triples[p]])
    else:
        return []