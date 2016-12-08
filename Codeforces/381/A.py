def ii():
	return map(int,raw_input().split())

n,a,b,c = ii()
 

if n%4 == 0:
	print 0
elif n%4 == 1:
	print min(c,3*a,b+a)
elif n%4 == 2:
	print min(2*a,b,2*c)
else:
	print min(a,b+c,3*c)