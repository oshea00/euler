from euler import *

for i in xrange(10, 7*math.factorial(9)):
    sumdig = 0
    digits = str(i)
    for d in digits:
        sumdig += math.factorial(int(d))
    if sumdig == i:
        print i
