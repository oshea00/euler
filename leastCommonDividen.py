from euler import *

scd = smallestCommonDividend(range(1,21))

f = ''
for p in primeFactors(scd):
    exp = factorExponent(p,scd)
    if exp > 1:
        f = f + str(p)+'^'+str(exp)+' * '
    else:
        f = f + str(p)+' * '
print(f[:-3]+' = '+str(scd))


