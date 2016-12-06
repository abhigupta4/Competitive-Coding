a,b,c,d,k = map(int,raw_input().split())

if max(a,c) <= min(b,d):
	ans = min(b,d)-max(a,c)+ 1
	if k >= max(a,c) and k <= min(b,d):
		ans -= 1
	print ans
else:
	print 0