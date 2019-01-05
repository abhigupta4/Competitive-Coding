lis = map(int,raw_input().split())
max1 = lis[0]

temp = 0
for ele in lis:
	temp += ele
	if temp > max1:
		max1 = temp
	if temp < 0:
		temp = 0

print temp