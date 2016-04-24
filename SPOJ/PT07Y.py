def dfs(current):
  visited[current] = 1
  ret = 1
  for child in graph[current]:
    if not visited[child]:
      ret += dfs(child)
  return ret

N, M = map(int, raw_input().split())
graph = [[] for i in xrange(N)]
visited = [0 for i in xrange(N)]
for _ in range(M):
    a, b = map(int, raw_input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

if N != M + 1:
    print "NO"
else:
    if dfs(0) == N:
        print "YES"
    else:
        print "NO"