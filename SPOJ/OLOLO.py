pyani = int(raw_input())
dict = {}
check = []
removed = []
for _ in range(pyani):
	current = int(raw_input())
	if current not in check:
		if current not in removed:
			check.append(current)
	else:
		check.remove(current)
		removed.append(current)
print check[0]


