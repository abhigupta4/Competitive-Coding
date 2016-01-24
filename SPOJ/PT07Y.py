def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
        path=recursive_dfs(graph, node, path)
  return path

#graph = {'A':['B','C'],'B':['A'],'C':['A']}
#print 'recursive dfs ', recursive_dfs(graph, 'A')

graph = {}
N, M = map(int, raw_input().split())
for _ in range(M):
    a, b = map(int, raw_input().split())
    if a in graph.keys():
        graph[a].add(b)
    else:
        graph[a] = set()
        graph[a].add(b)
    if b not in graph.keys():
        graph[b] = set()

if N != M + 1:
    print "NO"
else:
    if len(recursive_dfs(graph, graph.keys()[0])) == N:
        print "YES"
    else:
        print "NO"