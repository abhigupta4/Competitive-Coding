for _ in range(input()):
	string1 = raw_input()
	string2 = raw_input()
	graph1 = {}
	flag = 0
	for ele in string1:
		graph1[ele] = 1
	for ele2 in string2:
		if ele2 in graph1:
			flag = 1
			break
	if flag == 1:
		print "Yes"
	else:
		print "No"

#AC