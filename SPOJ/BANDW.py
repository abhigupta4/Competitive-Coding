while True:
	string1, string2 = raw_input().split()
	if string1 == '*':
		break
	length = len(string1)
	count = 0
	flag = 0
	for i in range(length):
		if(string1[i] == string2[i]):
			if flag == 1:
				count += 1
				flag = 0
		else:
			flag = 1
	if flag:
		count += 1
	print count 

#DONE