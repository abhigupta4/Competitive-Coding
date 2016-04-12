for _ in range(input()):
	numb, K = map(int, raw_input().split())
	A_arr = map(int, raw_input().split())
	B_arr = map(int, raw_input().split())
	maxi = 0
	sum1 = 0
	for i in range(numb):
		B_ele = B_arr[i]
		A_ele = A_arr[i]
		sum1 += B_ele * A_ele
		if abs(B_ele) > abs(maxi):
			maxi = B_ele
	sum1 += abs(maxi) * K
	print sum1

#AC