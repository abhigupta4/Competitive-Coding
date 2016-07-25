#TLE

def getsum(a):
	sum1 = 0
	while(a > 0):
		sum1 += BT[a]
		a -= a&(-a)
	return sum1

def update(n,a,val):
	while (a <= n):
		BT[a] += val
		a += a&(-a)

def upd(n,a,b,val):
	update(n,a,val)
	update(n,b+1,-val)

for _ in xrange(input()):
	n,u = map(int, raw_input().split())
	BT = [0 for _ in xrange(n+1)]
	for i in xrange(u):
		st,end,val = map(int,raw_input().split())
		upd(n,st+1,end+1,val)
	q = input()
	for e in xrange(q):
		print getsum(input() + 1)