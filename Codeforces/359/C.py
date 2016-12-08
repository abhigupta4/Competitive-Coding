from itertools import permutations

n,m = map(int,raw_input().split())

def digits(n):
	if n == 0:
		return 1
	c = 0
	while n:
		c += 1
		n /= 7
	return c

ans = 0
l1 = digits(n-1)
l2 = digits(m-1)
for s in permutations('0123456',l1+l2):
	s = ''.join(s)
	if int(s[:l1],7) < n and int(s[l1:],7) < m:
		ans += 1

print ans 