from math import log

def sumdigitsbypower(n,p):
    total = 0
    num = str(n)
    for d in num:
        total += (int(d)**p)
    return total

total = 0
for i in xrange(2,1000000):
    if i == sumdigitsbypower(i, 5):
        total += i
        print(i)

print("total {}".format(total))