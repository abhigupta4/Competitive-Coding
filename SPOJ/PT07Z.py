def recursive_dfs(graph, start, path = [], depth = 0):
    path += [start]
    #print path
    for node in graph[start]:
        if not node in path:
            depth += 1
            path, depth = recursive_dfs(graph, node, path, depth)
            #print "node" + str(node) + "depth" + str(depth)
            if len(graph[node]) == 1:
                list_deep.append(depth)
                list_node.append(node)
    depth -= 1
    return path, depth
    
N = int(raw_input())
graph = {}
list_deep = []
list_node = []
for _ in range(N-1):
    a, b = map(int, raw_input().split())
    if not a in graph.keys():
        graph[a] = set()
    graph[a].add(b)
    if not b in graph.keys():
        graph[b] = set()
    graph[b].add(a)

recursive_dfs(graph, graph.keys()[0])
#print list_deep
#print list_node
temp = list_node[list_deep.index(max(list_deep))]
#print "temp is " + str(temp)
list_deep = []
list_node = []
recursive_dfs(graph, temp, [])
print max(list_deep) + 1
#print list_node