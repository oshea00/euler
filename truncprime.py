from euler import isprime

total = 0

for n in xrange(11,1000000):
    if isprime(n):
        isleft = True
        isRight = True
        p = str(n)
        if '0' in p:
            continue
        for i in xrange(1, len(p)):
            ltrunc = int(p[i:])
            if not isprime(ltrunc):
                isleft = False
                break
            rtrunc = int(p[:len(p)-i])
            if not isprime(rtrunc):
                isRight = False
                break
        if isleft and isRight:
            total += n
            print n

print("Total: {}".format(total))

