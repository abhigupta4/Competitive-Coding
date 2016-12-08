n = input()
g = [[]  for _ in xrange(n+2)]

val = map(int,raw_input().split())
val = [0] + val

for i in xrange(n-1):
	a,b = map(int,raw_input().split())
	g[a].append((i+2,b))

count = 0
stack = [(1,0)]

while stack:
	node,dist = stack.pop()
	if dist > val[node]:
		continue
	count += 1
	for a,b in g[node]:
		stack.append((a,max(0,dist+b)))

print n-count