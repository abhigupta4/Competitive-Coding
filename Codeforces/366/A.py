lis = ['I hate that ','I love that ']
lis2 = ['I hate it','I love it']

n = input()
temp = ''
flag = 0
start = 0
while(start < n-1):
	temp += lis[flag]
	flag = not flag
	start += 1

temp += lis2[flag]
print temp