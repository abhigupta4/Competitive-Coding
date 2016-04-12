for _ in range(input()):
	n = input()
	list1 = map(int, raw_input().split())
	if list1[1] > list1[0]:
		inc = 1
	else:
		inc = 0
	count = 0
	for i in range(1,n - 1):
		if list1[i + 1] > list1[i]:
			if not inc:
				count += 1
				inc = 1
		else:
			if inc:
				count += 1
				inc = 0
	print count