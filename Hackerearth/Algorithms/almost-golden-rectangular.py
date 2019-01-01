n = input()

count = 0

for _ in xrange(n):
    w, h = map(int, raw_input().split())
    a = max(w, h)
    b = min(w, h)
    if float(a) / b >= 1.6 and float(a) / b <= 1.7:
        count += 1

print count