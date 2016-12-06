class seg:
	def __init__(self,pre,suff,tot,seg1):
		self.suff = suff
		self.pre = pre
		self.tot = tot
		self.seg1 = seg1

a = seg(0,0,0,0)
st = [a]*(5*10**5)

def comb(a,b):
	c = seg(0,0,0,0)
	c.pre = max(a.pre,a.tot + b.pre)
	c.suff = max(b.suff,a.suff+b.tot)
	c.tot = a.tot + b.tot
	c.seg1 = max(a.seg1,b.seg1,a.suff+b.pre)
	return c

def build(start,end,node):
	if start == end:
		yo = lis[start]
		st[node] = seg(yo,yo,yo,yo)
		return
	le = 2*node+1
	ri = 2*node+2
	mid = (start+end)/2
	build(start,mid,le)
	build(mid+1,end,ri)
	st[node] = comb(st[le],st[ri])


def update(start,end,node,pos):
	if start == end:
		yo = -(10**15)
		st[node] = seg(yo,yo,yo,yo)
		return
	mid = (start+end)/2
	le = 2*node+1
	ri = 2*node+2
	if pos <= mid:
		update(start,mid,le,pos)
	else:
		update(mid+1,end,ri,pos)
	
	st[node] = comb(st[le],st[ri])

n = input()
lis = map(int,raw_input().split())
order = map(int,raw_input().split())

build(0,n-1,0)
for ele in order:
	update(0,n-1,0,ele-1)
	print max(0,st[0].seg1)