from collections import defaultdict

c = 3
trips = defaultdict(lambda: [])

while c < 1000:
    a = 1
    while a < c:
        b = a + 1
        while a < b < c and a + b + c <= 1000:
            if a**2 + b**2 == c**2:
                print('Triplet {} {} {}'.format(a, b, c))
                trips[a+b+c].append([a, b, c])
            b += 1
        a += 1
    c += 1

max = 0
maxk = 0

for k in trips.keys():
    if len(trips[k]) > max:
        max = len(trips[k])
        maxk = k

print maxk
print trips[maxk]