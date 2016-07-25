def bfs(start,row1,col1):
	if row_arr[start[0]][start[1]] != '1':
		return
	visited, queue = set(), [start]
	ans[start[0]][start[1]] = 0
	while queue:
		# print queue
		vertex = queue.pop(0)
		if row_arr[vertex[0]][vertex[1]] == '1':
			if vertex != start:
				continue
		if vertex not in visited:
			visited.add(vertex)
			if ans[vertex[0]][vertex[1]] > abs(start[0]- vertex[0]) + abs(start[1] - vertex[1]):
				ans[vertex[0]][vertex[1]] = abs(start[0]- vertex[0]) + abs(start[1] - vertex[1])	

		if vertex[0] + 1 < row1 and (vertex[0]+1,vertex[1]) not in visited:
			queue.append((vertex[0]+1,vertex[1]))
		if vertex[0] - 1 >= 0 and (vertex[0]-1,vertex[1]) not in visited:
			queue.append((vertex[0]-1,vertex[1]))
		if vertex[1] + 1 < col1 and (vertex[0],vertex[1]+1) not in visited:
			queue.append((vertex[0],vertex[1]+1))
		if vertex[1] - 1 >= 0 and (vertex[0],vertex[1]-1) not in visited:
			queue.append((vertex[0],vertex[1]-1))
for _ in xrange(input()):
	try:
		row,col = map(int, raw_input().split())
		row_arr = []
		for i in xrange(row):
			row_arr.append(raw_input())
		ans = [[400 for j in xrange(col)] for k in xrange(row)]
		for i in xrange(row):
			for j in xrange(col):
				bfs((i,j),row,col)
		for i in xrange(row):
			for j in xrange(col):
				print ans[i][j],
			print 
	except:
		pass