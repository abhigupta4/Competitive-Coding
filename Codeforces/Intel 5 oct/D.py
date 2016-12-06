from heapq import *

def check(ele):
	if ele in di:
		if di[ele] == 0:
			return 1
		return 0
	return 1


n = input()
lis = map(int,raw_input().split())
di = {}
he = []
for ele in lis:
	di[ele] = 1
	heappush(he,-ele)

flag = 1
while flag:
	flag = 0
	ele = -heappop(he)
	temp = ele
	di[ele] = 0
	ele /= 2
	while(ele != 0):
		if check(ele):
			di[ele] = 1
			heappush(he,-ele)
			flag = 1
			break
		ele /= 2
	if not flag:
		heappush(he,-temp)
for ele in he:
	print -ele,