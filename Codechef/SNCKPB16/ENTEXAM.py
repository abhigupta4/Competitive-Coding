for _ in xrange(input()):
	n,k,e,m = map(int,raw_input().split())
	lis = []
	for _ in xrange(n-1):
		lis.append(sum(map(int,raw_input().split())))
	lis.sort()
	last = sum(map(int,raw_input().split()))
	if (lis[n-k-1] + 1) - last <= m:
		print max(0,(lis[n-k-1] + 1) - last)
	else:
		print "Impossible"