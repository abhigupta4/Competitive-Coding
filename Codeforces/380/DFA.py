def transition():
	global q
	global l
	if q == 0:
		if l == 'o':
			q = 1
			return ''
		return l
	if q == 1:
		if l == 'o':
			return 'o'
		if l == 'g':
			q = 2
			return ''
		q = 0
		return 'o'+l
	if q == 2:
		if l == 'o':
			q = 3
			return ''
		q = 0
		return 'og'+l
	if q == 3:
		if l == 'o':
			q = 1
			return '***'
		if l == 'g':
			q = 4
			return ''
		q = 0
		return '***'+l
	if q == 4:
		if l == 'o':
			q = 3
			return ''
		q = 0
		return '***g'+l

n = input()
s = raw_input()
q = 0
ans = ''
for l in s+'x':
	ans += transition()
print ans[:-1]