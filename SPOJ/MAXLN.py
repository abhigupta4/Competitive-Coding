test = int(raw_input())
for num in range(test):
	radius = int(raw_input())
	value = 0.25 + (2 * radius) ** 2 
	print "Case " + str(num + 1 ) + ": " + str("%.2f" % value)
