n = input()
l = 0
r = 0
fir = []
sec = []
for _ in xrange(n):
	a,b = map(int,raw_input().split())
	fir.append(a)
	sec.append(b)
	l += a
	r += b

d = abs(l-r)
cur = d
ind = 0
if l > r:
	for i in xrange(n):
		a = fir[i]-sec[i]
		if a > 0:
			if 2*a -d > cur:
				cur = 2*a - d
				ind = i+1
		else:
			if 2*abs(a) + d > cur:
				cur = 2*abs(a)+d
				ind = i+1
elif r > l:
	for i in xrange(n):
		a = sec[i]-fir[i]
		if a > 0:
			if 2*a-d > cur:
				cur = 2*a - d
				ind = i+1
		else:
			if 2*abs(a) + d > cur:
				cur = 2*abs(a) +d
				ind = i+1
else:
	for i in xrange(n):
		a = fir[i]-sec[i]
		if abs(a) > cur:
			cur = abs(a)
			ind = i+1

if i == 0:
	print 0
else:
	print ind