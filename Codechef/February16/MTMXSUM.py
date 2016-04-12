N = input()

var = 1000000007

A = map(int, raw_input().split())
B = map(int, raw_input().split())

list1 = []
list2 = []

for i in range(N):
	A[i] = A[i] + i + 1
	B[i] = B[i] + i + 1

print ((sum(A) % var) * (sum(B) % var) % var),

for i in range(N - 1):
	list1.append(max(A[i],A[i + 1]))
	list2.append(max(B[i],B[i + 1]))

K = N - 1

while(K > 0):
	# print list1
	# print list2
	# print K
	temp1 = sum(list1[:K]) % var
	temp2 = sum(list2[:K]) % var
	sum1 = (temp1 * temp2) % var
	print sum1,
	for i in range(K - 1):
		list1[i] = max(list1[i],list1[i + 1])
		list2[i] = max(list2[i],list2[i + 1])
	K -= 1