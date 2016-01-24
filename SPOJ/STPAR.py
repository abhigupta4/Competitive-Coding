def stpar(n, arr):
	side = []
	side.append(1001)
	side_count = 1
	truck_done = 1
	for ele in arr:
		if (ele == truck_done):
			truck_done += 1
		elif (side[side_count - 1] == truck_done):
			side.pop()
			side_count -= 1
			truck_done += 1
			while(side[side_count - 1] == truck_done):
				side_count -= 1
				side.pop()
				truck_done += 1
			if (ele > side[side_count - 1]):
				return "no"
			else:
				side.append(ele)
				side_count += 1
		elif (ele > side[side_count - 1]):
				return "no"
		else:
				side.append(ele)
				side_count += 1
	return "yes"

numb = int(raw_input())
while numb:
	array = map(int, raw_input().split())
	print stpar(numb, array)
 	numb = int(raw_input())

#DONE