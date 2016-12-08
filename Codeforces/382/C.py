import math

def ii():
	return map(int,raw_input().split())

n = input()
f1 = 1
f2 = 2
count = 0
while(f2 <= n):
	count += 1
	f1,f2 = f2,f1+f2

print count