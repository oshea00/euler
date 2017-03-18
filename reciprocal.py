import re
from decimal import *
from euler import *

def repeatsAfterN(n, digits):
    """
    Check for repeating groups after skipping a number of digits
    :param digits:
    :return:
        (str) or False
    """
    for i in xrange(2,len(digits)-n+1):
        pattern = r'\d{'+str(n)+r'}(\d{'+str(i)+r'})\1'
        r = re.match(pattern, digits)
        if r:
            return digits[:n], r.group(1)
    return digits, False


def allTheSame(digits):
    """
    Check for all digits the same
    :param digits:
    :return:
        (str) or False
    """

    r = re.match(r'^(\d)\1+$', digits)
    if r:
        return r.group(1)
    else:
        return False


def digitsThatRepeat(digits,num):
    """
    Checks a list of digits for a repeating sequence of digits optionally
    prefixed by a set of digits
    :param
        digits (str): digits to scan
    :return:
        (prefix,repeating)
    """

    r = allTheSame(digits)
    if r:
        return '', r

    skip = int(math.log10(num))
    for i in xrange(skip,len(digits)):
        p, r = repeatsAfterN(i, digits)
        if r:
            if allTheSame(r):
                return digits[0], r[1]
            return p, r

    return p, ''


def digitsInQuotient(n, d, cnt):
    getcontext().prec = cnt-1
    digits = str(Decimal(n)/Decimal(d))[2:].rstrip('0')
    return digits


def findLargestCycle():
    maxrun=0
    recip=0
    repeat=''
    maxprefix=0
    prefix=''

    for i in range(3, 1000):
        if isprime(i):
            p, r = digitsThatRepeat(digitsInQuotient(1, i, 10000),i)
            print('{} - {}({}-{})'.format(i, p, len(r), r))
            if len(r) > maxrun:
                maxrun = len(r)
                recip = i
                repeat = r
            if len(p) > maxprefix:
                maxprefix = len(p)
                prefix = p

    print('1/{} {}-{} repeating {}-{}'.format(recip, maxprefix, prefix, len(repeat), repeat))

findLargestCycle()
