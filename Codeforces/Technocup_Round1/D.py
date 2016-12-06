avail = map(int, raw_input().split())
flag = 1
lis = ['S','M', 'L', 'XL', 'XXL', 'XXXL']
di = {}

for i in xrange(6):
	di[lis[i]] = i

n = input()

ans = [0]*n
req = []
for _ in xrange(n):
	req.append(raw_input().split(','))

for i in xrange(n):
	if len(req[i]) == 1:
		if avail[di[req[i][0]]] > 0:
			avail[di[req[i][0]]] -= 1
			ans[i] = req[i][0]
		else:
			flag = 0
			break

if flag:
	for i in xrange(6):
		for j in xrange(n):
			if avail[i] > 0:
				if len(req[j])>1 and ans[j] == 0:
					if di[req[j][1]] == i:
						avail[i] -= 1
						ans[j] = req[j][1]
			else:
				break
		
		for j in xrange(n):
			if avail[i] > 0:
				if len(req[j])>1 and ans[j] == 0:
					if di[req[j][0]] == i:
						avail[i] -= 1
						ans[j] = req[j][0]
			else:
				break

	for ele in ans:
		if ele == 0:
			flag = 0
			print 'NO'
			break

	if flag:
		print 'YES'
		for ele in ans:
			print ele
else:
	print 'NO'

