n = input()
s = raw_input()
cur = ''
lis = []
lis1 = []
brack = 0
for i in xrange(n):
	if s[i] == '(':
		lis1.append(cur)
		cur = ''
		brack = 1
		continue
	elif s[i] == ')':
		lis.append(cur)
		brack = 0
		cur = ''
		continue
	elif brack:
		if (s[i] >= 'a' and s[i] <='z') or (s[i] >= 'A' and s[i] <= 'Z'):
			cur += s[i]
		else:
			lis.append(cur)
			cur = ''
	else:
		if (s[i] >= 'a' and s[i] <='z') or (s[i] >= 'A' and s[i] <= 'Z'):
			cur += s[i]
		else:
			lis1.append(cur)
			cur = ''


lis1.append(cur)
m1 = 0
for ele in lis1:
	if len(ele) > m1:
		m1 = len(ele)

m2 = 0
for ele in lis:
	if len(ele):
		m2 += 1

print m1,m2