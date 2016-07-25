def amuse(n):
	st = ''
	if n == '2':
		return '5'
	if n == '3':
		return '6'
	if int(n) % 2:
		st = amuse(str(int(n)/2)) + '6'
	else:
		st = amuse(str(int(n)/2)) + '5'
	return st

for _ in xrange(input()):
	print amuse(str(input() + 1))