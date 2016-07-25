n = input()
while True:
	if n == 0 :
		break
	cost = []
	students = []
	cost = map(int,raw_input().split())
	students = map(int, raw_input().split())
	cost.sort()
	students.sort(reverse=True)
	sum = 0
	for i in range(n):
		sum += cost[i] * students[i]
	print sum
	n = input()