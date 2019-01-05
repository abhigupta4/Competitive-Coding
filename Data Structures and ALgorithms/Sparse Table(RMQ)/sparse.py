#Building is O(nlogn)
#Range queries is O(1)

import math
def preprocess(n):
	for i in xrange(n):
		sparse[i][0] = i
	j = 1
	while(2**j <= n):
		i = 0
		while(i + 2**j -1) < n:
			# print i,j
			if lis[sparse[i][j-1]] < lis[sparse[i+2**(j-1)][j-1]]:
				sparse[i][j] = sparse[i][j-1]
			else:
				sparse[i][j] = sparse[i+ 2**(j-1)][j-1]
			i += 1
		j += 1

def rmq(low,high):
	l = high-low + 1
	k = log(l,2)
	return min(lis[sparse[low][k]],lis[sparse[low+l-2**k][k]])

n = input()
lis = map(int,raw_input().split())

sparse = [[0 for i in xrange(int(math.log(n,2))+1)] for j in xrange(n)]
preprocess(n)
