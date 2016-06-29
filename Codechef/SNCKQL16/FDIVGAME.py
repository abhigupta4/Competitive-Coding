win = {}
lose = {}
win2 = {}
lose2 = {}

def wf(nu):
	if nu in [1,2,3,4,5]:
		win[nu] = 1
		return 1
	if nu not in win:
		if lf(nu/2) or lf(nu/3) or lf(nu/4) or lf(nu/5) or lf(nu/6):
			win[nu] = 1
			return 1
		else:
			win[nu] = 0
			return 0
	else:
		return win[nu]

def lf(nu):
	if nu in [1,2,3,4,5]:
		lose[nu] = 0
		return 0
	if nu not in lose:
		if wf(nu/2) and wf(nu/3) and wf(nu/4) and wf(nu/5) and wf(nu/6):
			lose[nu] = 1
			return 1
		else:
			lose[nu] = 0
			return 0
	else:
		return lose[nu]

def force_lose(nu):
	if nu in [2,3,4,5,6]
	if nu in lose2:


# for _ in xrange(input()):
# 	n = input()
# 	lis = map(int,raw_input().split())
while True:
	temp = input()
	print wf(temp)
	print lf(temp)