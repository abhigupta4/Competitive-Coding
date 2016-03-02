for _ in range(input()):
	n = input()
	if n < 7:
		print "-1"
	else:
		print n
		print "1 2"
		print "2 3"
		print "3 4"
		print "4 5"
		print "2 6"
		print "4 6"
		print "6 7"
		temp = n - 7
		start = 8
		while(temp > 0):
			print str(start) + " 2"
			temp -= 1
			start += 1
		print 3	