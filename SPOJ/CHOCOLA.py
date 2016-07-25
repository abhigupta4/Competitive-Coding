def choc(m,n):
	f = 1
	s = 1
	st1 = 0
	st2 = 0
	cost = 0
	while(st1 < m-1 and st2 < n-1):
		if fir[st1] >= sec[st2]:
			cost += fir[st1] * s
			st1 += 1
			f += 1
		else:
			cost += sec[st2] * f
			st2 += 1
			s += 1
	while (st1 < m-1):
		cost += fir[st1]*s
		st1 += 1
	while (st2 < n-1):
		cost += sec[st2]*f
		st2 += 1
	return cost

for _ in xrange(input()):
	raw_input()
	m,n = map(int,raw_input().split())
	fir = []
	sec = []
	for i in xrange(m-1):
		fir.append(input())
	for i in xrange(n-1):
		sec.append(input())
	fir.sort(reverse=1)
	sec.sort(reverse=1)
	print choc(m,n)