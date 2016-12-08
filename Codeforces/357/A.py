n = input()
flag = 0
for _ in xrange(n):
	a,b,c = raw_input().split()
	b = int(b)
	c = int(c)
	if b >= 2400 and c > b:
		flag = 1
		break

if flag:
	print 'YES'
else:
	print 'NO'