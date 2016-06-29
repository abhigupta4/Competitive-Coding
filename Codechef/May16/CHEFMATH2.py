mod1 = 10**9 + 7
def count(n,min1,k):
	global memo
	if k == 1:
		if n in fibo and min1 >= n:
			memo[(n,min1,1)] = 1
		else:
			memo[(n,min1,1)] = 0
		return 
	if (n,min1,k) not in memo:
		memo[n,min1,k] = 0
		for ele in list1:
			if ele > min1:
				break
			count(n-ele,ele,k-1)
		for ele in list1:
			if ele > min1:
				break
			memo[n,min1,k] += memo[n-ele,ele,k-1]%mod1


memo = {}
fibo = {}
fibo[1] = 1
fibo[2] = 1
list1 = [1,2]
val = 3
while val <= 10**9:
  list1.append(val)
  fibo[val] = 1
  val = list1[-1] + list1[-2]

fibo[val] = 1
for _ in xrange(input()):
	a,b = map(int,raw_input().split())
	count(a,a,b)
	print memo[(a,a,b)]%mod1