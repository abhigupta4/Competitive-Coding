color = ['C','M','Y']
row,col = map(int,raw_input().split())
r = []
for _ in xrange(row):
	r.append(raw_input())

flag = 0
for row1 in r:
	for ele in row1:
		if ele in color:
			flag = 1
			break

if flag:
	print "#Color"
else:
	print "#Black&White"