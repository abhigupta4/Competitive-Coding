n = input()
row = []
for _ in xrange(n):
	row.append(raw_input())

flag = 0
for i in xrange(n):
	if row[i][:2] == 'OO':
		row[i]= '++' + row[i][2:]
		flag = 1
		break
	elif row[i][3:] == 'OO':
		row[i] = row[i][:3] + '++'
		flag = 1
		break

if not flag :
	print "NO"
else:
	print "YES"
	for ele in row:
		print ele