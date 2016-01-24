def danger(list1):
	length = len(list1)
	if(length == 1):
		return list1
	elif (length % 2) :
		for i in range((length / 2) - 1, -1, -1):
			del list1[(2 * i) + 1]
		del list1[0]
		return danger(list1)
	else:
		for i in range((length / 2) - 1, -1, -1):
			del list1[(2 * i) + 1]
		return danger(list1)

def danger_number(numb):
	return int(string[0] * 10 ) + int(string[1]) * (10 ** int(string[3]))

def first_list(numb):
	list1 = []
	if(numb % 2):
		for i in range(1, (numb / 2) + 1):
			list1.append((2 * i) + 1)
		return list1
	else:
		for i in range((numb / 2)):
			list1.append((2 * i) + 1) 
		return list1

while True:
	string = raw_input()
	print danger(first_list(int(string)))
	