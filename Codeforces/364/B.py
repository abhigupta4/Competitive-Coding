row_mark = 0
col_mark = 0

n,m = map(int,raw_input().split())

row = [0]*(n+3)
col = [0]*(n+3)
begin = n**2

for _ in xrange(m):
	a,b = map(int,raw_input().split())
	flag = 0
	if not row[a] and not col[b]:
		flag = 1

	if not row[a]:
		row_mark += 1		

	if not col[b]:
		col_mark += 1

	if not row[a]:
		row[a] = 1
		begin -= (n-col_mark)

	if not col[b]:
		col[b] = 1
		begin -= (n- row_mark) 

	if flag:
		begin -= 1
		
	print begin,
