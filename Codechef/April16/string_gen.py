def string_generate(prefix,k,len1,K,string):
	global my_count
	temp = set()
	d = 1
	if K < 0:
		return
	while(len1 - k - 2*d) >= 0:
		if prefix[len1 - k - d] == prefix[len1 - k -2*d]:
			temp.add(prefix[len1 - k - d])
		d += 1
	if (k == 0):
		# list1.append(prefix)
		my_count += 1
		return
	for ele in char_set - temp:
		if string[len1 - k] == ele: 
			string_generate(prefix + ele,k-1,len1,K,string)
		else:
			string_generate(prefix + ele,k-1,len1,K-1,string)
 
# def hamming(str1,str2,n,K):
# 	count = 0
# 	for i in xrange(n):
# 		if str1[i] != str2[i]:
# 			count += 1
# 		if count > K:
# 			return 0
# 	return 1
 
 
# list1 = []
# char_set = set(['a','b'])
# string_generate('',8,8)
# print list1
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
			my_count = 0
			list1 = []
			char_set = set(['a','b'])
			string_generate('',len1,len1,K,string)
			# for ele in list1:
			# 	if hamming(ele,string,len1,K):
			# 		count1 += 1
			print my_count
	elif A == 3:
		if len1 > 26:
			print 0
		else:
			my_count = 0
			list1 = []
			char_set = set(['a','b','c'])
			string_generate('',len1,len1,K,string)
			# for ele in list1:
			# 	if hamming(ele,string,len1,K):
			# 		count1 += 1
			print my_count 