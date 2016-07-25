for _ in range(input()):
	number = int(raw_input())
	if(number > 4):
		sum = 0
		quotient = 5
		while (number >= quotient):
			sum += number / quotient
			quotient *= 5
		print sum
	else:
		print 0