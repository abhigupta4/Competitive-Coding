def hangover(value):
	count = 1
	sum = 0.50
	while (sum < value):
		count += 1
		sum += (1 / float(count + 1))
	return count 

input = float(raw_input())
while (input != 0.00):
	print str(hangover(input)) + " card(s)"
	input  = float(raw_input())
