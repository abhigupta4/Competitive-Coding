n,m,k = map(int,raw_input().split())
col = map(int,raw_input().split())

g = [set() for _ in xrange(n)]

for _ in xrange(m):
	a,b = map(int,raw_input().split())
	a -= 1
	b -= 1
	g[a].add(b)
	g[b].add(a)

ans = 0
visi = [0]*n
for i in xrange(n):
	if visi[i] == 0:
		visi[i] = 1
		tot = 0
		di = {}
		m1 = 0
		stack = [i]
		while stack:
			cur = stack.pop()
			tot += 1
			if col[cur] in di:
				di[col[cur]] += 1
			else:
				di[col[cur]] = 1
			if di[col[cur]] > m1:
				m1 = di[col[cur]]
			for ele in g[cur]:
				if visi[ele] == 0:
					visi[ele] = 1
					stack.append(ele)

		ans += tot - m1

print ans