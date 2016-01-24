test = input()
for t in range(test):
	list1 = []
	list1.append(0)
	list1.append(0)
	list1.append(0)
	mons = int(raw_input())
	mons_array = map(int, raw_input().split())
	for i in range(mons):
		list1.append( mons_array[i] + max(list1[i],list1[i + 1]))
	print "Case " + str(t + 1) + ": " + str(max(list1[mons + 1],list1[mons + 2]))

#DONE