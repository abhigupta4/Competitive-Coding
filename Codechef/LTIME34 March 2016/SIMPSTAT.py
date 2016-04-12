for _ in range(input()):
	numb , k = map(int, raw_input().split())
	arr1 = map(int,raw_input().split())
	arr1.sort()
	temp = (float(sum(arr1[k:numb - k]))/ (numb - 2*k))
	print '{0:.6f}'.format(float(temp))

#AC