while True:
	string = raw_input().split()
	if string[0] == "*":
		break
	else:
		flag = 1
		match = string[0][0].lower()
		for ele in string:
			if ele[0].lower() != match:
				flag = 0
				break
		if flag:
			print "Y"
		else:
			print "N"

#DONE