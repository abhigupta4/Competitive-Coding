def danger_number(numb):
	return int(string[0] * 10 ) + int(string[1]) * (10 ** int(string[3]))

def danger(numb):
	if numb == 1:
		return 1
	else:
		return (danger(numb - 1) + 1) % numb + 1

while True:
	num = int(raw_input())
	print danger(num)