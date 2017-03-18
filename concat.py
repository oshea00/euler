from euler import *


def concatproduct(p, n):
    conprod = ''
    for m in n:
        prod = str(p * m)
        conprod += prod
    return conprod


maxpan = '0'
num = 0
a = 0

for i in xrange(9, 500000):
    n = []
    for j in xrange(1, 7):
        n.append(j)
        c = concatproduct(i, n)
        if ispandigital(c):
            if int(c) > int(maxpan):
                maxpan = c
                num = i
                a = j

print maxpan
print num
print a
print ispandigital(maxpan)


