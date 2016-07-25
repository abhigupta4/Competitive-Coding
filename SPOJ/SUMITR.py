for _ in xrange(input()):
	r = input()
	t = [[0]*(r+1) for i in xrange(row+1)]
	for i in xrange(r):
		c = map(int,raw_input().split())
		for j in xrange(i+1):
			t[i+1][j+1] = c[j] + max(t[i][j],t[i][j+1])
	print max(t[r])