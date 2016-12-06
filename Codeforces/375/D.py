import sys
sys.setrecursionlimit(10**7)

n,m,k = map(int,raw_input().split())
g = []

rx = [0,0,-1,1]
cx = [-1,1,0,0]

def dfs(r,c):
	val = 1
	for i in xrange(4):
		r1 = r+rx[i]
		c1 = c+cx[i]
		if (r1 >= 0 and r1 < n and c1 >=0  and c1 < m):
			if not visi[r1][c1] and g[r1][c1] == '.':
				visi[r1][c1] = 1
				val += dfs(r1,c1)

	return val

def conv(r,c):
	for i in xrange(4):
		r1 = r+rx[i]
		c1 = c+cx[i]
		if (r1 >= 0 and r1 < n and c1 >=0  and c1 < m):
			if g[r1][c1] == '.':
				g[r1][c1] = '*'
				conv(r1,c1)

visi = [[0]*m for _ in xrange(n)]
for _ in xrange(n):
	g.append(list(raw_input()))

comp = 0

for r in xrange(n):
	if not visi[r][0] and g[r][0] == '.':
		visi[r][0] = 1
		dfs(r,0)
	if not visi[r][m-1] and g[r][m-1] == '.':
		visi[r][m-1] = 1
		dfs(r,m-1)

for c in xrange(m):
	if not visi[0][c] and g[0][c] == '.':
		visi[0][c] =  1
		dfs(0,c)
	if not visi[n-1][c] and g[n-1][c] == '.':
		visi[n-1][c] = 1
		dfs(n-1,c) 

use = []
for i in xrange(n):
	for j in xrange(m):
		if not visi[i][j] and g[i][j] == '.':
			visi[i][j] = 1
			comp += 1
			val = dfs(i,j)
			use.append((val,(i,j)))

count = 0
use.sort()
for yo in xrange(comp-k):
	count += use[yo][0]
	r,c = use[yo][1]
	g[r][c] = '*'
	conv(r,c)

print count
for a in xrange(n):
	print ''.join(g[a])