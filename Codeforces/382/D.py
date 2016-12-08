import math

def prime(n):
	if n == 2 or n == 3:
		return 1
		
	end = int(math.sqrt(n))+2
	for j in xrange(2,end):
		if n%j == 0:
			return 0

	return 1

n = input()
if prime(n):
	print 1
elif n%2 == 0 or prime(n-2):
	print 2
else:
	print 3
