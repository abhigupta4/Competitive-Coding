n = input()
s = raw_input()
ans = 10**6
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in xrange(0,n,2):
	if s[i] != 'r':
		count1 += 1
	else:
		count3 += 1
for i in xrange(1,n,2):
	if s[i] != 'b':
		count2 += 1
	else:
		count4 += 1


ans = min(max(count1,count2),max(count3,count4))
print ans