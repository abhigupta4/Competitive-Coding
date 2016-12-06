n = input()
lis = map(int,raw_input().split())
ans = [0]*(10**5 + 10)
q = input()

for ele in lis:
	ans[ele] += 1

for i in xrange(1,10**5 + 5):
	ans[i] += ans[i-1]

for _ in xrange(q):
	t = input()
	if t >= 10**5:
		print n
	else:
		print ans[t]