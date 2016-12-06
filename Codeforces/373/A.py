n = input()
lis = map(int,raw_input().split())
if n == 1:
	if lis[0] == 0:
		print 'UP'
	else:
		print -1
else:
	if lis[-1] == 15:
		print 'DOWN'
	else:
		if lis[-1] > lis[-2]:
			print 'UP'
		else:
			print 'DOWN'