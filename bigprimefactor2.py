import euler

num = 600851475143
r = num
factors = []
root = (num/2)+1

for i in xrange(2, root+1):
    if euler.isprime((i)):
        if r > 1:
            while (r/i)*i == r:
                r = (r/i)
                factors.append(i)
        else:
            break

if len(factors) == 0:
    print("Number %d is prime" % num)
else:
    print("Largest prime factor = %d" % factors[-1])

print(factors)