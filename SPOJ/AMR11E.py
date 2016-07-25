import math
list1 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
list2 = [30,42]

n = 43
for i in range(44,500):
	flag = 0
	for ele1 in list1:
		if ele1 > math.sqrt(i):
			break
		if (i % ele1) == 0:
			flag = 1
			break
	if flag == 0:
		list1.append(i)

while n < 3000:
	count = 0
	for ele in list1:
		if (n % ele) == 0:
			count += 1
		if count >= 3:
			list2.append(n)
			break
	n += 1

for _ in range(input()):
	print list2[input() - 1]

#DONE

