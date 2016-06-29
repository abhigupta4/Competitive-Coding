for _ in xrange(input()):
	e,f = map(int,raw_input().split())
	wt = f-e
	type_coins = input()
	val_list = []
	coin_wt = []
	for _ in xrange(type_coins):
		p,w = map(int, raw_input().split())
		val_list.append(p)
		coin_wt.append(w)
	dp = [10**10 for i in xrange(wt+1)]
	# dp[0] = 0
	for j in xrange(type_coins):
		for i in xrange(1,wt+1):
			if coin_wt[j] == i:
				dp[i] = min(dp[i],val_list[j])
			if coin_wt[j] < i:
				if dp[i-coin_wt[j]] != 10**10:
					dp[i] = min(dp[i],dp[i-coin_wt[j]] + val_list[j])
	if dp[wt] != 10**10:
		print "The minimum amount of money in the piggy-bank is %d." %dp[wt]
	else:
		print "This is impossible." 