data = \
    [[75],
    [95,64],
    [17,47,82],
    [18,35,87,10],
    [20,4,82,47,65],
    [19,1,23,75,3,34],
    [88,2,77,73,7,63,67],
    [99,65,4,28,6,16,70,92],
    [41,41,26,56,83,40,80,70,33],
    [41,48,72,33,47,32,37,16,94,29],
    [53,71,44,65,25,43,91,52,97,51,14],
    [70,11,33,28,77,73,17,78,39,68,17,57],
    [91,71,52,38,17,14,91,43,58,50,27,29,48],
    [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
    [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

def visitleft(n):
    if n[0] > 0 and n[1] > 0:
        return n[0] - 1, n[1] - 1
    return -1, 0


def visitright(n):
    if n[0] > 0 and n[0] > n[1]:
        return n[0]-1, n[1]
    return 0, -1

def memoize(f):
    hash = {}
    def wrapper(x):
        if x not in hash:
            hash[x] = f(x)
        return hash[x]
    return wrapper

def pathsTo(n):
    paths = []

    if n == (0,0):
        paths = [[(0,0)]]
    else:
        if visitleft(n) != (-1 , 0):
            pl = pathsTo(visitleft(n))
            for p in pl:
                p.append(n)
                paths.append(p)
        if visitright(n) != (0, -1):
            pr = pathsTo(visitright(n))
            for p in pr:
                p.append(n)
                paths.append(p)

    return paths

def sumpath(p):
    t = 0
    for r, c in p:
        t += data[r][c]
    return t

#pathsTo = memoize(pathsTo)

maxpath = []
maxsum = 0
lastrow = len(data)-1
for c in range(len(data[lastrow])):
    paths = pathsTo((lastrow, c))
    for p in paths:
        psum = sumpath(p)
        if psum > maxsum:
            maxsum = psum
            maxpath = p

print(maxpath)
print(maxsum)
