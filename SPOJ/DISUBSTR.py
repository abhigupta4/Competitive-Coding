def sub(string):
	lis = []
	len1 = len(string)
	for i in xrange(len1):
		lis.append(string[i:])
	lis.sort()
	print lis
	ans = len(lis[0])
	for i in xrange(len1-1):
		ans += len(lis[i+1]) - lcp(lis[i+1],lis[i])
		# print lcp(lis[i+1],lis[i])
	return ans

def lcp(a,b):
	count = 0
	for i in xrange(min(len(a),len(b))):
		if a[i] == b[i]:
			count +=1
		else:
			break
	return count
for _  in xrange(input()):
	print sub(raw_input())