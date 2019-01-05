def make_lps(pat):
	len1 = 0
	M = len(pat)
	lps[0] = 0
	i = 1
	while i < M:
		if pat[i] == pat[len1]:
			len1 += 1
			lps[i] = len1
			i += 1
		else:
			if len1:
				len1 = lps[len1-1]
			else:
				lps[i] = 0
				i += 1

def kmp_search(pat,text):
	M = len(pat)
	N = len(text)
	j = i = 0
	while i < N:
		if pat[j] == text[i]:
			i += 1
			j += 1

		if j == M:
			print "pattern found at i-j"
			j = lps[j-1]
		elif i < N and pat[j] != text[i]:
			if j:
				j = lps[j-1]
			else:
				i += 1

lps = [0 for i in xrange(len(pat))]