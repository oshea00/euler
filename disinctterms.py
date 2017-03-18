
list = set()
for a in xrange(2,101):
    for b in xrange(2,101):
        list.add(a**b)

print (len(list))