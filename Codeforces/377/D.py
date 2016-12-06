n,m = map(int,raw_input().split())
sched = map(int,raw_input().split())
sched = [0] + sched
req = map(int,raw_input().split())
req = [0] + req


def check(day):
	stack = []
	visi = [0]*(m+1)
	for i in xrange(day,0,-1):
		if sched[i] != 0:
			stack.append(sched[i])
			break

	count = 0
	visi[sched[i]] = 1
	avail = 0
	for j in xrange(i-1,0,-1):
		if sched[j]	 == 0:
			avail += 1
		else:
			if visi[sched[j]] == 1:
				avail += 1
			else:
				stack.append(sched[j])
				visi[sched[j]] = 1

		if len(stack):
			if avail >= req[stack[-1]]:
				avail -= req[stack[-1]]
				stack.pop()
				count += 1

		if count == m:
			return 1
				
	for i in xrange(1,m+1):
		if visi[i] == 0:
			return 0

	if len(stack) == 0:
		return 1
	return 0


low = 1
high = n
ans = -1
while(low <= high):
	mid = (low+high)/2
	if check(mid):
		high = mid-1
		ans = mid
	else:
		low = mid+1

	if low == high:
		if check(low):
			ans = low
		else:
			break

print ans