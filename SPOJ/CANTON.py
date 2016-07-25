for _ in range(input()):
	i = 1
	number = int(raw_input())
	temp = number
	while (number > i):
		number -= i
		i += 1
	print "TERM " + str(temp) + ' IS' ,
	if (i % 2) == 0:
		print str(number) + '/' + str((i + 1) - number)
	else:
		print  str((i + 1) - number) + '/' + str(number)

#DONE