for _ in range(input()):
	number = int(raw_input())
	string = raw_input()
	length = len(string)
	arr = [0] * 8
	for i in range(length - 2):
		substring = string[i:i+3]
		if (substring == "TTT"):
			arr[0] += 1
		elif (substring == "TTH"):
			arr[1] += 1
		elif (substring == "THT"):
			arr[2] += 1
		elif(substring == "THH"):
			arr[3] += 1
		elif(substring == "HTT"):
			arr[4] += 1
		elif(substring == "HTH"):
			arr[5] += 1
		elif(substring == "HHT"):
			arr[6] += 1
		else:
			arr[7] += 1
	print number, 
	for ele in arr:
		print ele,
