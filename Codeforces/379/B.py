k2,k3,k5,k6 = map(int,raw_input().split())
f1 = min(k2,k5,k6)
k2 -= f1

f2 = min(k2,k3)
ans = f1*256 + f2*32
print ans