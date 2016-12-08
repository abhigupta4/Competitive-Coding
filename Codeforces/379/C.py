import bisect

n,m,k = map(int,raw_input().split())
x,money = map(int,raw_input().split())

time = map(int,raw_input().split())
cost = map(int,raw_input().split())
time.append(x)
cost.append(0)

pot = map(int,raw_input().split())
cost2 = map(int,raw_input().split())

ans = n*x

for i in xrange(m+1):
	if cost[i] <= money:
		rem = money - cost[i]
		j = bisect.bisect_right(cost2,rem)
		if j > 0:
			j -= 1
			ans = min(ans,(n-pot[j])*time[i])
		else:
			ans = min(ans,n*time[i])

print ans
