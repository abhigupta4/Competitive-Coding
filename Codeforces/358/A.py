r1 = [0,0,0,0,0]
r2 = [0,0,0,0,0]

n,m = map(int,raw_input().split())

for i in xrange(1,n+1):
	r1[i%5] += 1

for i in xrange(1,m+1):
	r2[i%5] += 1

ans = 0

for i in xrange(1,5):
	ans += r1[i]*r2[5-i]

ans += r1[0]*r2[0]
print ans