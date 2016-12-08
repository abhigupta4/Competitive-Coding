def ii():
	return map(int,raw_input().split())

r,c = ii()	
g = []
for _ in xrange(r):
	g.append(ii())

count = 0
for row in g:
	for ele in row:
		if ele == 1:
			count += 1

left = [[0]*c for _ in xrange(r)]
up = [[0]*c for _ in xrange(r)]

for i in xrange(r):
	for j in xrange(c):
		if i == 0 and j == 0:
			left[i][j] = g[i][j]
			up[i][j] = g[i][j]
		elif i == 0:
			up[i][j] = g[i][j]
			left[i][j] = g[i][j]|left[i][j-1]
		elif j == 0:
			left[i][j] = g[i][j]
			up[i][j] = g[i][j]|up[i-1][j]

		else:
			left[i][j] = g[i][j]|left[i][j-1]
			up[i][j] = g[i][j]|up[i-1][j]

down = [[0]*c for _ in xrange(r)]
right = [[0]*c for _ in xrange(r)]

for i in xrange(r-1,-1,-1):
	for j in xrange(c-1,-1,-1):
		if i == r-1 and j == c-1:
			down[i][j] = g[i][j]
			right[i][j] = g[i][j]
		elif i == r-1:
			right[i][j] = g[i][j]|right[i][j+1]
			down[i][j] = g[i][j]
		elif j == c-1:
			right[i][j] = g[i][j]
			down[i][j] = down[i+1][j]|g[i][j]
		else:
			right[i][j] = right[i][j+1]|g[i][j]
			down[i][j] = down[i+1][j]|g[i][j]

c1 = 0
for i in xrange(r):
	for j in xrange(c):
		c1 += up[i][j] + down[i][j] + left[i][j] + right[i][j]

print c1 - 4*count