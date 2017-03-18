from euler import *

def primeList(list,n):
    if isprime(n):
        list.append(n)
        return True
    else:
        return False


def quadratic(a, b, i):
    return i**2 + a*i + b


def maxQuadraticPrimes():
    maxlist = []
    maxa = 0
    maxb = 0
    for a in xrange(-999,1000):
        for b in xrange(-999,1001):
            if (a / 100) * 100 == a and (b/100)*b == b:
                print('a={}'.format(a))
            list = []
            i=0
            while primeList(list,quadratic(a, b, i)):
                i += 1
            if len(list) > len(maxlist):
                maxlist = list
                maxa = a
                maxb = b

    print('a={} b={} a*b={} listlength={}'.format(maxa, maxb, maxa*maxb, len(maxlist)))
    print(maxlist)

maxQuadraticPrimes()