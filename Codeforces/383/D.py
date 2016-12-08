def ii():
	return map(int,raw_input().split())

n,m,w = ii()
wt = ii()
wt = [0] + wt
bt = ii()
bt = [0] + bt

def dfs(node):
	global tot,bty
	di[node] = 1
	lis.append(node)
	tot += wt[node]
	bty += bt[node]
	for ele in g[node]:
		if ele not in di:
			dfs(ele)

di = {}

g = [[] for _ in xrange(n+1)]
for _ in xrange(m):
	a,b = ii()
	g[a].append(b)
	g[b].append(a)

ans = [[0]*1123 for _ in xrange(1123)]

for i in xrange(1,n+1):
	if i not in di:
		tot = 0
		bty = 0
		lis = []
		dfs(i)
		for j in xrange(0,w+1):
			ans[i][j] = ans[i-1][j]
			for ele in lis:
				if wt[ele] <= j:
					ans[i][j] = max(ans[i][j],ans[i-1][j-wt[ele]] + bt[ele])

			if j >= tot:
				ans[i][j] = max(ans[i][j],ans[i-1][j-tot] + bty)

	else:
		for j in xrange(0,w+1):
			ans[i][j] = ans[i-1][j]

print ans[n][w]