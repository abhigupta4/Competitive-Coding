for _ in range(input()):
	blank = raw_input()
	array = raw_input().split()
	if (array[0].isdigit() == False):
		(array[0]) = str(int(array[4]) - int(array[2]))
	elif(array[2].isdigit() == False):
		(array[2]) = str(int(array[4]) - int(array[0]))
	else:
		(array[4]) = str(int(array[0]) + int(array[2]))
	print ' '.join(array)
		
#DONE
