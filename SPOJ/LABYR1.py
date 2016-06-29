def find_max(i,j,depth,par):
	global max1,node,r,c
	if depth > max1:
		max1 = depth
		node = (i,j)
	for a,b in gen_neigh(i,j,r,c):
		if lab[a][b] == '.' and (a,b) != par:
			find_max(a,b,depth+1,(i,j))

def gen_neigh(a,b,r,c):
	li = []
	if a + 1 <r:
		li.append((a+1,b))
	if b+1<c:
		li.append((a,b+1))
	if a-1>=0:
		li.append((a-1,b))
	if b-1>=0:
		li.append((a,b-1))
	return li

for _ in xrange(input()):
	c,r = map(int,raw_input().split())
	lab = []
	for R in xrange(r):
		lab.append(raw_input())

	max1 = 0
	node = (0,0)
	flag = 0
	for R in xrange(r):
		for C in xrange(c):
			if lab[R][C] == '.':
				find_max(R,C,0,(-1,-1))
				flag = 1
				break
		if flag:
			break
	# print max1
	# print node
	find_max(node[0],node[1],0,(-1,-1))
	print "Maximum rope length is " + str(max1) + '.'