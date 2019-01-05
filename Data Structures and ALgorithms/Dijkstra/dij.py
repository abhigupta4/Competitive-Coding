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