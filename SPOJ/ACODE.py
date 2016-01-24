def acode(numb):
	list1 = [10, 20]
	arr = []
	arr.append(1)
	arr.append(1)
	string = str(numb)
	if (numb < 10 or numb in list1):
		return 1
	elif(numb <= 26):
		return 2
	else:
		length = len(string)
		for i in range(1, length):
			if (int(string[i]) == 0):
				if (i == 1):
					arr.append(1)
				else:
					arr.append(arr[i - 1])
			elif (int(string[i -1 :i +1]) <= 26 and int(string[i -1 :i +1]) > 9):
				arr.append(arr[i ] + arr[i - 1])
			else:
				arr.append(arr[i])
	return arr[length]
while True:
	number = int(raw_input())
	if(number != 0):
		print acode(number)
	else:
		break

#DONE