n = input()
s = raw_input()
h,m = s.split(':')
if n == 12:
	if (h) == '00':
		h = '01'
	elif int(h) > 12:
		if h[1] == '0':
			h = '10'
		else:
			h = '0' + h[1]

else:
	if (h) > '23':
		h = '0' + h[1]

if m > '59':
	m = '0' + m[1]

print h + ':' + m