import math
mod1 = 10**9 + 7
def cons_tree(low,high,pos,seg,list1):
	if (low == high):
		seg[pos][0] = list1[low]
		seg[pos][1] = str(list1[low])
		return
	mid = (low + high)/2
	cons_tree(low,mid,2*pos + 1,seg,list1)
	cons_tree(mid+1,high,2*pos + 2,seg,list1)
	seg[pos][0] = (seg[2*pos + 1][0]*seg[2*pos + 2][0])%mod1
	seg[pos][1] = str(int(seg[2*pos+1][1])*int(seg[2*pos+2][1]))[:9]
 
def update(low,high,idx,val,pos,seg):
	if high == low:
		# seg_tree[pos] = list1[idx]
		seg[pos][0] = val
		seg[pos][1] = str(val)
	else:
		mid = (low+high)/2
		if (low <= idx and idx <= mid):
			update(low,mid,idx,val,2*pos + 1,seg)
		else:
			update(mid+1,high,idx,val,2*pos + 2,seg)
		seg[pos][0] = (seg[2*pos + 1][0]*seg[2*pos + 2][0])%mod1
		seg[pos][1] = str(int(seg[2*pos + 1][1])*int(seg[2*pos + 2][1]))[:9]
 
n = input()
lis = map(int,raw_input().split())
seg_tree = []
for i in xrange(1,n+1):
	temp = []
	seg_tree.append([])
	for j in xrange(0,n,i):
		temp.append(lis[j])
	x = math.ceil(math.log(int(math.ceil(float(n)/i)),2))
	size = 2*(2**x) -1
	seg_tree[i-1] = [[0,'0'] for k in xrange(int(size))]
	# print seg_tree[i-1]
	cons_tree(0,int(math.ceil(float(n)/i)) - 1,0,seg_tree[i-1],temp)
 
q = input()
for i in xrange(q):
	t = map(int,raw_input().split())
	if t[0] == 1:
		if t[1] == 1:
			for r in xrange(1,n+1):
				update(0,int(math.ceil(float(n)/r))-1,0,t[2],0,seg_tree[r-1])
		else:
			for r in xrange(1,int(math.sqrt(t[1]))+1):
				if (t[1]-1) % r == 0:
					r_t = (t[1]-1)/r
					update(0,int(math.ceil(float(n)/r))-1,(t[1]-1)/r,t[2],0,seg_tree[r-1])
					update(0,int(math.ceil(float(n)/r_t))-1,(t[1]-1)/r_t,t[2],0,seg_tree[r_t-1])
 
	else:
		a,b = seg_tree[t[1]-1][0]
		print b[0] + ' ' + str(a)