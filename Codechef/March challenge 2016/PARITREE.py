for _ in range(input()):
	node, query = map(int, raw_input().split())
	graph = {}
	for i in range(1,node + 1):
		graph[i] = []
	for _ in range(node - 1):
		u, v = map(int, raw_input().split())
		graph[u].append(b)
	