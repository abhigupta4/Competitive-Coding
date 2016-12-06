n = input()
lis = map(int,raw_input().split())

carry = 0
flag = 0

for i in xrange(n):
	if carry:
		if lis[i] == 0:
			flag = 1
			break
		else:
			lis[i] -= 1
	if lis[i]%2 == 0:
		carry = 0
	else:
		carry = 1

if flag:
	print 'NO'
else:
	if carry:
		print 'NO'
	else:
		print 'YES'