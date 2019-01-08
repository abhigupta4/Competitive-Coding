n = input()

lis = map(int, raw_input().split())

stack1 = []
left_max = []
right_max = [0]*n

for i in xrange(n):
	cur = lis[i]
	while(len(stack1) != 0 and lis[stack1[-1]] <= cur):
		stack1.pop()

	if(len(stack1) == 0):
		left_max.append(-1)
	else:
		left_max.append(stack1[-1]+1)

	stack1.append(i)

# print left_max
stack1 = []
for i in xrange(n):
	index = n-1-i
	cur = lis[index]
	while(len(stack1) != 0 and lis[stack1[-1]] <= cur):
		stack1.pop()

	if(len(stack1) == 0):
		right_max[index] = -1
	else:
		right_max[index] = stack1[-1]+1

	stack1.append(index)

for i in xrange(n):
	print left_max[i]+right_max[i],