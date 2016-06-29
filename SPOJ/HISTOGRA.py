#O(n)
def find_max():
	count = 0
	max_ar = -1
	stack = []
	while (count < len(lis)):
		if (len(stack) == 0 or lis[stack[-1]] <= lis[count]):
			stack.append(count)
			count += 1
		else:
			top = stack.pop()
			if (len(stack) == 0):
				max_ar = max(max_ar,lis[top]*count)
			else:
				max_ar = max(max_ar,lis[top]*(count-stack[-1]-1))

	while (len(stack) != 0):
		top = stack.pop()
		if (len(stack) == 0):
			max_ar = max(max_ar,lis[top]*count)
		else:
			max_ar = max(max_ar,lis[top]*(count-stack[-1]-1))

	return max_ar

while 1:
	lis = map(int,raw_input().split())
	if lis[0] == 0:
		break
	else:
		lis = lis[1:]
		print find_max()