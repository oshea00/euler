from itertools import permutations
from euler import ispandigital

def panproducts():
    count = 0
    sum = 0
    pandigitals = set()

    for pa in permutations(xrange(1, 10), 1):
        a = int(''.join([str(n) for n in pa]))
        for pb in permutations(xrange(1, 10), 4):
            b = int(''.join([str(n) for n in pb]))
            c = a * b
            if ispandigital(str(a)+str(b)+str(c)):
                print('{} x {} = {}'.format(a, b, c))
                pandigitals.add(c)
                sum += c

    for pa in permutations(xrange(1, 10), 2):
        a = int(''.join([str(n) for n in pa]))
        for pb in permutations(xrange(1, 10), 3):
            b = int(''.join([str(n) for n in pb]))
            c = a * b
            if ispandigital(str(a)+str(b)+str(c)):
                print('{} x {} = {}'.format(a, b, c))
                pandigitals.add(c)
                sum += c

    return pandigitals


products = panproducts()
print(products)
print(sum(products))

