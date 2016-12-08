def ii():
	return map(int,raw_input().split())

n,m = ii()
m1 = 10**9 + 5
for _ in xrange(m):
	l,r = ii()
	m1 = min(r-l+1,m1)

print m1
for i in xrange(n):
	print i%(m1),