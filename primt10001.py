import euler


def prime10001():
    i = 2
    cnt = 0
    lastPrime = 0
    while cnt < 10001:
        if euler.isprime((i)):
            cnt += 1
            lastPrime = i
        i += 1
    return lastPrime

print(prime10001())
