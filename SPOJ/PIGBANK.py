max1 = 10**10
def knap(wt):
	k = [max1] * (wt + 1)
	for n in xrange(0,len(coins)):
		# print w,n
		for w in xrange(1,wt+1):
			if w == coins[n][1]:
				k[w] = min(k[w], coins[n][0])
			elif w > coins[n][1] and k[w-coins[n][1]] != max1:
				k[w] = min(k[w], coins[n][0] + k[w-coins[n][1]])

	if k[wt] != max1:
		print "The minimum amount of money in the piggy-bank is %d." %k[wt]
	else:
		print "This is impossible."

for _ in xrange(input()):
	emp,full = map(int, raw_input().split())
	coins = []
	for c in xrange(input()):
		coins.append(map(int,raw_input().split()))

	knap(full-emp) 