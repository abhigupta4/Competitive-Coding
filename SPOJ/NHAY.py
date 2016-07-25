def lps(pat,M,lps1):
	len1 = 0
	lps1[0] = 0
	i = 1
	while i < M:
		if pat[i] == pat[len1]:
			len1 += 1
			lps1[i] = len1
			i += 1
		else:
			if len1 != 0:
				len1 = lps1[len1 - 1]
			else:
				lps1[i] = 0
				i += 1

def kmp(pat,text,list1):
	M = len(pat)
	N = len(text)
	lps1 = [0] * M
	j = 0
	lps(pat,M,lps1)		
	i = 0
	while i < N:
		if pat[j] == text[i]:
			i += 1
			j += 1
		if j == M:
			#print i - j
			list1.append(i - j)
			#count += 1
			j = lps1[j - 1]
		elif i < N and pat[j] != text[i]:
			if j != 0:
				j = lps1[j-1]
			else:
				i += 1

while True:
	try:
		M = input()
		pat = raw_input()
		text = raw_input()
		list1 = []
		kmp(pat,text,list1)
		#print count
		for ele in list1:
			print ele
		if len(list1) == 0:
			print 
		print 
	except:
		break

#DONE
