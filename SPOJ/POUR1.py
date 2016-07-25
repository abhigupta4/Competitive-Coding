from collections import deque
def pour(a,b,c):
	if c > max(a,b):
		return -1
	if c == 0:
		return 0
	visi = {}
	dist = {}
	qu = deque()
	qu.append((0,0))
	dist[(0,0)] = 0
	visi[(0,0)] = 1
	while qu:
		cur = qu.popleft()
		lis = gen(cur,a,b)
		for ele in lis:
			f = ele[0]
			s = ele[1]
			if f==c or s==c:
				return (dist[cur]+1)
			if ele not in visi:
				visi[ele] = 1
				dist[ele] = dist[cur] + 1
				qu.append(ele)

	return -1


def gen(cur,a,b):
	li = []
	f = cur[0]
	s = cur[1]
	li.append((0,s))
	li.append((f,0))
	li.append((a,s))
	li.append((f,b))
	if a >= f+s:
		li.append((f+s,0))
	else:
		li.append((a,f+s-a))
	if b >= f+s:
		li.append((0,f+s))
	else:
		li.append((f+s-b,b))
	return li
for _ in xrange(input()):
	a = input()
	b = input()
	c = input()
	print pour(a,b,c)