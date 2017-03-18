
def collatz(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        yield n

start=0
maxlength=0
for i in xrange(1, 1000000):
    length = 0
    for j in collatz(i):
        length += 1
    if length > maxlength:
        start = i
        maxlength = length

print('{} len {}'.format(start,maxlength))

