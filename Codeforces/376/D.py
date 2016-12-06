n,c = map(int,raw_input().split())

sent = []
words = []

def add(a,b):
	if a > b:
		return
	if a in begin:
		begin[a] += 1
	else:
		begin[a] = 1
	if b in end:
		end[b] += 1
	else:
		end[b] = 1

	return

begin = {}
end = {}

def comp1(fir,sec):
	global c
	l1 = len(fir)
	l2 = len(sec)

	for i in xrange(min(l1,l2)):
		if fir[i] > sec[i]:
			add(0,c-fir[i])
			add(c-sec[i]+1,c-1)
			return 0
		elif fir[i] < sec[i]:
			add(c-sec[i]+1,c-fir[i])
			return 0

	if l1 > l2:
		return 1

	return 0

for _ in xrange(n):
	lis = map(int,raw_input().split())
	sent.append(lis[0])
	words.append(lis[1:])

count = 0
flag = 1


for i in xrange(n-1):
	if comp1(words[i],words[i+1]):
		flag = 0
		break

got = 0
if flag:
	for j in xrange(c):
		if j in begin:
			count += begin[j]

		if count == 0:
			print j
			got = 1
			break

		if j in end:
			count -= end[j]

if not flag:
	print -1
else:
	if not got:
		print -1