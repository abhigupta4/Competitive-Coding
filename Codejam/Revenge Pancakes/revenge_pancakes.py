for case in range(input()):
	str1 = raw_input()
	ele = str1[0]
	count = 0
	for i in range(1,len(str1)):
		if str1[i] != ele:
			ele = str1[i]
			count += 1
	if ele == '-':
		count += 1
	print "Case #" + str(case + 1) + ": " + str(count)