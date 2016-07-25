def bin(ele,start,end):
	if ele > list1[end] or ele < list1[start]:
		return 0
	while (end > start):
		mid = (start + end)/2
		if list1[mid] == ele:
			return 1
		elif list1[mid] > ele:
			end = mid
		else:
			start = mid + 1
	return 0
n,k = map(int, raw_input().split())
list1 = map(int, raw_input().split())
list1.sort()
count = 0
for i in xrange(n):
	if bin(list1[i] + k,i+1,n-1):	
		count += 1

print count