for _ in xrange(input()):
	a = raw_input()
	b = raw_input()
	dict1 = {}
	dict1['0'] = 0
	dict1['1'] = 0
	dict2 = {}
	dict2['0'] = 0
	dict2['1'] = 0
	for i in xrange(len(a)):
		dict1[a[i]] += 1
		if a[i] != b[i]:
			dict2[a[i]] += 1
	if a == b:
		print "Lucky Chef"
		print 0
	else:
		if dict1['0'] == 0 or dict1['1'] == 0:
			print "Unlucky Chef"
		else:
			print "Lucky Chef"
			print max(dict2['0'],dict2['1'])
