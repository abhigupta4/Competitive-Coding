n,q = map(int,raw_input().split())
lis = map(int,raw_input().split())

min1 = 10**9 + 1
max1 = 0

for ele in lis:
	if ele < min1:
		min1 = ele
	if ele > max1:
		max1 = ele

for _ in xrange(q):
	temp = input()
	if temp <= max1 and temp >= min1:
		print "Yes"
	else:
		print "No"