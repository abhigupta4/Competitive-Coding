s = raw_input()
min1 = 65
di = {}
lis1 = [0]*13
lis2 = [0]*13

for i in xrange(27):
	if s[i] in di:
		break
	else:
		di[s[i]] = i
s += s
bet1 = i-di[s[i]]-1
if bet1 == 0:
	print 'Impossible'
else:
	start = di[s[i]]
	for j in xrange(13-bet1/2-1,13):
		lis1[j] = s[start]
		start += 1

	for j in xrange(12,-1,-1):
		if start == i:
			start += 1
		lis2[j] = s[start]
		start += 1

	for j in xrange(0,13-bet1/2-1):
		lis1[j] = s[start]
		start += 1

	print ''.join(lis1)
	print ''.join(lis2)