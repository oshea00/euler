from euler import *

tree = [      [0],\
            [0,  0],\
          [0,  10,  0],\
        [0,  0,  0,  11]]


maxlvl = len(tree)


def left(lvl, c):
    if lvl + 1 < maxlvl:
        return lvl+1, c
    else:
        return -1, -1


def right(lvl, c):
    if lvl + 1 < maxlvl:
        return lvl+1, c+1
    else:
        return -1, -1


def visit(tree, lvl, c):
    print("{}({},{})".format(tree[lvl][c]),lvl,c)


def traverse(lvl, c):
    if lvl == -1:
        return
    traverse(*left(lvl, c,))
    visit(tree, lvl, c)
    traverse(*right(lvl, c))


def printtree(tree):
    h = len(tree)
    for l in xrange(h):
        print('  '*(h-l)),
        for c in xrange(len(tree[l])):
            print("[{}]".format(tree[l][c])),
        print
    print


def copyTree(tree):
    copy = []
    for r in xrange(len(tree)):
        copy.append([])
        for c in xrange(len(tree[r])):
            copy[r].append(tree[r][c])
    return copy


def addparents(tree, r,c):
    if r-1 > -1:
        if c-1 > -1:
            tree[r][c] += tree[r-1][c-1]
        if c < len(tree[r-1]):
            tree[r][c] += tree[r-1][c]


def maxsumpath(tree):
    printtree(tree)
    ctree = copyTree(tree)
    for r in xrange(len(ctree)):
        for c in xrange(len(ctree[r])):
            # this needs tweaking - polynomial? - or we want Cnr of parents in tree?
            ctree[r][c] = CnR(r,c) * tree[r][c]
            addparents(ctree, r, c)
    printtree(ctree)

    # Looking at the ctree - the largest number on the last row is the ending point
    # of the largest path. We should follow that upwards...
    r = len(ctree)-1
    maxc=0
    maxpath = []
    maxsum = 0
    maxval = 0
    for c in xrange(len(ctree[r])):
        if ctree[r][c] > maxval:
            maxval = ctree[r][c]
            maxsum = tree[r][c]
            maxc = c
    c = maxc
    while r - 1 > -1:
        leftp = rightp = -1
        if c - 1 > -1:
            leftp = tree[r - 1][c - 1]
        if c < len(tree[r - 1]):
            rightp = tree[r - 1][c]
        if leftp == -1 and rightp == -1:
            maxpath.append(r, c)
            maxsum += tree[r][c]
            break
        if leftp == -1:
            maxpath.append((r, c))
            maxsum += rightp
            r -= 1
            continue
        if rightp == -1:
            maxpath.append((r, c))
            maxsum += leftp
            r -= 1
            c -= 1
            continue
        if leftp > rightp:
            maxpath.append((r, c))
            maxsum += leftp
            r -= 1
            c -= 1
        else:
            maxpath.append((r, c))
            maxsum += rightp
            r -= 1
    maxpath.append((0,0))
    print maxpath
    print maxsum

maxsumpath(tree)




