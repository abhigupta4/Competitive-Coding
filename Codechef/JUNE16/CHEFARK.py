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

dict1 = {}
for i in xrange(1,10**5 + 1):
	dict1[i] = modinv(i,m)
 
for _ in xrange(input()):
	n,k = map(int,raw_input().split())
	lis = map(int,raw_input().split())
	flag = 0
	for ele in lis:
		if ele == 0:
			flag = 1
			n -= 1
	count = 0
	if n == 0:
		print 1
	else:
		start = 1
		div = 1
		temp = 1
		if flag:
			for i in xrange(0,min(n,k) + 1):
				temp = (temp * (start * dict1[div])%m)%m
				start = (n-i)%m
				div = (i+1)
				count = (count + temp%m)%m
		else:
			if k%2 == 1:
				start = n
			for i in xrange(k%2,min(n,k) + 1,2):
				temp = (temp * (start * div)%m)%m
				start = ((n-i)%m * (n-i-1)%m)%m
				div = (dict1[i+1] * dict1[i+2])%m
				count = (count + temp)%m
		print count %m 