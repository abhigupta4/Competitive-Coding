for _ in range(input()):
	len1 = input()
	string = raw_input()
	dict1 = {}
	dict1['R'] = 0
	dict1['G'] = 0
	dict1['B'] = 0
	for ele in string:
		dict1[ele] += 1
	print len1 - max(dict1.values())