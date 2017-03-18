# English pence
P = [200, 100, 50, 20, 10, 5, 2]


# Recursively find combinations
def f(p, t):
    if len(p) > 0:
        p_ = p[0]
        return sum([f(p[1:], t-p_*n) for n in range(1 + t // p_)])
    else:
        return 1


# Find combos of pence at target 200
print(f(P, 200))

