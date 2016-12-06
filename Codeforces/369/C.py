n,m,k2 = map(int,raw_input().split())
col = map(int,raw_input().split())

for i in xrange(n):
	col[i] -= 1

cost = []
for _ in xrange(n):
	cost.append(map(int,raw_input().split()))


dp = [[[10**12]*(m) for _ in xrange(k2+1)] for a in xrange(n)]


if col[0] == -1:
	for i in xrange(m):
		dp[0][1][i] = cost[0][i]
else:
	dp[0][1][col[0]] = 0


for i in xrange(1,n):
	for j in xrange(1,k2+1):
		if col[i] == -1:
			for k in xrange(m):
				for l in xrange(m):
					if k != l:
						dp[i][j][k] = min(dp[i][j][k],dp[i-1][j-1][l]+cost[i][k])
					else:
						dp[i][j][k] = min(dp[i][j][k],dp[i-1][j][l]+cost[i][k])
		else:
			for l in xrange(m):
				if l != col[i]:
					dp[i][j][col[i]] = min(dp[i-1][j-1][l],dp[i][j][col[i]])
				else:
					dp[i][j][col[i]] = min(dp[i-1][j][l],dp[i][j][col[i]])

ans = 10**12
for i in xrange(m):
	ans = min(ans,dp[n-1][k2][i])

if ans == 10**12:
	print -1
else:
	print ans

