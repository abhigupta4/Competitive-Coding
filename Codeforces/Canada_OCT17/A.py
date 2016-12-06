n = input()
s = raw_input()
count = 0
for ele in s:
	if ele == '<':
		count += 1
	else:	
		break

for ele in s[::-1]:
	if ele == '>':
		count += 1
	else:
		break

print count