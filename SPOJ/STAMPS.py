test = int(raw_input())
for i in range(test):
	stamps, friends = map(int, raw_input().split())
	stamps_array = map(int, raw_input().split())
	sum = 0
	count = 0
	stamps_array.sort(reverse = True)
	for ele in stamps_array:
		sum += ele
		count += 1
		if (sum >= stamps):
			break
	print "Scenario #" + str(i + 1) + ":"
	if (sum >= stamps):
		print count 
	else:
		print "impossible"
	print
		
#DONE