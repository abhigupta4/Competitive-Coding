import math
# def silver(numb):
# 	sum = 1
# 	count = 0
# 	if (numb == 1	):
# 		return 0
# 	while numb > sum:
# 		numb -= sum
# 		sum += sum + (2 ** count)
# 		if numb == 0:
# 			return count
# 		count += 1
# 		if numb <= sum:
# 			return count

n = int(raw_input())
while n:
 	print int(math.log(n, 2))
 	n = int(raw_input())

# DONE