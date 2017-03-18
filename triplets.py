from euler import *

for a, b, c in threeVarSumsOf(1000):
    if a**2 + b**2 == c**2:
        print('{} {} {}'.format(a,b,c))
        print('a*b*c = {}'.format(a*b*c))






