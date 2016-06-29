#TLE
def palin(string):
	len1 = len(string)
	dp = [[0]*(len1+1) for i in xrange(len1+1)]
	for i in xrange(len1):
		for j in xrange(len1):
			if string[j] == string[len1-i-1]:
				dp[i+1][j+1] = dp[i][j] + 1
			else:
				dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

	return len1 - dp[i+1][j+1]

for _ in xrange(input()):
	string = raw_input()
	print palin(string)