li = map(int,raw_input().split())
tot = sum(li)
m1 = 0
di = {}
for ele in li:
	if ele in di:
		di[ele] += 1
	else:
		di[ele] = 1

for ele in li:
	if di[ele] > 1:
		m1 = max(m1,min(3,di[ele])*ele)

print tot-m1