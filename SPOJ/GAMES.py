def gcd1(a,b):
	while b:
		a,b = b,a%b
	return a

c = 10**4
for _ in xrange(input()):
	n = raw_input()
	flag = 0
	for i in xrange(-1,-1*len(n)-1,-1):
		# print i
		if n[i] == '.':
			flag = 1
			break
	temp = 0
	for j in xrange(len(n)):
		if n[j] != '.':
			temp = temp*10 + int(n[j])
	# print temp
	# print (i+1)
	if flag:
		print pow(10,-1*(i+1))/gcd1(temp,pow(10,-1*(i+1)))
	else:
		print 1