def factorial(n, k):
	if (n == k or n <= 1):
		return 1
	else:
		return  n * factorial(n -1, k)

for _ in range(input()):
	N, K = map(int,raw_input().split())
	print factorial(N - 1,K - 1) / factorial(N - K,1)