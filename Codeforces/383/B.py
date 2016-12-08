def ii():
	return map(int,raw_input().split())

n,x = ii()
lis = ii()
di1 = {}
co = 0
for ele in lis:
	if ele^x in di1:
		co += di1[ele^x]

	if ele in di1:
		di1[ele] += 1
	else:
		di1[ele] = 1

print co