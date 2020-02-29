# build huffman code
# based on alphabet frequency

class Tree:
	def __init__(this,val=None,left=None,right=None):
		this.left = left
		this.right = right
		this.val = val
	def __repr__(this):
		return str(this.val)
		
	def display(this):
		def displayT(this,lvl):
			if this == None:
				return
			displayT(this.right,lvl+1)
			print(f"{'  '*lvl}{this}")
			displayT(this.left,lvl+1)
		displayT(this,0)
		
	def find(this,v):
		def findD(this,v,path):
			if this == None:
				return ''
			if v==this.val[0]:
				return path
			left = findD(this.left,v,path+'0')
			right = findD(this.right,v,path+'1')
			return left + right
		return findD(this,v,'')

class Huffman:
	def __init__(this,a):
		this.A = [c[0] for c in a]
		this.F = [Tree(n) for n in a]
		while len(this.F) > 1:
			f = sorted(this.F,key=lambda x:x.val[1])[:2]
			this.F.remove(f[0])
			this.F.remove(f[1])
			this.F.append(this.mergeTrees(f[0],f[1]))
			
	def mergeTrees(this,a,b):
		if b.val[0] < a.val[0]:
			a, b = b, a
		return Tree(('*',round(a.val[1]+b.val[1],2)),a,b)
		
	def displayTree(this):
		this.F[0].display()
		
	def displayCode(this):
		for v in this.A:
			print(f'{v} = {this.F[0].find(v)}')							
						
# letter frequencies
a = [('A',3),('B',2),('C',6),('D',8),('E',2),('F',6)]
h = Huffman(a)
h.displayTree()
print()
h.displayCode()
