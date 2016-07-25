for _ in range(input()):
	space = raw_input()
	N = int(raw_input())
	sum = 0
	for i in range(N):
		candies = int(raw_input()) 
		sum += candies
	if (sum % N):
		print "NO"
	else:
		print "YES"

#DONE