def ii():
	return map(int,raw_input().split())

n,n1,n2 = ii()
lis = ii()
lis.sort()
m1 = min(n1,n2)
m2 = max(n1,n2)

ans = 0
temp = 0
for j in xrange(-1,-m1-1,-1):
	temp += lis[j]

ans += float(temp)/m1

temp = 0
for j in xrange(-m1-1,-m1-m2-1,-1):
	temp += lis[j]

ans += float(temp)/m2
print ans