import math
def prime(n):
	if (n == 2):
		return 0
	for i in range(3,10):
		if (n % i) == 0:
			return i

	return 0

print "Case #1:"
count = 0
poss = (2**15 +1)
while True:
	if count == 50:
		break
	flag = 0
	binary = bin(poss)[2:]
	list1 = ''
	poss += 2
	for check in range(2,11):
		temp = prime(int(binary	,check))
		if temp:
			list1 += ' ' + str(temp)
		else:
			flag = 1
			break
	if flag:
		continue
	print str(binary) + list1 
	count += 1