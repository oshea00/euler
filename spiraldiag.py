
# 1*1 3*3          5*5            7*7
# 1   2  2  2  2   4   4   4   4   6
# 1,  3, 5, 7, 9, 13, 17, 21, 25, 31

diags = [1]

for x in xrange(2,1001,2):
    for y in xrange(4):
        diags.append(diags[-1]+x)

print sum(diags)
print diags

