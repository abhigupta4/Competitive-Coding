n = input()
x,y = map(int,raw_input().split())
m1 = 10**12
up = m1
down = 10**12
right = 10**12
left = 10**12
ul = m1
ur = m1
dl = m1
dr = m1
di = {}

for _ in xrange(n):
	s = raw_input().split()
	s[1] = int(s[1])
	s[2] = int(s[2])
	a = s[1]-x
	b = s[2]-y

	di[(a,b)] = s[0]
	if a == 0:
		if b > 0:
			up = min(b,up)
		else:
			down = min(down,abs(b))
	elif b == 0:
		if a > 0:
			right = min(a,right)
		else:
			left = min(abs(a),left)
	elif abs(a) == abs(b):
		if a > 0 and b > 0:
			ur = min(ur,abs(a))
		elif a > 0 and b < 0:
			dr = min(dr,abs(a))
		elif a < 0 and b > 0:
			ul = min(ul,abs(a))
		else:
			dl = min(dl,abs(a))

flag = 0
if up != m1:
	if di[(0,up)] == 'Q' or di[(0,up)] == 'R':
		flag = 1
if down != m1:
	if di[(0,-down)] == 'Q' or di[(0,-down)] == 'R':
		flag = 1
if left != m1:
	if di[(-left,0)] == 'Q' or di[(-left,0)] == 'R':
		flag = 1
if right != m1:
	if di[(right,0)] == 'Q' or di[(right,0)] == 'R':
		flag = 1
if ur != m1:
	t = (ur,ur)
	if di[t] == 'Q' or di[t] == 'B':
		flag = 1
if dr != m1:
	t = (dr,-dr)
	if di[t]== 'Q' or di[t] == 'B':
		flag = 1
if ul != m1:
	t = (-ul,ul)
	if di[t]== 'Q' or di[t] == 'B':
		flag = 1
if dl != m1:
	t = (-dl,-dl)
	if di[t]== 'Q' or di[t] == 'B':
		flag = 1

if flag:
	print 'YES'
else:
	print 'NO'