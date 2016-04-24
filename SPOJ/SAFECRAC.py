mod = 1000000007
list1 = [[] for _ in xrange(10)]
list1[0] = [7]
list1[1] = [2,4]
list1[2] = [1,3,5]
list1[3] = [2,6]
list1[4] = [1,5,7]
list1[5] = [2,4,6,8]
list1[6] = [3,5,9]
list1[7] = [4,8,0]
list1[8] = [5,7,9]
list1[9] = [6,8]
ans = [[0 for _ in xrange(10)] for i in xrange(100001)]
ans[1] = [1] * 10
for ind in xrange(2,100001):
	for cur in xrange(10):
		for ele in list1[cur]:
			ans[ind][cur] += ans[ind-1][ele] % mod

for _ in range(input()):
	print sum(ans[input()]) % mod

#GIVES TLE ON SPOJ