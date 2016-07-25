test = 1
while True:
	n = input()
	if (n == 0):
		break
	list1 = []
	for _ in range(n):
		list1.append(map(int,raw_input().split()))
	list2 = [[1001 for i in range(5)] for j in range(n + 1)]
	list2[1][2] = list1[0][1]
	for i in range(2,n + 1):
		for j in range(3):
			list2[i][j + 1] = list1[i - 1][j] + min(list2[i - 1][j],list2[i - 1][j + 1],list2[i - 1][j + 2])

	print str(test) + '. ' + str(list2[n][2])
	test += 1

