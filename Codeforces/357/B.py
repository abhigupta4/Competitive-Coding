f = 1234567
s = 123456
t = 1234

n = input()
flag = 0
for i in xrange(1000):
	if flag:
		break
	if i*f > n:
		break
		
	rem = n - f*i
	j = 0
	while(j*s <= rem):
		if (rem - j*s)% t == 0:
			flag = 1
			break
		j += 1

if flag:
	print 'YES'
else:
	print 'NO'