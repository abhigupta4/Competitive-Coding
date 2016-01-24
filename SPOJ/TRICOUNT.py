for _ in range(input()):
	n = int(raw_input())
	sum =  (n ** 2) + ((n - 1) * (n) * (n + 1))/6
	if (n >= 4 ):
		if (n % 2) == 0:
			value = (n - 4)/2
			sum += (value * (value + 1) * ((4 *value) + 11)) / 6
			sum += value + 1
		else:
			value = (n - 3) / 2
			sum += value * (value + 1) * (4 * value  + 5) / 6
	print sum

#DONE