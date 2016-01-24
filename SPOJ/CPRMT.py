def cprmt(a, b):
	b_list = list(b)
	tem = []
	for letter in a:
		if letter in b_list:
			b_list.remove(letter)			
			tem.append(letter)
	tem.sort()
	return ''.join(tem)

while True:
	try:
		first  = raw_input()
		second = raw_input()
		print cprmt(first, second)
	except:
		break

#DONE