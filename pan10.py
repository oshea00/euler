from itertools import permutations
from euler import ispandigital10

nums = []

perms = permutations("0123456789", 10)

for p in perms:
    sp = ''.join(p)
    if ispandigital10(sp):
        found = True
        for i, n in enumerate([2, 3, 5, 7, 11, 13, 17]):
            sub = int(sp[i+1:i+1+3])
            if sub != (sub / n) * n:
                found = False
                break
        if found:
            nums.append(sp)
            print sp

print sum([int(n) for n in nums])

