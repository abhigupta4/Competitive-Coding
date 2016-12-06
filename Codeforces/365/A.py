n = input()
c1 = 0
c2 = 0
for _ in xrange(n):
	a,b = map(int,raw_input().split())
	if a > b:
		c1 += 1
	elif b > a:
		c2 += 1

if c1 > c2:
	print "Mishka"
elif c2 > c1:
	print "Chris"
else:
	print "Friendship is magic!^^"