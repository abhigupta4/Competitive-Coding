for _ in range(input()):
	row, col = map(int, raw_input().split())
	row_ele = []
	row_info = {}
	col_info = {}

	for i in range(row):
		row_ele.append(map(int, raw_input().split()))
		for j in range(col):
			ele = row_ele[i][j]
			if ele in row_info:
				if i in row_info[ele]:
					row_info[ele][i] += 1
				else:
					row_info[ele][i] = 1
			else:
				row_info[ele] = {}
				row_info[ele][i] = 1

			if ele in col_info:
				if j in col_info[ele]:
					col_info[ele][j] += 1
				else:
					col_info[ele][j] = 1
			else:
				col_info[ele] = {}
				col_info[ele][j] = 1

	max1 = 0
	for elem in row_info.keys():
		max_row = 0
		max_col = 0
		for dc,row1 in row_info[elem].iteritems():
			if row1 > max_row:
				max_row = row1
		for dc,col1 in col_info[elem].iteritems():
			if col1 > max_col:
				max_col = col1

		flag = 0
		for k,v in row_info[elem].iteritems():
			if v == max_row:
				for j,l in col_info[elem].iteritems():
					if l == max_col:
						if row_ele[k][j] != elem:
							flag = 1
							break
				if flag == 1:
					break

		if flag == 0:
			max_row -= 1
		if (max_row + max_col) > max1:
			max1 = max_row + max_col

	print max1

#DONE