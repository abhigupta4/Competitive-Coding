str1 = raw_input()
str2 = raw_input()
len1 = len(str1)
len2 = len(str2)

arr = [[0 for i in xrange(len2 + 1)] for j in xrange(len1 + 1)]
max1 = 0
for i in xrange(len1):
	for j in xrange(len2):
		if str1[i] == str2[j]:
			temp = arr[i+1][j+1] = arr[i][j] + 1
			if temp > max1:
				max1 = temp

print max1