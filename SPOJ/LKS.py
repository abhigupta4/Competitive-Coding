S,N = map(int,raw_input().split())
val = []
wt = []

for _ in xrange(N):
	v,w = map(int,raw_input().split())
	wt.append(w)
	val.append(v)

ans = [[0]*(S+1) for i in xrange(N+1)]

for i in xrange(N):
	for j in xrange(1,S+1):
		if wt[i] > j:
			ans[i+1][j] = ans[i][j]
		else:
			ans[i+1][j] = max(val[i] + ans[i][j-wt[i]],ans[i][j])

print ans[N][S]