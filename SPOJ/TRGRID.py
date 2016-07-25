def trgrid(c, d):
	if d >= c:
		if c % 2:
			return "R"
		else:
			return "L"
	else:
		if d % 2:
			return "D"
		else:
			return "U"

for _ in range(input()):
	a, b = map(int, raw_input().split())
	print trgrid(a, b)

#DONE