def ii():
	return map(int,raw_input().split())

def check(val):
	time = 0
	for ele in petrol:
		if val >= 2*ele:
			time += ele
		elif val >= ele:
			time += 3*ele - val
		else:
			return 0
		if time > t:
			return 0

	return 1

n,k,s,t = ii()
lis = []
for _ in xrange(n):
	lis.append(ii())

petrol = ii()
petrol.sort()
petrol.append(s-petrol[-1])
for i in xrange(k-1,0,-1):
	petrol[i] -= petrol[i-1]

lo = 1
hi = 10**9 + 2
ans = 10**9 + 1
while (lo <= hi):
	mid = (hi+lo)/2
	if check(mid):
		ans = mid
		hi = mid-1
	else:
		lo = mid+1

cost = 10**9 + 5
for c,p in lis:
	if p >= ans:
		cost = min(cost,c)

if cost == 10**9 + 5:
	print -1
else:
	print cost