def primes_sieve2(limit):
    a = []
    for i in xrange(limit):
    	a.append(True)                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

for _ in range(input()):
	begin,limit = map(int,raw_input().split())
	x = primes_sieve2(limit + 1)    
	while True:
		try:
			prime = x.next()
			if  prime >= begin:
				print prime 
		except:
			break
	print 
