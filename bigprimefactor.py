from euler import *

num = 600851475143
factors = primeFactors(num)

if len(factors) == 0:
    print("Number %d is prime" % num)
else:
    print("Largest prime factor = %d" % factors[-1])

print(factors)

