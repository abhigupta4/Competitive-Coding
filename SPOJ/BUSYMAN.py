for _ in xrange(input()):
	di = {}
	lis = []
	n = input()
	for i in xrange(n):
		a,b = map(int,raw_input().split())
		if b in di:
			di[b] = max(a,di[b])
		else:
			lis.append(b)
			di[b] = a
	lis.sort()
	end = lis[0]
	count = 1
	for i in xrange(1,len(lis)):
		if di[lis[i]] >= end:
			count += 1
			end = lis[i]
	print count