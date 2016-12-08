n = input()
lis = map(int,raw_input().split())
lis.sort()

cur = 1
for i in xrange(n):
	if lis[i] > cur:
		lis[i] = cur
		cur += 1
	elif lis[i] == cur:
		cur += 1

print lis[-1]+1