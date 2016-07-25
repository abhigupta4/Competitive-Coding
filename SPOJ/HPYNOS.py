number = int(raw_input())
arr = []
count = 0
while (number != 1):
	arr.append(number)
	count += 1
	temp = 0
	while(number):
		temp += (number % 10) ** 2
		number /= 10
	number = temp
	if number in arr:
		break
if (number == 1):
	print count
else:
	print -1
