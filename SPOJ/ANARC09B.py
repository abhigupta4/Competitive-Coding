import fractions	
while True:
	W,H = map(int, raw_input().split())
	if W == 0:
		break
	temp = fractions.gcd(W,H)
	print (W / temp) * (H / temp)

#DONE