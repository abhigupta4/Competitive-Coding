def factorial(number):
	if (number == 1 or number == 0):
		return 1
	else:
		return number * factorial(number - 1)


for _ in range(input()):
	number = int(raw_input())
	print factorial(number)
	