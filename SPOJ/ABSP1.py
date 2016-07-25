for _ in range(input()):
	N = input()
	array = map(int, raw_input().split())
	sum1 = tot_sum = 0
	for index in range(N - 1):
		if(index == 0):
			for j in range(1,N):
				sum1 += array[j] - array[0]
			tot_sum += sum1
		else:
			temp = array[index] - array[0]
			tot_sum += sum1 - (N - index) * temp
	print tot_sum

#TLE