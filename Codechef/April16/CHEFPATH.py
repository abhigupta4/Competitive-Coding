for _ in range(input()):
	a,b = map(int, raw_input().split())
	min1 = min(a,b)
	if min1 % 2:
		if min1 == 1:
			if max(a,b) == 2:
				print "Yes"
			else:
				print "No"
		elif max(a,b) % 2:
			print "No"
		else:
			print "Yes"
	else:
		print "Yes"