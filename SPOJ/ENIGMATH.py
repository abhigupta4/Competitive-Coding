def max(a, b):
	if a > b:
		return [a, b]
	else:
		return [b, a]

def gcd(big, small):
	if (big % small) == 0:
		return small
	else:
		return gcd(small, big % small)

for _ in range(input()):
	a, b = map(int, raw_input().split())
	order = max(a,b)
	gcd_value =  gcd(order[0], order[1])
	print b / gcd_value, a/gcd_value

#DONE