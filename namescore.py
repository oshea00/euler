
names = file('p022_names.txt','r').readline().split(",")
names = sorted([n.replace('"','').upper() for n in names])

def pos(a):
    return int(ord(a) - 64)

def wordscore(word):
    return sum([pos(l) for l in name])

totalscore = 0
for i,name in enumerate(names):
    wordscore = sum([pos(l) for l in name])
    totalscore += wordscore * (i+1)
print(totalscore)