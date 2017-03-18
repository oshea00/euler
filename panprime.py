from euler import isprime
from itertools import permutations

maxprime=2
pand=0

for n in xrange(9, 0, -1):
    perms = permutations(xrange(1, n + 1), n)
    for p in perms:
        pan = ''.join([str(c) for c in p])
        if isprime(int(pan)):
            if pan > maxprime:
                maxprime = pan

print maxprime

