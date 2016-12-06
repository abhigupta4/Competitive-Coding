n = input()
di = {}
count = 0
lis = map(int,raw_input().split())
flag = 0
for ele in lis:
	if ele not in di:
		count += 1
		di[ele] = 1
	if count > 3:
		flag = 1
		break

if not flag:
	t = di.keys()
	t.sort()
	if count == 1:
		print "YES"
	elif count == 2:
		print "YES"
	else:
		if (t[2]-t[0])%2:
			print "NO"
		else:
			if t[1] == (t[0]+t[2])/2:
				print "YES"
			else:
				print "NO"
else:
	print "NO"