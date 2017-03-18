from itertools import permutations
from decimal import *

def digitfractions():
    twodigits = []
    for pa in permutations(xrange(1, 10), 2):
        a = int(''.join([str(n) for n in pa]))
        for pb in permutations(xrange(1, 10), 2):
            b = int(''.join([str(n) for n in pb]))
            c = Decimal(a) / Decimal(b)
            if c < 1:
                if pa[0] == pb[1] and pa[1] == pb[0]:
                    continue
                if pa[0] == pb[1] or pa[1] == pb[0]:
                    if canceldigits(a, b):
                        print('{} / {} = {}'.format(a, b, c))
                        twodigits.append((a, b))
    return twodigits


def canceldigits(a, b):
    digitincommon = ''
    sa = str(a)
    sb = str(b)
    for da in sa:
        if da in sb:
            digitincommon = da
    ra = int(sa.replace(digitincommon, ''))
    rb = int(sb.replace(digitincommon, ''))
    if round(Decimal(ra)/Decimal(rb), 6) == round(Decimal(a)/Decimal(b), 6):
        return a, b
    else:
        return False

print digitfractions()





