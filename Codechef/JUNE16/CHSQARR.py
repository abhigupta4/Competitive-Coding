from collections import deque

def find_sum(i,j,row,col):
	return sum_mat[i][j] - sum_mat[i-row][j] - sum_mat[i][j-col] + sum_mat[i-row][j-col]

n,m = map(int,raw_input().split())
lis = []
for i in xrange(n):
	lis.append(map(int,raw_input().split()))

sum_mat = [[0] *(m+1) for i in xrange(n+1)]
for i in xrange(n):
	for j in xrange(m):
		sum_mat[i+1][j+1] = lis[i][j]+sum_mat[i][j+1] + sum_mat[i+1][j] - sum_mat[i][j]

q = input()
for i in xrange(q):
	row,col = map(int,raw_input().split())
	temp = [[0 for i in xrange(m-col+1)] for j in xrange(n)]
	for j in xrange(n):
		qu = deque()
		for k in xrange(col):
			while(len(qu) and lis[j][k] >= lis[j][qu[-1]]):
				qu.pop()
			qu.append(k)

		for k in xrange(col,m):
			temp[j][k-col] = lis[j][qu[0]]
			while(len(qu) and lis[j][k] >= lis[j][qu[-1]]):
				qu.pop()
			while(len(qu) and qu[0] <= k-col):
				qu.popleft()
			qu.append(k)
		temp[j][k-col+1] = lis[j][qu[0]]
	ans = 10**15
	for j in xrange(m-col+1):
		qu2 = deque()
		for k in xrange(row):
			while(len(qu2) and temp[k][j] >= temp[qu2[-1]][j]):
				qu2.pop()
			qu2.append(k)

		ans = min(ans,(temp[qu2[0]][j]*row*col)-find_sum(row,j+col,row,col))
		for k in xrange(row,n):
			while(len(qu2) and temp[k][j] >= temp[qu2[-1]][j]):
				qu2.pop()
			while(len(qu2) and qu2[0] <= k-row):
				qu2.popleft()
			qu2.append(k)
			ans = min(ans,(temp[qu2[0]][j]*row*col)-find_sum(k+1,j+col,row,col))
	print ans