#AC
for _ in xrange(input()):
	act,org  = raw_input().split()
	sum1 = 0
	for __ in xrange(int(act)):
		li = raw_input().split()
		if li[0] == 'CONTEST_WON':
			sum1 += 300
			sum1 += max(20-int(li[1]),0)
		elif li[0] == 'TOP_CONTRIBUTOR':
			sum1 += 300
		elif li[0] == 'BUG_FOUND':
			sum1 += int(li[1])
		elif li[0] == 'CONTEST_HOSTED':
			sum1 += 50

	if org == 'INDIAN':
		print sum1/200
	else:
		print sum1/400