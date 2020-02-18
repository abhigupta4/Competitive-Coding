n = input()

lis1 = map(int, raw_input().split())
lis2 = map(int, raw_input().split())

lis1.sort()
lis2.sort()

mod = 10 ** 9 + 7
ans = 0
for i in xrange(n):
    ans = (ans + (abs(lis1[i] - lis2[i])) % mod) % mod

print ans