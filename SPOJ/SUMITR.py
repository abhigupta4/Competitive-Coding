for _ in range(input()):
	tri = []
	for _ in range(input()):
		tri.append(map(int,raw_input().split()))
	[[tri[0][0]  for i in range(n + 1)] for j in range(n)]
	# new[0][1] = tri[0][0]
	# new = [[(tri[l][k] + max(new[l-1][k + 1],new[l-1][k])) for k in range(1,l + 1)] for l in range(1,n)]
	# print new
	print tri