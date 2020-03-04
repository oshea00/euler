# kruskals min spanning algo.
# uses uniondfind to check if vertices
# in edge are connected (would cause cycle).
# and sorts edges by cost, resulting in
# cheapest spanning path.
class UnionFind:
	def __init__(this,size):
		this.components = [i for i in range(size)]
		this.componentSize = [1]*size
		this.componentCount = len(this.components)
	def find(this,a):
		while this.components[a] != a:
			a = this.components[a]
		return a
	def connected(this,a,b):
		return this.find(a) == this.find(b)
	def union(this,a,b):
		if not this.connected(a,b):
			ia = this.find(a)
			ib = this.find(b)
			if this.componentSize[ia] > this.componentSize[ib]:
				ia, ib = ib, ia
			this.components[ia]=ib
			this.componentSize[ib] += this.componentSize[ia]
			this.componentCount -= 1

def printEdges(V,E):
	for e in E:
		print(f'{V[e[0]]}-{V[e[1]]} cost:{e[2]}')

from console import clear
clear()

V = ['A','B','C','D']
E = [(0,1,1),(0,2,4),(0,3,3),
	(1,3,2),(2,3,5)]

g = UnionFind(len(V))
span = []
S = sorted(E,key=lambda x: x[2])
for e in S:
	if not g.connected(e[0],e[1]):
		span.append(e)
		g.union(e[0],e[1])

print("Graph:")
printEdges(V,E)
print("Spanning:")	
printEdges(V,span)
