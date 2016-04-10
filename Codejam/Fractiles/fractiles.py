import math
for test in xrange(input()):
	K,C,S = map(int, raw_input().split())
	if K == S:
		list1 = [x + 1 for x in xrange(K)]
		temp = ''
		for ele in list1:
			temp += ' '
			temp += str(ele)
		print "Case #" + str(test + 1) + ":" + temp
	elif int(math.ceil(float(K) / C)) > S:
		print "Case #" + str(test + 1) + ":" + " IMPOSSIBLE"
	else:
		temp = ''