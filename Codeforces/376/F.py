def calc(nu):
	tot = 0
	end = nu*2
	last = 200100
	i = nu
	for i in xrange(end,last,nu):
		tot += (i-nu)*(lis[i-1]-lis[i-nu-1])
	tot += i*(lis[last]-lis[i-1])
	return tot

n = input()
lis = [0]*(210000)

temp = map(int,raw_input().split())
for ele in temp:
	lis[ele] += 1

for i in xrange(1,201000):
	lis[i] += lis[i-1]

ans = 0
di = {}
for ele in temp:
	if ele not in di:
		ans = max(calc(ele),ans)
		di[ele] = 1
		
print ans