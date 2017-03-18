from euler import ispentagonal


def pentagonal():
    n = 1
    yield (n*3-1)/2
    n += 1

print [p for p in pentagonal() if p > 1]







