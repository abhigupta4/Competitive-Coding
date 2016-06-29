for _ in xrange(input()):
	n = input()
	time_giv = map(int,raw_input().split())
	time_req = map(int,raw_input().split())
	count = 0
	prev = 0
	for i in xrange(n):
		if time_req[i] <= time_giv[i] - prev:
			count += 1
		prev = time_giv[i]

	print count