m = 10**9 + 7
 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
 
def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

for _ in xrange(input()):
	n,k = map(int,raw_input().split())
	lis = map(int,raw_input().split())
	lis.sort()
	i = 0
	j = n-1
	start = 1
	ans = 1
	if lis[-1] 
	while(k and i <= j):

