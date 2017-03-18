import math
from itertools import combinations
from collections import defaultdict


def isprime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


def ispalindrome(n):
    s = str(n)
    end = len(s) - 1
    start = 0
    if start == end:
        return True
    while start < end:
        if s[start] != s[end]:
            return False
        end -= 1
        start += 1
    return True


def fib(n):
  a, b = 0, 1
  while n > 0:
    a, b = b, a+b
    n -= 1
  return a

def product(list):
    return reduce(lambda x, y: x*y, list)


def sumseries(start, inc, n):
    nth = start + (inc * (n-1))
    return n*(start + nth)/2


def factorExponent(p,num):
    if p < 2:
        return 0
    ntimes = 0
    r = num
    while (r / p) * p == r:
        r /= p
        ntimes += 1
    return ntimes

def primeFactors(num):
    factors = []
    root = (num / 2) + 1
    i = 2
    r = num
    while i < root + 1 and r > 1:
        if isprime(i):
            exp = factorExponent(i, r)
            if exp > 0:
                r /= i ** exp
                factors.append(i)
        i += 1
    return factors


def smallestCommonDividend(factors):
    primes = []
    for f in factors:
        ffactors = primeFactors(f)
        if len(ffactors) == 0:
            primes.append(f)
        else:
            for ff in ffactors:
                exp = factorExponent(ff, f)
                for n in xrange(0, exp - primes.count(ff)):
                    primes.append(ff)
    return product(primes)


def isqrt(n):
    x = n
    y = (x + 1) / 2
    while y < x:
        x = y
        y = (x + n / x) / 2
    return x

def isPerfectSquare(n):
    if isqrt(n)**2 == n:
        return True
    else:
        return False

def sequentialTriplets(csqr):
    f, i = math.modf(math.sqrt(csqr))
    a = i - 2
    b = a+1
    c = a**2 + b**2
    if c == csqr:
        return int(a), int(b), int(c)
    else:
        return 0, 0, 0

def threeVarSumsOf(n):
    a = 1
    b = a + 1
    while a < n/3+1:
        c = n - a - b
        while a < b < c:
            yield a, b, c
            b += 1
            c = n - a - b
        a += 1
        b = a + 1


def nprimes(n):
    i = 2
    cnt = 0
    while cnt < n:
        if isprime(i):
            cnt += 1
            yield i
        i += 1


def primes():
    i = 2
    while i > 1:
        if isprime(i):
            yield i
        i += 1


def trianglenums():
    i = 1
    while i > 0:
        yield sumseries(1, 1, i)
        i += 1


def primeFactorization(num):
    expfacs = []
    facs = primeFactors(num)
    if len(facs) == 0:
        expfacs.append(num)
    else:
        for f in facs:
            fexp = factorExponent(f, num)
            for i in range(fexp):
                expfacs.append(f)
    return expfacs


def divisors(n):
    allfacs = [1]
    facs = primeFactorization(n)
    for i in range(1, len(facs)+1):
        for c in combinations(facs, i):
            allfacs.append(product(c))
    return set(allfacs)


def PnR(n, r):
    return math.factorial(n)/math.factorial(n-r)


def CnR(n, r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))


def propersum(n):
    return sum(divisors(n))-n


def factorials():
    n = 0
    while True:
        yield math.factorial(n)
        n += 1


def ispandigital(n):
    digits = str(n)
    if len(digits) != 9:
        return False
    h = defaultdict(int)
    for d in digits:
        h[d] += 1
    for c in '123456789':
        if h[c] == 0 or h[c] > 1:
            return False
    return True


def ispandigital10(n):
    if len(n) != 10:
        return False
    if n[0] == '0':
        return False
    h = defaultdict(int)
    for d in n:
        h[d] += 1
    for c in '0123456789':
        if h[c] == 0 or h[c] > 1:
            return False
    return True


def gcd(u, v):
    while u > 0:
        if u < v:
            t = u
            u = v
            v = t
        u = u % v
    return v


def pos(a):
    return int(ord(a) - 64)


def wordscore(word):
    return sum([pos(l) for l in word])


def isTriangle(t):
    n = t*8 + 1
    k = int(math.sqrt(n))
    if k*k == n:
        return True
    else:
        return False

def ispentagonal(n):
    t = 24*n + 1
    if isPerfectSquare(t):
        if isqrt(t) % 6 == 5:
            return True
    return False
