def getsum(index):
	sum1 = 0
	while index > 0:
		sum1 += BIT[index] 
		index -= index & (-index)

	return sum1

def updateBIT(n,index,val):
	while(index <= n):
		BIT[index] += val
		index += index & (-index)

def updateR(n,start,end,val):
	updateBIT(n,start,val)
	updateBIT(n,end+1,-val)

def cons(n):
	for i in xrange(n):
		updateBIT(n,i,list1[i])

BIT = [0] * (10**6 + 2)
list1 = [0] * (10**6 + 2)
# n,q = map(int,raw_input().split())
# for i in xrange(q):
# 	arr = raw_input().split()
# 	if arr[0] == 'find':
# 		print (getsum(int(arr[2]))-getsum(int(arr[1])-1))
# 	else:
# 		updateBIT(n,int(arr[1]),int(arr[2]))

while True:
	print "Enter three values"
	a,b,c = map(int,raw_input().split())
	updateR(10,a,b,c)
	# elif a == 'u':
	# 	updateBIT(10,b,c)
	print BIT[:11]
	print "enter query index"
	print getsum(input())