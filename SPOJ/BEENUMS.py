import math
number  = int(raw_input())
while (number != -1):
	check_perfect_square = math.sqrt(((4 * number ) - 1 )/ 3)
	if int(check_perfect_square) - check_perfect_square :
		print "N"
	else:
		if check_perfect_square % 2:
			print "Y"
		else:
			print "N"
	number = int(raw_input())

#DONE