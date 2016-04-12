for _ in range(input()):
	n = input()
	dict1 = {}
	dict1['hhb'] = 0
	dict1['lxh'] = 1
	x = dict1[raw_input()]
	for _ in xrange(n-1):
		x = x^(dict1[raw_input()])
	if x == 0:
		print 'hhb'
	else:
		print 'lxh'