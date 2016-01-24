def gcd2(a, b):
	if( b == 0):
		return a
	else:
		return gcd2(b, a%b)
for _ in range(input()):
	A,B = map(int,raw_input().split())
	print gcd2(B,A)

#DONE