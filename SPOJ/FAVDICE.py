for _ in range(input()):
	n = input()
	val = 0.0
	for i in range(1,n + 1):
		val += 1.0/i
	print "%.2f" % (val * n)