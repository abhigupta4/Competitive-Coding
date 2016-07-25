for _ in range(input()):
	blank = raw_input()
	temp = raw_input().split()
	current_value = int(temp[0])
	i = 1;
	while(temp[i] != '='):
		if (temp[i] == '+'):
			current_value += int(temp[i + 1])
		elif(temp[i] == '-'):
			current_value -= int(temp[i + 1])
		elif(temp[i] == '/'):
			current_value /= int(temp[i + 1])
		else:
			current_value *= int(temp[i + 1])
		i += 2
	print current_value


#DONE