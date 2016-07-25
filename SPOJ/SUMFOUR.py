li1 = []
li2 = []
li3 = []
li4 = []
n = input()
di = {}
for i in xrange(n):
	a,b,c,d = map(int,raw_input().split())
	li1.append(a)
	li2.append(b)
	li3.append(c)
	li4.append(d)

for i in xrange(n):
	for j in xrange(n):
		if (li1[i] + li2[j]) in di:
			di[li1[i]+li2[j]] += 1
		else:
			di[li1[i]+li2[j]] = 1

count = 0
for i in xrange(n):
	for j in xrange(n):
		if -(li3[i]+li4[j]) in di:
			count += di[-(li3[i]+li4[j])]

print count