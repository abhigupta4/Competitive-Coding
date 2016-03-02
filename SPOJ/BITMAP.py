def bfs(graph,start):
	visited, queue = set(), [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			if row_arr[vertex[0]][vertex[1]] == '1':
				return vertex
			visited.add(vertex)
			for ele in graph[vertex]:
				if ele not in visited:
					queue.append(ele)

for _ in range(input()):
	row,col = map(int, raw_input().split())
	row_arr = []
	graph = {}
	for _ in range(row):
		row_arr.append(raw_input())
	for i in range(row):
		for j in range(col):
			graph[(i,j)] = []
			if (i - 1) >= 0:
				graph[(i,j)].append((i - 1,j))
			if (i + 1) <= row - 1:
				graph[(i,j)].append((i + 1,j))
			if (j - 1) >= 0:
				graph[(i,j)].append((i,j - 1))
			if (j + 1) <= col - 1:
				graph[(i,j)].append((i,j + 1))
	
	for i in range(row):
		for j in range(col):
			temp = bfs(graph,(i,j))
			print abs(i - temp[0]) + abs(j - temp[1]),
		print
	raw_input()