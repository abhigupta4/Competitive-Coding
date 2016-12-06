n,m,k = map(int,raw_input().split())
g = [[] for _ in xrange(n+1)]
for _ in xrange(m):
	u,v,l = map(int,raw_input().split())
	g[u].append((v,l))
	g[v].append((u,l))

ans = 10**12
flour = []

if k:
	flour = map(int,raw_input().split())
	di = {}

	for ele in flour:
		di[ele] = 1

	for ele in flour:
		for v,l in g[ele]:
			if v not in di:
				ans = min(ans,l)

	if ans == 10**12:
		print -1
	else:
		print ans 
else:
	print -1