n = input()
di = {}
count = 0
ans = 0
ind = 0
for i in xrange(n):
	a,b,c = map(int,raw_input().split())
	t=[a,b,c]
	t.sort()
	a,b,c = t
	if min(a,b,c) > ans:
		count = 1
		ind = i+1
		ans = min(a,b,c)

	if (b,c) in di:
		di[(b,c)].append((a,i+1))
	else:
		di[(b,c)] = [(a,i+1)]

for b,c in di.keys():
	lis = di[(b,c)]
	# print b,c
	# print lis
	lis.sort()
	if len(lis) > 1:
		if min(b,c,lis[-1][0]+lis[-2][0]) > ans:
			ans = min(b,c,lis[-1][0]+lis[-2][0])
			count = 2
			ind = (lis[-1][1],lis[-2][1])

print count
if count == 1:
	print ind
else:
	print ind[0],ind[1]