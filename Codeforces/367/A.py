import math
a,b = map(int,raw_input().split())
n = input()
ans = 10**15
for _ in xrange(n):
	x,y,v = map(int,raw_input().split())
	dist = math.sqrt((a-x)**2 + (b-y)**2)
	time = dist/v
	ans = min(ans,time)

print ans