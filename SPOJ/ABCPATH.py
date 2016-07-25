def dfs(row,col,i,j,ans):
	# print "hi"
	# print i,j
	global max1
	max1 = max(max1,ans)
	for verti in xrange(-1,2,1):
		if i + verti < row and i + verti >= 0:
			for hori in xrange(-1,2,1):
				if j + hori < col and j + hori >= 0:
					# print i+verti,j+hori
					if ord(grid[i+verti][j+hori]) == ord(grid[i][j]) + 1:
						if visited[i+verti][j+hori] != 1:
							visited[i+verti][j+hori] = 1
							dfs(row,col,i+verti,j+hori,ans+1) 

case = 1
while True:
	row,col = map(int,raw_input().split())
	if row + col == 0:
		break
	grid = []
	for i in xrange(row):
		grid.append(raw_input())
	max1 = 0
	visited = [[-1] * col for _ in xrange(row)]
	for i in xrange(row):
		for j in xrange(col):
			if grid[i][j] == 'A':
				visited[i][j] = 1
				dfs(row,col,i,j,1)

	print "Case " + str(case) + ": " + str(max1)
	case += 1
