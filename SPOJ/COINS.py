def coins_bank(number):
	return (number / 2) + (number / 3) + (number /4)
dict = {}
def bytelandian(coins):
	if(coins == 0):
		return 0
	if coins in dict:
		return dict[coins]
	if coins > coins_bank(coins):
		dict[coins] = coins
		return coins
	else:
		a = bytelandian(coins / 2) 
		dict[coins / 2] = a
		b =  bytelandian(coins / 3) 
		dict[coins /3 ] = b
		c = bytelandian (coins / 4)
		dict[coins /4] = c
		return a + b + c

while True:
	try:
		coin = input()
		byte = bytelandian(coin)
		dict[coin] = byte
		print byte
	except:
		pass