from math import log
def danger_number(string):
	return int(string[0:2]) * (10 ** int(string[3]))

def danger(n):
	return (2*(n - 2 ** (int(log(n, 2))))) + 1

var = int(danger_number(raw_input()))
while var:
	print danger(var)
	var = int(danger_number(raw_input()))

#DONE