def permut(n,k):
	if n == 0:
		return 0
	if k == 0:
		return 1
	if dp[n][k] != -1:
		return dp[n][k]
	val = 0
	i = 0
	while(i<n and k-i >= 0):
		val += permut(n-1,k-i)
		i += 1

	dp[n][k] = val
	return val

for _ in xrange(input()):	
	n,k = map(int,raw_input().split())
	dp = [[-1]*(k+1) for i in xrange(n+1)]
	print permut(n,k)