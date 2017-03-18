from itertools import product

ways = 0

c = (p for p in product(xrange(2),xrange(3),xrange(5),xrange(11),xrange(21),xrange(41),xrange(101),xrange(201)))

count = 0

for p in c:
    count += 1
    if p[0] * 200 + p[1] * 100 + p[2] * 50 + p[3] * 20 + p[4] * 10 + p[5] * 5 + p[6] * 2 + p[7] == 200:
        ways += 1
        print("Count {} Ways {}".format(count/1000000,ways))

print("Grand Total {}".format(ways))

