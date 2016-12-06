s,e = map(int,raw_input().split())

a = max(s,e)
b = min(s,e)

count = 0
prev = b
cur = b
while(cur < a):
	cur,prev = cur+prev-1,cur
	count += 1

print count+2
