a,b = map(int,(raw_input().split()))
while (a + b) != -2:
	boys = max(a, b)
	girls = min(a, b)
	if (girls == boys):
		if(girls):
			print 1
		else:
			print 0
	else:
		if (boys % (girls + 1)):
			print boys/(girls + 1) + 1
		else:
			print boys/(girls + 1)

	a,b = map(int,(raw_input().split()))

#DONE