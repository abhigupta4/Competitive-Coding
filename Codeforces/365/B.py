n,k = map(int,raw_input().split())
cost = 0
beauty = map(int,raw_input().split())
caps = map(int,raw_input().split())
beauty = [0] + beauty + [0]

di = {}
for ele in caps:
	di[ele] = 1

cost = 0
tot = sum(beauty)
for i in xrange(1,n+1):
	if i in di:
		if i-1 in di:
			cost += beauty[i]*(tot-beauty[i])
		else:
			cost += beauty[i]*(tot-beauty[i]-beauty[i-1])

		tot -= beauty[i]
		
	else:
		cost += beauty[i]*beauty[i+1]


if 1 not in di and n not in di:
	cost += beauty[1]*beauty[n]

print cost 