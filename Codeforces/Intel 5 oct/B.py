t = ['a','e','i','o','u','y']
n = input()
lis = map(int,raw_input().split())
flag = 0
sen = []
for _ in xrange(n):
	sen.append(raw_input())

for i in xrange(n):
	co = 0
	for ele in sen[i]:
		if ele in t:
			co += 1
	if co != lis[i]:
		flag = 1
		break

if flag:
	print 'NO'
else:
	print 'YES'