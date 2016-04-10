def counting_sheep(n):
	if n == 0:
		return "INSOMNIA"
	occur = set()
	temp = str(n)
	for ele in temp:
		occur.add(ele)
	count = 1
	while (len(occur) != 10):
		count += 1
		temp = n * count
		for ele in str(temp):
			occur.add(ele)
	return count
for i in range(input()):
	N = input()
	if N == 0:
		print "Case #" + str(i + 1) + ": INSOMNIA"
	else:
		print "Case #" + str(i + 1) + ": " + str(counting_sheep(N) * N)