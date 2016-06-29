from heapq import *
def dikshtra(s):
	q,seen = [(0,s)] , set()
	while q:
		cost,v1 = heappop(q)
		if v1 not in seen:
			seen.add(v1)
			sd[v1] = cost
			for c,v2 in g[v1]:
				if v2 not in seen:
					heappush(q,(cost+c,v2))

n = input()
e = input()
t = input()
m = input()
g = [[] for i in xrange(n+1)]
sd = [-1 for i in xrange(n+1)]
for i in xrange(m):
	u,v,w = map(int,raw_input().split())
	g[v].append((w,u))

dikshtra(e)
count = 0
for i in xrange(n):
	if sd[i+1] != -1 and sd[i+1] <= t:
		count += 1	
print count