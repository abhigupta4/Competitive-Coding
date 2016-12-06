def conv(s):
	tot = 0.0
	temp = ''
	if len(s) > 3 and s[-3] == '.':
		tot += float('0.' + s[-2] + s[-1])
		temp = ''
		for i in xrange(-1,-len(s)-1,-1):
			if i != -1 and i != -2 and s[i] != '.':
				temp = s[i] + temp
	else:
		for i in xrange(-1,-len(s)-1,-1):
			if s[i] != '.':
				temp = s[i] + temp

	tot += float(temp)
	return tot


def conv2(given):
	temp = ''
	if len(given) >= 3 and given[-2] == '.':
		lite = given[:-2]
		for i in xrange(-1,-1-len(lite),-1):
			if (-i-1)%3 == 0 and i != -1:
				temp = '.' + temp
			temp = lite[i] + temp

		if given[-1] == '0':
			return temp

		return temp + given[-2:] + '0'
	elif len(given) >= 3 and given[-3] == '.':
		lite = given[:-3]
		for i in xrange(-1,-1-len(lite),-1):
			if (-i-1)%3 == 0 and i != -1:
				temp = '.'+temp
			temp = lite[i] + temp
		if int(given[-2:]) == 0:
			return temp
		return temp + given[-3:]
	else:
		for i in xrange(-1,-1-len(given),-1):
			if (-i-1)%3 == 0 and i != -1:
				temp = '.' + temp
			temp = given[i] + temp

		return temp

s = raw_input()
cur = ''
tot = 0
for ele in s:
	if ele.islower():
		if len(cur):
			tot += conv(cur)
			cur = ''
	else:
		cur += ele

tot += conv(cur)
print conv2(str(tot))
