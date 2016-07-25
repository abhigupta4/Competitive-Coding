sum = 0
min = 0
while True:
	try:
		string = raw_input()
		if (string == "EOF"):
			break
		sum += int(string)
		if sum == 100:
			print 100
			break
		if (sum > 100):
			if ( sum - 100) == (100 - min):
				print sum
			elif ( sum - 100) > (100 - min) :
				print min
			else:
				print sum
			break
		min = sum
		raw_input()
	except:
		break