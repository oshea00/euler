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

class Graph:
	def __init__(this,A,V,E):
		this.A = A
		this.V = V
		this.E = E
	def display(this):
		for e in E:
			print(f'{this.A[e[0]]}-{this.A[e[1]]}')
A = ['A','B','C','D','E','F','G']
V = [0,1,2,3,4,5,6]
E = [(0,1),(0,2),(0,3),(1,2),(2,3),(4,5),(5,6)]

from console import clear
clear()
g = Graph(A,V,E)
n = UnionFind(len(V))
for e in E:
	n.union(e[0],e[1])
g.display()
print(n.components)
print(n.componentSize)
print(n.componentCount)
print(n.connected(0,3))
print(n.connected(0,5))
print(n.find(4))
