from euler import *

total = 0
for n in xrange(1,1000000):
    if ispalindrome(n):
        b = str(bin(n)[2:]).lstrip('0')
        #print b
        if ispalindrome(b):
            print('{} - {}'.format(n,b))
            total += n

print("Total = {}".format(total))