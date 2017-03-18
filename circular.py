from itertools import permutations
from euler import *


def rotateString(s):
    return s[1:]+s[0]

count=0
for i in xrange(2, 1000000):
    if isprime(i):
        digits = str(i)
        allprime = True
        for i in xrange(len(digits)):
            digits = rotateString(digits)
            pint = int(digits)
            if not isprime(pint):
                allprime = False
                break
        if allprime:
            count += 1
            print pint

print("circular = {}".format(count))



