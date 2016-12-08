def ii():
	return map(int,raw_input().split())

n,k = ii()
s = raw_input()

g = 0
t = 0
for i in xrange(n):
	if s[i] == 'G':
		g = i
	if s[i] == 'T':
		t = i

flag = 1
for j in xrange(min(g,t),max(g,t),k):
	if s[j] == '#':
		flag = 0
if abs(g-t) < k or abs(g-t)%k != 0: 
	flag = 0
if flag:
	print 'YES'
else:
	print 'NO'