n = input()
cost = map(int,raw_input().split())
s = []
for _ in xrange(n):
	s.append(raw_input())

dp1 = [-1]*n
dp2 = [-1]*n

dp1[n-1] = 0
dp2[n-1] = cost[n-1]
flag = 0
for i in xrange(n-2,-1,-1):
	flag = 0
	if dp1[i+1] != -1:
		if s[i] <= s[i+1]:
			flag = 1
			dp1[i] = dp1[i+1]

		if s[i][::-1] <= s[i+1]:
			dp2[i] = dp1[i+1]+cost[i]
			flag = 1

	if dp2[i+1] != -1:		
		if s[i] <= s[i+1][::-1]:
			if dp1[i] != -1:
				dp1[i] = min(dp1[i],dp2[i+1])
			else:
				dp1[i] = dp2[i+1]
			flag = 1

		if s[i][::-1] <= s[i+1][::-1]:
			if dp2[i] != -1:
				dp2[i] = min(dp2[i],dp2[i+1]+cost[i])
			else:
				dp2[i] = dp2[i+1]+cost[i]

			flag = 1

	if flag == 0:
		print -1
		break

if flag:
	if dp1[0] == -1:
		print dp2[0]
	elif dp2[0] == -1:
		print dp1[0]
	else:
		print min(dp1[0],dp2[0])