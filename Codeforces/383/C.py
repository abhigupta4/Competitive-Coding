def ii():
	return map(int,raw_input().split())


def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   lcm = (x*y)//gcd(x,y)
   return lcm

def dfs(node):
	global co
	if node in di:
		return node
	else:
		co += 1
		di1[node] = 1
		di[node] = 1
		return dfs(lis[node])

co = 0
n = input()
di1 = {}
lis = ii()
lis = [0] + lis
nn = []
flag = 1

for i in xrange(1,n+1):
	if i not in di1:
		di = {}
		co = 0
		st = dfs(i)
		if st == i:
			if co %2:
				nn.append(co)
			else:
				nn.append(co/2)
		else:
			flag = 0
			break


ans = 1
if flag:
	for ele in nn:
		ans = lcm(ans,ele)

	print ans
else:
	print -1