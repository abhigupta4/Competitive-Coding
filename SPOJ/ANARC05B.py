def binary_search(elem,arr,size,low):
	high = size - 1
	while (high >= low):
		mid = (low + high)/ 2
		midval = arr[mid]
		if midval > elem:
			high = mid - 1
		elif midval < elem:
			low = mid + 1
		else:
			return mid
	return -1

while True:
	first = map(int,raw_input().split())
	if first[0] == 0:
		break
	second = map(int,raw_input().split())
	prev_1 = 1
	prev_2 = 1
	sum_main = 0
	sum1 = 0
	sum2 = 0
	for curr_1 in range(1,first[0] + 1):
		curr_2 = binary_search(first[curr_1], second[1:],second[0],0) 
		if curr_2 != -1:
			sum1 = sum(first[prev_1:curr_1 + 1])
			sum2 = sum(second[prev_2:curr_2 + 2])
			temp = max(sum1,sum2)
			sum_main += temp
			prev_1 = curr_1 + 1
			prev_2 = curr_2 + 2
	if prev_1 != first[0] + 1:
		sum1 = sum(first[prev_1:])
		sum2 = sum(second[prev_2:])
		temp = max(sum1,sum2)
		sum_main += temp
	print sum_main