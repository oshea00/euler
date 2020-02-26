
names = sorted([n.replace('"','').upper() for n in open('words.txt','r').readline().split(",")])

totalscore = 0
for i,name in enumerate(names):
    wordscore = sum([int(ord(a) - 64) for a in name])
    totalscore += wordscore * (i+1)
print(totalscore)
