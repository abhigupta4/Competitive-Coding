mod = 10**9 + 7
temp = 1
for i in range(1,100000):
    temp = (temp * (i % mod))%mod