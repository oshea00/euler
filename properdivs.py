from euler import *

def sumproper(n):
    return sum(divisors(n))-n

def amicablepair(a):
    b = sumproper(a)
    aprime = sumproper(b)
    if a == aprime and a != b:
        return a, b
    return -1,-1

nums = []
for i in range(4,10000):
    a, b = amicablepair(i)
    if a != -1:
        print(a)
        nums.append(a)

print sum(nums)