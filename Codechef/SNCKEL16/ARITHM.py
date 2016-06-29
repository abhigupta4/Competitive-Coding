def arithm(n,c):
	if n == 1:
		return "Yes"
	if (2*c)%n == 0:
		right = (2*c)/n
		flag = 0
		for i in xrange(n-1,right,n-1):
			if (right - i) % 2 == 0:
				return "Yes"
	return "No"
for _ in xrange(input()):
	n,c = map(int,raw_input().split())
	print arithm(n,c)