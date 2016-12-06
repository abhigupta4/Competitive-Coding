def check(val):
	di = {}
	tot = 0
	for i in xrange(val):
		if s[i] not in di:
			di[s[i]] = 1
			tot += 1
		else:
			di[s[i]] += 1

	if tot == count:
		return 1

	for j in xrange(val,n):
		if s[j] not in di or di[s[j]] == 0:
			di[s[j]] = 1
			tot += 1
		else:
			di[s[j]] += 1

		di[s[j-val]] -= 1
		if di[s[j-val]] == 0:
			tot -= 1

		if tot == count:
			return 1


	return 0

n = input()
s = raw_input()
t = {}
count = 0
for ele in s:
	if ele not in t:
		t[ele] = 1
		count += 1

low = count 
high = n
ans = n
while(low <= high):
	mid = (low+high)/2
	if check(mid):
		ans = min(ans,mid)
		high = mid-1
	else:
		low = mid+1

	if low == high:
		if check(low):
			ans = min(ans,low)

		break

print ans