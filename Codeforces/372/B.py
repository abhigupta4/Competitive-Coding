given = raw_input()
len1 = len(given)
di = {}
ques = 0
flag = 0
if len1 >=26:
	for i in xrange(len1-26+1):
		di = {}
		ques = 0
		for j in xrange(i,26+i):
			ele = given[j]
			if ele == '?':
				ques += 1
			elif ele in di:
				break
			else:
				di[ele] = 1
		if len(di) + ques == 26:
			flag = 1
			break


yo = 'ABCDEFGHIJKLMNOPQRZTUVWXYS'
use = ''
for ele in yo:
	if ele not in di:
		use += ele

g = list(given)
beg = 0
if len1 >= 26:
	for j in xrange(i,26+i):
		if g[j] == '?':
			g[j] = use[beg]
			beg += 1
if len1 >= 26:
	for i in xrange(len1):
		if g[i] == '?':
			g[i] = 'A'

if flag:
	print ''.join(g)
else:
	print -1