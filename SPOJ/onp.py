def onp(string):
	temp_list = []
	open_bracket = 0
	position = 0
	for ele in string:
		temp_list[position] = ele
		if (ele == '('):
			open_bracket1 = position
		if (ele == ')'):
			temp_string = temp_list[position - 3] + temp_list[position - 1] + temp_list[position - 2]
			temp_list[open_bracket] = temp_string
			position = open_bracket
		position += 1
	return temp_list
print onp("(a+(b*c))") 


