for _ in range(input()):
	N,K = map(int,raw_input().split())
	N_arr = map(int,raw_input().split())
	N_arr.sort()
	min = N_arr[K-1] - N_arr[0]
	for i in range(1,(N-K) + 1):
		value = N_arr[i + K - 1] -N_arr[i]
		if (value < min):
			min = value
	print min

#DONE