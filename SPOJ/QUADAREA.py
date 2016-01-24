import math
for _ in range(input()):
	sides = map(float,raw_input().split())
	semi = sum(sides) / 2.00
	prod = 1
	for side in sides:
		prod *= (semi - side)
	print math.sqrt(prod)

#DONE