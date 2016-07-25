import fractions
for _ in range(input()):
	n = input()
	temp = n / 2
	while temp >= 1:
		if fractions.gcd(n,temp) == 1:
			print temp
			break
		temp -= 1

#DONE