from euler import wordscore, isTriangle

words = file('p042words.txt','r').readline().split(",")
words = sorted([n.replace('"','').upper() for n in words])

trianglewords = []

for w in words:
    if isTriangle(wordscore(w)):
        trianglewords.append(w)

print trianglewords
print len(trianglewords)

