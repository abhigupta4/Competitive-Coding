def alaska(list1,value):
	flag = 0
	if ((1422 - list1[value - 1]) > 100 ):
		flag = 1
		return "IMPOSSIBLE"
	for i in range(value - 1):
		if (list1[i + 1] - list1[i]) > 200:
			flag = 1
			return "IMPOSSIBLE"
	if flag == 0:
		return "POSSIBLE"

while True:
	value = int(raw_input())
	if value == 0:
		break
	list1 = []
	for _ in range(value):
		list1.append(int(raw_input()))
	list1.sort()
	print alaska(list1,value)

#DONE