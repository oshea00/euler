# Traverse graph to find "square" paths.
# List paths and total number.
# 00--01--02--03--04
# |   |       |   |   
# 05--06--07--08--09
# |   |   |   |   |
# 10  11--12--13  14
# |   |   |   |   |
# 15--16--17--18--19
# |   |       |   |
# 20--21--22--23--24 
#
cols=5
graph = {
	0 : [1,5],
	1 : [0,2,6],
	2 : [1,3],
	3 : [2,4,8],
	4 : [3,9],
	5 : [0,6,10],
	6 : [1,5,7,11],
	7 : [6,8,12],
	8 : [3,7,9,13],
	9 : [4,8,14],
	10 : [5,15],
	11 : [6,12,16],
	12 : [7,11,13,17],
	13 : [8,12,18],
	14 : [9,19],
	15 : [10,16,20],
	16 : [11,15,17,21],
	17 : [12,16,18],
	18 : [13,17,19,23],
	19 : [14,18,24],
	20 : [15,21],
	21 : [16,20,22],
	22 : [21,23],
	23 : [18,22,24],
	24 : [19,23]
}

def dispGraph():
	for y in range(0,cols):
		for x in range(0,cols):
			sep = "  "
			if x < cols-1 and y*cols+x+1 in graph[y*cols+x]:
				sep = "--"
			print(f'{y*cols+x:2}{sep}',end='')
		print()
		print(' ',end='')
		for x in range(0,cols):
			down = "   "
			if y < cols-1 and y*cols+x in graph[(y+1)*cols+x]:
				down = "|  "
			print(down,end=' ')
		print()

def getDirectionOffset(dir,dist):
	if dir == 1: # N
		return (0,-dist)
	if dir == 2: # W
		return (-dist,0)
	if dir == 3: # S
		return (0,dist)
	if dir == 4: # E
		return (dist,0)
	return (cols,cols)

def isInbounds(row,col,dist,dir):
	coloff, rowoff = getDirectionOffset(dir,dist)
	if not 0 <= row + rowoff < cols:
		return False
	if not 0 <= col + coloff < cols:
		return False
	return True
				
def isSquarePossibleAt(row,col,size):
	for dir in range(1,5):
		coloff, rowoff = getDirectionOffset(dir,size)
		if not isInbounds(row,col,size,dir):
			return False
		row += rowoff
		col += coloff
	return True

def pathWalkSquare(row,col,size):
	path = []
	if isSquarePossibleAt(row,col,size):
		for dir in range(1,5):
			coloff, rowoff = getDirectionOffset(dir,1)
			for _ in range(0,size):
				node1 = row*cols+col
				node2 = (row+rowoff)*cols+(col+coloff)
				if not node1 in graph[node2]:
					return []
				path.append(node1)
				row += rowoff
				col += coloff
		return path
	return []

import console
console.clear()

paths = []
dispGraph()
for row in range(0,cols):
	for col in range(0,cols):
		for dist in range(1,cols+1):
			path = pathWalkSquare(row,col,dist)
			if len(path) > 0:
				paths.append(path)
				
print(f'Number of squares = {len(paths)}')
print('Paths:')
for p in paths:
	print(p)

	
