for _ in range(input()):
	list1 = []
	numb = input()
	flag = 0
	for i in range(numb):
		list1.append(raw_input())
	list1.sort()
	for i in range(numb - 1):
		if list1[i] in list1[i + 1]:
			flag = 1

	if flag == 1:
		print "NO"
	else:
		print "YES"