n = input()
lis = map(int,raw_input().split())
tot = sum(lis)
each = (tot*2)/n

pos = [[] for i in xrange(200)]
for i in xrange(n):
	pos[lis[i]].append(i+1)

count = 0
cur = 1
while(count < n/2):
	if each%2 == 0 and cur == each/2:
		while(len(pos[cur])):
			print pos[cur][-1],
			print pos[cur][-2]
			pos[cur].pop()
			pos[cur].pop()
			count += 1

	if len(pos[cur]):
		print pos[cur][-1],
		print pos[each-cur][-1]
		pos[cur].pop()
		pos[each-cur].pop()
		count += 1
	else:
		cur += 1
