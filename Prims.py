def printEdges(V,E):
	for e in E:
		print(f'{V[e[0]]}-{V[e[1]]} cost:{e[2]}')

def unvisitedEdges(visited,E):
	u = []
	for e in E:
		if (e[0] in visited) and (not e[1] in visited):
				u.append(e)
	return u 

from console import clear
clear()

V = ['A','B','C','D']
E = [(0,1,1),(0,2,4),(0,3,3),
	(1,3,2),(2,3,5)]

span = []
visited = [0]

while True:
	unvisited = unvisitedEdges(visited,E)
	if len(unvisited) == 0:
		break
	cheapest = sorted(unvisited,key=lambda x: x[2])[0]
	span.append(cheapest)
	visited.append(cheapest[1])

print("Graph:")
printEdges(V,E)
print("Spanning:")	
printEdges(V,span)

