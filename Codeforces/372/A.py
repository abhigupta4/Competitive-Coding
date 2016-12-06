n,c = map(int,raw_input().split())
count = 0
lis = map(int,raw_input().split())
count = 0
prev = 0
for ele in lis:
	if abs(ele-prev) <= c:
		count += 1
	else:
		count = 1
	prev = ele

print count