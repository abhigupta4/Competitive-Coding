for _ in range(input()):
	string = raw_input().split()
	max1 = 0
	count = 0
	length = 0
	for ele in string:
		temp = len(ele)
		if temp == length:
			count += 1
		else:
			count = 1
			length = temp
		if count > max1:
			max1 = count
	print max1

#DONE