n,k = map(int,raw_input().split())
lis = map(int,raw_input().split())

count = 0
for i in xrange(1,n):
	count += max(lis[i],k-lis[i-1])-lis[i]
	lis[i] = max(lis[i],k-lis[i-1])

print count
for ele in lis:
	print ele,