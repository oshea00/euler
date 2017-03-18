from euler import *

t = 0
for p in primes():
    if p < 2000000:
        t += p
    else:
        print(t)
        break

