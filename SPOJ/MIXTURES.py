def compute(l,r):
	if dp[l][r] != -1:
		return dp[l][r]
	if r == l:
		dp[l][r] = 0
		return 0
	ans = 10**12
	for i in xrange(r-l):
		ans = min(ans,compute(l,l+i)+compute(l+i+1,r)+((sum(lis[l:l+i+1])%100) *(sum(lis[l+i+1:r+1])%100)))

	dp[l][r] = ans
	return ans

while True:
	try:
		n = input()
		dp = [[-1]*n for i in xrange(n)]
		lis = map(int,raw_input().split())
		print compute(0,n-1)
	except:
		break