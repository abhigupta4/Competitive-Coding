for _ in range(input()):
	n,k = map(int, raw_input().split())
	mod = 10**9 + 7
	if k == 1:
		if n > 1:
			print 0
		else:
			print 1
	else:
		print ((k%mod) * pow(k-1,n-1,mod))%mod