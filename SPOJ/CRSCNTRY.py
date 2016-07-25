def lcs():
	n = len(A)
	m = len(B)
	dp = [[0]*(n+1) for i in xrange(m+1)]
	for i in xrange(m+1):
		for j in xrange(n+1):
			if i and j:
				if A[j-1] == B[i-1]:
					dp[i][j] = dp[i-1][j-1] + 1
				else:
					dp[i][j] = max(dp[i-1][j],dp[i][j-1])
	return dp[m][n]

for _ in xrange(input()):
	ans = -1
	A = map(int,raw_input().split())
	B = map(int,raw_input().split())
	while B[0] != 0:
		ans = max(ans,lcs())
		# print lcs()
		B = map(int,raw_input().split())
	print ans-1