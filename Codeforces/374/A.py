n = input()
s = raw_input()
temp = 0
count = 0
numb = []
for ele in s:
	if ele == 'B':
		temp += 1
	elif temp != 0:
		numb.append(temp)
		temp = 0
		count += 1
	


if temp:
	numb.append(temp)
	count += 1

print count
if count:
	for ele in numb:
		print ele,