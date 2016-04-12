for _ in range(input()):
	a,b,c = map(int, raw_input().split())
	k = input()
	print min(k-1,a) + min(k-1,b) + min(k-1,c) + 1