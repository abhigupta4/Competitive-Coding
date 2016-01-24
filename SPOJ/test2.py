Q = int(raw_input())
array = [] 
for _ in range(Q):
	operation = raw_input().split()
	if operation[0] == 'i':
		array.append(int(operation[1]))
	elif operation[0] == "d":
		del array[int(operation[1])]
	elif operation[0] == "u":
		array[int(operation[1]) - 1] = int(operation[2])
	else:
		min = array[int(operation[1]) - 1]
		for posi in range(int(operation[1]) - 1,int(operation[2])):
			if array[posi] < min:
				min = array[posi]
		print min
	