arr1 = map(int, raw_input().split())
val = min(arr1[0] + arr1[1] + arr1[2] + arr1[3],arr1[0] + arr1[3] + arr1[4],arr1[0] + arr1[5] + arr1[1])

if val < 0:
	print abs(val)
else:
	print 0

#DONE
