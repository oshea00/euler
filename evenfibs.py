import euler


def sumEvenFibsLessThan(num):
    fibs = [];
    i = 1
    while True:
        f = euler.fib(i)
        i += 1
        if f < num:
            fibs.append(f)
        else:
            break

    return sum([n for n in fibs if n%2 == 0])


print("Sum even fibs = %d" % sumEvenFibsLessThan(4000000))
