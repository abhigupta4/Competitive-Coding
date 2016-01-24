for _ in range(input()):
	a, b = map(int,raw_input().split())
	if(b == a):
		if (b % 2 ) == 0:
			print 2 * b
		else:
			print (2 * b) - 1
	elif(b + 2 == a):
		if (b % 2 ) == 0:
			print (2 * b) + 2 
		else:
			print (2 * b) + 1
	else:
		print "No Number"

