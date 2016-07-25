import math
for _ in range(input()):
	first_array = map(int,raw_input().split())
	second_array = map(int,raw_input().split())
	min = 1000001
	for i in range(1,first_array[0]):
		for j in range(1,second_array[0]):
			temp = abs(second_array[j] - first_array[i])
			if temp < min:
				min = temp
	print min