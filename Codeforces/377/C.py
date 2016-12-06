a,b,c = map(int,raw_input().split())
m1 = max(a,b,c)
ans = max(0,m1-a-1) + max(0,m1-b-1) + max(0,m1-c-1)
print ans 