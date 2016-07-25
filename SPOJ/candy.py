def candy(temp,numb):
	tempsum = sum(temp)
	transfer = 0
	compare = tempsum / numb
	if (tempsum % numb):
		return -1
	else:
		for val in temp:
			if(val > compare):
				transfer += (val - compare)
		return transfer

number = int(raw_input())
while (number != -1):
	arr = []
	for i in range(number):
		var = int(raw_input())
		arr.append(var)
	#print arr
	return_v = candy(arr,number)
	print return_v
	number = int(raw_input())

