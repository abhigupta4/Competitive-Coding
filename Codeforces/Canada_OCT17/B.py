di = {}
di['a'] = 4
di['f'] = 1
di['e'] = 2
di['d'] = 3
di['b'] = 5
di['c'] = 6
s = raw_input()

n = int(s[:-1])
n -= 1

char = s[-1]

time = 0
time += (n/4)*16
if n%2:
	time += 7

time += di[char]
print time