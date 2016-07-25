import math
test = int(raw_input())
for _ in range(test):
	a,b = map(int, raw_input().split())
	arr = [2,]
	for k in range(3,a,2):
		root1 = math.sqrt(k)
		
	for i in range(a,b):
		root = math.sqrt(i)
		flag = 0
		if i <= 2:
			print 2
		j = 3
		odd = False
		if i % 2 == 1:
			odd = True
		while j <= root:
			if i % j == 0:
				flag = 1				
			j += 2
		if (flag == 0) and odd:
			print i
	print 
		
		
	