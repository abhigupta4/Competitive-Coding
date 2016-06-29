prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
mod1 = 10**9 + 7

def recur(factors,k,count,numb,M):
	# print factors
	count_lis[k] += 1
	count_lis[k]%mod1
	if k <= count:
		for i in xrange(numb+1,M+1):
			if len(facts[i]&factors) == 0:
				# print i,numb
				recur(facts[i]|factors,k+1,count,i,M) 

for _ in xrange(input()):
	N,M = map(int,raw_input().split())
	if N > 10 or M > 10:
		print 0
	else:
		facts = [set() for i in xrange(101)]
		for ele in prime:
			if ele > M:
				break
			for i in xrange(ele,M+1,ele):
				facts[i].add(ele)

		count = 0
		for ele in prime:
			if ele > M:
				break
			count += 1

		count_lis = [0 for i in xrange(count+1)]
		for j in xrange(2,M+1):
			recur(facts[j],1,count,j,M)

		ans = 1
		val = N%mod1
		for i in xrange(1,count+1):
			ans += (count_lis[i]%mod1 * val%mod1)%mod1
			val *= (N - i)%mod1
			val % mod1
		print ans