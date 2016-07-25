# your code goes here
def reverse(number):
	sum = 0
	while(number > 0):
		temp =  number % 10
		sum = sum*10 + temp
		number /= 10
	return sum
test = int(raw_input())
for _ in range(test):
	a,b = map(int,raw_input().split())
	print reverse(reverse(a) + reverse(b))

	#print reverse(reverse(a) + reverse(b))
	
		