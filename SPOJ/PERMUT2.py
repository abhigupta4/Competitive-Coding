test = int(raw_input())
while (test):
	given_array = map(int,raw_input().split())
	flag = 0
	for i in range(test):
		if (given_array[given_array[i] - 1] != i + 1):
			flag = 1
	if (flag):
		print "not ambiguous"
	else:
		print "ambiguous"
	test = int(raw_input())

#DONE