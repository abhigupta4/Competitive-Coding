import math

def easyprob(number):
	if (number == 1):
		return '2(0)'
	elif (number == 2):
		return '2'
	else:
		power = int(math.log(number , 2))
		if (number - (2 ** power)):
			return easyprob(2 ** power) + '+'+ easyprob(number - (2 ** power))
		else:
			return '2(' + easyprob(power) + ')'
list1 = [137, 1315, 73, 136, 255, 1384, 16385]
for ele in list1:
	print str(ele) + "=" + easyprob(ele)

#DONE