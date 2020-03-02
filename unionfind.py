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
			if this.componentSize[a]<this.componentSize[b]:
				this.components[a]=b
				this.componentSize[b] += this.componentSize[a]
			else:
				this.components[b]=a
				this.componentSize[a] += this.componentSize[b]
			this.componentCount -= 1
		
V = [0,1,2,3,4,5,6]
E = [(0,1),(0,2),(0,3),(1,2),(2,3),(4,5),(5,6)]

from console import clear
clear()
n = UnionFind(len(V))
for e in E:
	n.union(e[0],e[1])
print(n.components)
print(n.componentSize)
print(n.connected(0,3))
print(n.connected(0,5))
