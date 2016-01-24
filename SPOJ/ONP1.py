def onp(string):
	temp_list = []
	for ele in string:
		if(ele != ')'):
			temp_list.append(ele)
		else:
			a,b,c = temp_list.pop(),temp_list.pop(),temp_list.pop()
			temp_list.pop()
			temp_list.append(c+a+b)
	return temp_list[0]
	
for _ in range(input()):
	print onp(raw_input())