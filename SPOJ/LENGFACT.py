import math
p = math.pi
e = math.e
def Kamenetsky(n):
	if n < 3:
		return 1
	len1 = math.log10(2*p*n)/2+math.log10(n/e)*n+1
	return int(len1)

for _ in xrange(input()):
	print Kamenetsky(input())