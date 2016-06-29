for _ in xrange(input()):
	n = input()
	lis = map(int,raw_input().split())
	flag = 0
	for i in xrange(n-2):
		if lis[i] == lis[i+1] and lis[i] == lis[i+2]:
			flag = 1
			break

	if flag:
		print "Yes"
	else:
		print "No"