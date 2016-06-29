def max_sub_sum(left,right,flag):
	if left == right:
		return lis[left]
	middle = (left+right)/2
	leftans = max_sub_sum(left,middle,flag)
	rightans = max_sub_sum(middle+1,right,flag)
	leftmax = lis[middle]
	rightmax = lis[middle+1]
	temp = 0
	for i in xrange(middle,left -1,-1):
		temp += lis[i]
		leftmax = max(leftmax,temp)

	temp = 0
	for i in xrange(middle+1,right+1):
		temp += lis[i]
		rightmax = max(rightmax,temp)

	if min()
	return max(rightmax+leftmax,leftans,rightans)

for _ in xrange(input()):
	n = input()
	lis = map(int,raw_input().split())
	print max_sub_sum(0,n-1,1)