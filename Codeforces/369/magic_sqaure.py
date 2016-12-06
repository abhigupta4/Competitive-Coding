n = input()
mat = []
for _ in xrange(n):
	mat.append(map(int,raw_input().split()))

diag1 = 0
diag2 = 0
row = [0] * n
col = [0] * n
miss_row = 0
miss_col = 0

if n == 1:
	print 1
else:
	for i in xrange(n):
		for j in xrange(n):
			if mat[i][j] == 0:
				miss_row = i
				miss_col = j
			row[i] += mat[i][j]
			col[j] += mat[i][j]
			if i == j:
				diag1 += mat[i][j]
			if j == n-i-1:
				diag2 += mat[i][j]

	for i in xrange(n):
		if i != miss_row:
			tot = row[i]
			break
	missing = tot - row[miss_row]
	if missing <= 0:
		print -1
	else:
		row[miss_row] += missing
		col[miss_col] += missing
		if miss_col == miss_row:
			diag1 += missing
		if miss_col == n - miss_row - 1:
			diag2 += missing
		flag = 0
		if diag1 == diag2 and diag1 == tot:
			if row == [tot]*n and col == [tot]*n:
				flag = 1
		if flag :
			print missing
		else:
			print -1