list1 = []
N = int(raw_input())
for _ in range(N):
	raw_input()
	temp = map(int, raw_input().split())
	del temp[1]
	list1 += temp
	set1 = set(list1)
print len(set1) - N

#DONE