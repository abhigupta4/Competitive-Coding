import fractions
def mod(a):
	if a < 0:
		return a * -1
	else:
		return a
for _ in range(input()):
	a, b = map(int, raw_input().split())	
	gcd1 = fractions.gcd(mod(a),mod(b))
	a = a /gcd1
	b = b /gcd1
	if a != 0:
		print mod(a - b)
	else:
		print 1

#DONE