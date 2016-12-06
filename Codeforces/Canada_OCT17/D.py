from heapq import *

h = []
n = input()
lis = []
mine,ran = map(int,raw_input().split())
for _ in xrange(n-1):
	a,b = map(int,raw_input().split())
	lis.append((a,b))

lis.sort()
tot = 1
ans = 10**6
for i in xrange(n-2,-1,-1):
	if lis[i][0] > mine:
		heappush(h,lis[i][1]-lis[i][0]+1)
		tot += 1
	else:
		break

ans = min(ans,tot)
while(len(h)):
	cost = heappop(h)
	if mine >= cost:
		mine -= cost
		tot -= 1
		for j in xrange(i,-1,-1):
			if lis[j][0] > mine:
				heappush(h,lis[j][1]-lis[j][0]+1)
				tot += 1
			else:
				break

		i = j
		ans = min(ans,tot)
	else:
		break

print ans