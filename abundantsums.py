from euler import *

# greatest 28123
'''
def isabundant(n):
    return propersum(n) > n

abundant = file('abundant.txt', 'w')

for i in range(1,28124):
    isit = isabundant(i)
    if isit:
        print(i)
        abundant.write("%s\n" % i)

abundant.close()
'''

fin = file('abundant.txt','r')
abundant = []
abundantsums = {}
for line in fin:
    abundant.append(int(line.strip()))

for i in xrange(len(abundant)):
    for j in xrange(len(abundant)):
        abundantsums[abundant[i]+abundant[j]] = True

total = 0
for i in xrange(28124):
    if i not in abundantsums:
        print i
        total += i

print('sum %d\n' % total)


