def compute(start,stop,dict2):
	min1 = 0
	for ele in dict2.keys():
		if ele > stop:
			min1 += (ele-stop) * dict2[ele]
		elif ele < start:
			min1 += ele * dict2[ele]
	return min1

for _ in xrange(input()):
	dict1 = {}
	for i in xrange(26):
		dict1[i] = 0

	word,k = raw_input().split()
	k = int(k)
	for ele in word:
		dict1[ord(ele) - 97] += 1

	dict2 = {}

	for i in xrange(26):
		if dict1[i] != 0:
			if dict1[i] in dict2:
				dict2[dict1[i]] += 1
			else:
				dict2[dict1[i]] = 1
	start = 1
	ans = 10**5
	for stop in xrange(k+1,10**5 + 1):
		ans = min(ans,compute(start,stop,dict2))
		start += 1

	print ans