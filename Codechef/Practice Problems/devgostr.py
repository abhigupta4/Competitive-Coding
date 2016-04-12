def string_generate(prefix,k,len1):
	temp = set()
	if k < 0:
		return
	d = 1
	if two:
		two_arr[len1 - k].append(prefix)
	else:
		three_arr[len1-k].append(prefix)
	while(len1 - k - 2*d) >= 0:
		if prefix[len1 - k - d] == prefix[len1 - k -2*d]:
			temp.add(prefix[len1 - k - d])
		d += 1

	for ele in char_set - temp:
		string_generate(prefix + ele,k-1,len1)

def hamming(str1,str2,n,K):
	count = 0
	for i in xrange(n):
		if str1[i] != str2[i]:
			count += 1
		if count > K:
			return 0
	return 1

char_set = set(['a','b'])
two_arr = [[] for _ in xrange(9)]
two = 1
string_generate('',8,8)
two = 0
char_set = set(['a','b','c'])
three_arr = [[] for _ in xrange(27)]
string_generate('',26,26)
# print len(three_arr[26])

for _ in range(input()):
	A,K = map(int, raw_input().split())
	string = raw_input()
	len1 = len(string)
	if A == 1:
		if len1 > 2:
			print 0
		else:
			print 1
	elif A == 2:
		if len1 > 8:
			print 0
		else:
			count1 = 0
			for ele in two_arr[len1]:
				if hamming(ele,string,len1,K):
					count1 += 1
			print count1
	elif A == 3:
		if len1 > 26:
			print 0
		else:
			my_count = 0
			for ele in three_arr[len1]:
				if hamming(ele,string,len1,K):
					my_count += 1
			print my_count

	# print len(three_arr[26])
