def ii():
	return map(int,raw_input().split())

n,m = ii()
lis = ii()
begin = 0
cum = [0]
for i in xrange(n):
	begin += lis[i]
	cum.append(begin)

tot = 0
for _ in xrange(m):
	l,r = ii()
	if (cum[r]-cum[l-1]) > 0 :
		tot +=  cum[r]-cum[l-1]

print tot