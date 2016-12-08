n = input()
lis = map(int,raw_input().split())
yo = 0
while True:
	yo = 0
	for i in xrange(n-1):
		if lis[i] > lis[i+1]:
			yo = 1
			break
	if not yo:
		break
	beg = 0
	flag = 0
	while(beg < n-1):
		if lis[beg] > lis[beg+1]:
			if not flag:
				start = beg
			flag = 1
			temp = lis[beg]
			lis[beg] = lis[beg+1]
			lis[beg+1] = temp
			beg += 2
		else:
			if flag:
				print start+1,beg
				flag = 0
				break
			flag = 0
			beg += 1
	if flag:
		print start+1,beg
