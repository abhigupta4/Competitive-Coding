end  = int(raw_input())
while (end):
	encrypt = raw_input()
	length = len(encrypt)
	temp = []
	for i in range(end):
		flag = length % (2 * end)
		for j in range(length / (2 * end)):
			temp.append(encrypt[((2 * end) * j) + i])
			temp.append(encrypt[((2 * end) * (j + 1)) - (1 + i)])
		if (flag):
			temp.append(encrypt[((2 * end) * (j + 1) + i)])
	print ''.join(temp)
	end  = int(raw_input())

#DONE
	