di = {}
di['L'] = 0
di['R'] = 0
di['U'] = 0
di['D'] = 0
s = raw_input()
if len(s)%2	 == 0:
	for ele in s:
		di[ele] += 1

	fir = abs(di['U']-di['D'])
	sec = abs(di['R']-di['L'])

	print min(fir,sec) + abs(fir-sec)/2 
else:
	print -1