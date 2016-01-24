list1 = map(int, raw_input().split())
while (sum(list1) != -8):
	max = 0
	for i in range(4):
		temp = float(list1[i]) / list1[i + 4]
		if temp > max:
			max = temp
	if (max > int(max)):
		max += 1
	list2 = []
	for i in range(4):
		temp = (int(max) * list1[i + 4] ) - list1[i]
		list2.append(temp)
	for num in list2:
		print num,
	list1 = map(int, raw_input().split())

#DONE