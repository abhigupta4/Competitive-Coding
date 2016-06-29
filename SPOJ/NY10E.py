def ndec(n):
	lis = [[0]*10 for i in xrange(n)]
	lis[0] = [1]*10
	for i in xrange(n-1):
		lis[i+1][0] = 1
		for j in xrange(1,10):
			lis[i+1][j] = lis[i+1][j-1] + lis[i][j]
	return sum(lis[n-1])
for i in xrange(input()):
	a,n = map(int,raw_input().split())
	print a,ndec(n)