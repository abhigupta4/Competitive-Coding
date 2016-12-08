n,cur = map(int,raw_input().split())
dist = 0
for _ in xrange(n):
	s,val = raw_input().split()
	val = int(val)
	if s == '+':
		cur += val
	else:
		if cur >= val:
			cur -= val
		else:
			dist += 1

print cur,dist