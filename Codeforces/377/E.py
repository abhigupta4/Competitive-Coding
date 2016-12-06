n,m = map(int,raw_input().split())
pow1 = map(int,raw_input().split())
sock = map(int,raw_input().split())

comp = 0
req = 0

di = {}
m1 = max(pow1)
for ele in pow1:
	di[ele] = []
for i in xrange(n):
	di[pow1[i]].append(i)

config = []
sock_req = [0]*m
connection = [0]*n

for i in xrange(m):
	config.append((sock[i],i))

c = 0 
u = 0

config.sort()
for val,pos in config:
	div = 0
	while(val > 0):
		if val <= m1:
			if val in di:
				if len(di[val]):
					temp = di[val].pop()
					connection[temp] = pos+1
					sock_req[pos] = div
					c += 1
					u += div
					break

		div += 1
		val = (val+1)/2
		if val == 1:
			if val in di:
				if len(di[val]):
					temp = di[val].pop()
					connection[temp] = pos+1
					sock_req[pos] = div
					c += 1
					u += div
			break
print c,u
for ele in sock_req:
	print ele,
print
for ele in connection:	
	print ele,