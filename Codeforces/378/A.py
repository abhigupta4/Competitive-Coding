s = raw_input()
lis = ['A','E','I','O','U','Y']

count = 0
ans = 1
for ele in s:
	count += 1
	if ele in lis:
		ans = max(ans,count)
		count = 0

ans = max(ans,count+1)
print ans