n,k = map(int,raw_input().split())

size = [0]*102
for _ in xrange(n):
	s = raw_input()
	size[len(s)] += 1

ans = len(raw_input())

tot = 0
for i in xrange(ans):
	tot += size[i]

a1 = tot + (tot/k)*5 + 1
a2 = tot + size[ans] -1 + ((tot+size[ans]-1)/k)*5 + 1

print a1,a2