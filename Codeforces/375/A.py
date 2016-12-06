lis = map(int,raw_input().split())
lis.sort()
ans = -lis[0] + lis[2]
print ans