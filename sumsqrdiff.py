from euler import *

n = 20
print sumseries(1, 1, n)**2 - sum((s**2 for s in range(1, n+1)))


