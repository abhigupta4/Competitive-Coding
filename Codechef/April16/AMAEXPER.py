def dfs(start,parent,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if len(graph[start]) == 1:
    	if graph[start][0][0] == parent:
    		return 

    for next in graph[start]:
    	if next[0] not in visited:
        	dfs(next[0],start, visited)

    max1 = 0
    for next in graph[start]:
    	if next[0] != parent:
    		if next[1] + height[next[0]] > max1:
    			long_path[start] = [next[0]] + long_path[next[0]]
    			max1 = height[next[0]] + next[1] 
   	height[start] = max1

    return visited

def centre(start):
	

for _ in xrange(input()):
	N = input()
	graph = [[] for _ in xrange(N + 1)]
	height = [0 for _ in xrange(N+1)]
	long_path =[[] for _ in xrange(N+1)]
	for __ in xrange(N-1):
		u,v,w = map(int,raw_input().split())
		graph[u].append((v,w))
		graph[v].append((u,w))
	# wt = 0
	# for ele in graph[0]:
	# 	if ele[1] > wt:
	# 		wt = ele[1]
	# print wt
	# for i in xrange(N-1):
	# 	print 0
	dfs(1,0)