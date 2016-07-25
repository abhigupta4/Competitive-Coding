def die(h,a):
	count = 0
	flag = 0
	while (h > 0 and a > 0):
		if not flag:
			count += 1
			h += 3
			a += 2
			flag = 1
		else:
			if h > 5 and a > 10:
				count += 1
				h -= 5
				a -= 10
				flag = 0
			elif h > 20:
				h -= 20
				a += 5
				count += 1
				flag = 0
			else:
				break
	return count

for _ in xrange(input()):
	h,a = map(int,raw_input().split())
	print die(h,a)