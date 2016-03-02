for _ in range(input()):
	N,M,K = map(int, raw_input().split())
	hearts = map(int, raw_input().split())
	total = (N * (N + 1) * M * (M + 1))/4
	sum = 0
	for ele in hearts:
		row = (ele - 1)/M
		col = (ele - 1) % M
		sum += ((col + 1)* (row + 1) *(M - col) * (N - row))
	print float(sum)/float(total)

#DONE