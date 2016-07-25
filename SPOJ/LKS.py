S,N = map(int,raw_input().split())
val = []
wt = []

for _ in xrange(N):
	v,w = map(int,raw_input().split())
	wt.append(w)
	val.append(v)

flag = 0

ans = [[0]*(S+1) for i in xrange(2)]

# ans = [[0]*(S+1) for i in xrange(N+1)]

for i in xrange(N):
	for j in xrange(1,S+1):
		if wt[i] > j:
			ans[not flag][j] = ans[flag][j]
		else:
			ans[not flag][j] = max(val[i] + ans[flag][j-wt[i]],ans[flag][j])
	flag = not flag

print ans[flag][S]