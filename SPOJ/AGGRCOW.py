def check(x,pos,N,C):
	last_posi = pos[0]
	cow_placed = 1
	n = 1
	while( n < N):
		if (pos[n] - last_posi) >= x:
			cow_placed += 1
			last_posi = pos[n]
		if (cow_placed == C):
			return 1
		n += 1
	return 0
for _ in range(input()):
	N,C = map(int, raw_input().split())
	pos = []
	for _ in range(N):
		posi = int(raw_input())
		pos.append(posi)
	# N = 5
	# C = 3
	# pos = [1,2,8,4,9]
	pos.sort()

	start = 0
	end = pos[N - 1] - pos[0] + 1
	while ((end - start) > 1):
		mid = (start + end) / 2
		check_mid = check(mid,pos,N,C) 
		#print "mid is" + str(mid) + "ans is" + str(check_mid)
		if ((check_mid) == 1):
			start = mid
		elif ((check_mid) == 0):
			end = mid

	print start

#DONE
