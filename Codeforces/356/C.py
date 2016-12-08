import sys
a = sys.stdout.flush
li = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

co = 0

for i in xrange(len(li)):
	print li[i]
	a()
	s = raw_input()
	a()
	if s == 'yes':
		co += 1
		div1 = li[i]

	if co > 1:
		print 'composite'
		a()
		break

if co == 0:
	print 'prime'
	a()
elif co == 1:
	if div1**2 < 100:
		print div1**2
		a()
		s = raw_input()
		a()
		if s == 'yes':
			print 'composite'
			a()
		else:
			print 'prime'
			a()
	else:
		print 'prime'
		a()
