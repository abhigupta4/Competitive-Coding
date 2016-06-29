def seq(n):
	if n == '0':
		return '2'
	elif n == '1':
		return '3'
	elif n =='2':
		return '5'
	elif n == '3':
		return '7'
	if int(n) %4 == 0:
		return seq(str((int(n)/4)-1)) + '2'
	elif int(n) %4 == 1:
		return seq(str((int(n)/4)-1)) + '3'
	elif int(n) %4 == 2:
		return seq(str((int(n)/4)-1)) + '5'
	else:
		return seq(str((int(n)/4)-1)) + '7'

for _ in xrange(input()):
	print seq(str(input()-1))