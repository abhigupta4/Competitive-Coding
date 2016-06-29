def to_base_5(n):
    s=""
    while n:
        s=str(n%5)+s
        n=n/5
    return s
for _ in xrange(input()):
	temp = input()
	if temp == 1:
		print '0'
	else:
		print int(to_base_5(temp - 1))*2