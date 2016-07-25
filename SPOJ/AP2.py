for _ in range(input()):
	third, thirdlast, apsum = map(int,raw_input().split())
	number = (2 * apsum) / (thirdlast + third)
	print number
	diff = (thirdlast - third) / (number - 5)
	first = third - (2 * diff)
	for num in range(number):
		print first + num * diff,

#DONE