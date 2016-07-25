for _ in range(input()):
	sum_hotness = 0
	participants = int(raw_input())
	men_hotness = map(int, raw_input().split())
	women_hotness = map(int,raw_input().split())
	men_hotness.sort()
	women_hotness.sort()
	for i in range(participants):
		sum_hotness += men_hotness[i] * women_hotness[i]
	print sum_hotness
