from euler import *
i=1
while True:
    if len(str(fib(i))) >= 1000:
        print(i)
        break
    i += 1