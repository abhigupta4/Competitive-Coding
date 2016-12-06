n,m = map(int,raw_input().split())
lis = map(int,raw_input().split())
a1 = n/m
tot = 0
count = [0]*(m+1)
for ele in lis:
	if ele <= m:
		count[ele] += 1

for j in xrange(1,m+1):
	for i in xrange(n):
		if count[j] >= a1:
			break
		if lis[i] > m:
			lis[i] = j
			count[j] += 1
			tot += 1
	for i in xrange(n):
		if count[j] >= a1:
			break
		if count[lis[i]] > a1:
			count[lis[i]] -= 1
			lis[i] = j
			count[j] += 1
			tot += 1

print a1,tot
for ele in lis:
	print ele,