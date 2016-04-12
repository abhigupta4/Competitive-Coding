# from itertools import product
# def string_good(str1,len1):
# 	len1 = len(str1)
# 	start = 1
# 	dist = 0
# 	while (start <= len1 - 2):
# 		dist = 1
# 		curr = str1[start]
# 		while((start + dist <= len1 -1) and (start - dist >= 0)):
# 			if str1[start + dist] == curr and str1[start - dist] == curr:
# 				return 0
# 			dist += 1
# 		start += 1
# 	return 1

def hamming(str1,str2,n,K):
	count = 0
	for i in xrange(n):
		if str1[i] != str2[i]:
			count += 1
		if count > K:
			return 0
	return 1

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
			for combo in product('ab',repeat = len1):
				if hamming(''.join(combo),string,len1,K):
					if string_good(''.join(combo)):
						count1 += 1
			print count1
	elif A == 3:
		if len1 > 27:
			print 0
		elif len1 > 8:
			count1 = 0
			for combo in product('abc',repeat = len1):
				if hamming(''.join(combo),string,len1,K):
					if 'a' in ''.join(combo) and 'b' in ''.join(combo) and 'c' in ''.join(combo):
						if string_good(''.join(combo)):
							count1 += 1
			print count1
		else:
			count1 = 0
			for combo in product('abc',repeat = len1):
				if hamming(''.join(combo),string,len1,K):
					if string_good(''.join(combo)):
						count1 += 1
			print count1
