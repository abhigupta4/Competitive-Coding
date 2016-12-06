def convert(numb):
	t = ''
	for ele in str(numb):
		if int(ele) %2:
			t += '1'
		else:
			t += '0'
	return '0'*(20-len(t)) + t

di = {}

for _ in xrange(input()):
	cur = raw_input().split()
	t = convert(cur[1])
	if cur[0] == '+':
		if t in di:
			di[t] += 1
		else:
			di[t] = 1
	elif cur[0] == '-':
		di[t] -= 1
	else:
		if t in di:
			print di[t]
		else:
			print 0