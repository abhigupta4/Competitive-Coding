#AC
def ch_time(time,min1,n,wood):
	sum1 = 0
	for i in xrange(n):
		temp = start[i] + time*growth[i]
		if (temp) >= min1:
			sum1 += temp
			if sum1 >= wood:
				return 1
	return 0

n,wood,min1 = map(int,raw_input().split())

start = []
growth = []
for _ in xrange(n):
	a,b = map(int,raw_input().split())
	start.append(a)
	growth.append(b)

low = 0
end = 10**19
save = 0
while(low<=end):
	mid = (low+end)/2
	if ch_time(mid,min1,n,wood) == 1:
		save = mid
		end = mid-1
	else:
		low = mid+1
print save