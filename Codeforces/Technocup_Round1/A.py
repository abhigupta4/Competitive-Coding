import sys
sys.setrecursionlimit(10**7)

def dfs(nu,par):
	global b,di	
	if int(nu) > int(b):
		return 0
	if nu not in di:
		if nu == b:
			return 1
		else:
			if dfs(str(int(nu)*2),nu):
				di[str(int(nu)*2)] = nu				
				return 1
			elif dfs(nu+'1',nu):
				di[nu+'1'] = nu
				return 1
			else:
				return 0
	else:
		return 0

di = {}
a,b = raw_input().split()
if dfs(a,-1):
	count = 0
	lis = []
	lis.append(b)
	while(b !=  a):
		b = di[b]
		count += 1
		lis.append(b)

	print 'YES'
	print count+1
	for ele in lis[::-1]:
		print ele,

else:
	print 'NO'