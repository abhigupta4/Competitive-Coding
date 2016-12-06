n = input()
lis = map(int,raw_input().split())
temp = []
lis += [0]
for i in xrange(-1,-n-1,-1):
	temp.append(lis[i]+lis[i-1])

for ele in temp[::-1]:
	print ele,