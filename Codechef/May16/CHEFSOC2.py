max1 = 10**9 + 7
for _ in xrange(input()):
	N,pstren,begin = map(int,raw_input().split())
	stren = map(int,raw_input().split())
	matrix = [[0 for i in xrange(N)] for j in xrange(pstren+1)]
	matrix[0][begin-1] = 1
	for i in xrange(pstren):
		for j in xrange(N):
			if (j - stren[i]) >= 0:
				matrix[i+1][j] += matrix[i][j-stren[i]]
			if (stren[i] + j) < N:
				matrix[i+1][j] += matrix[i][j+stren[i]]

	for ele in matrix[pstren]:
		print ele%max1,
	print