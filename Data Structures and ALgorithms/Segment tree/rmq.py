#Everything is 1-indexed

import sys
sys.setrecursionlimit(10**5)

def build(idx, start, end):
    if(start == end):
        st[idx] = lis[start]
    else:
        mid = (start+end)/2
        build(2*idx,start,mid)
        build(2*idx+1,mid+1,end)
        st[idx] = min(st[2*idx],st[2*idx+1])
        
        
def upd(idx, start, end, pos, val):
    if(start == end):
        st[idx] = val
        lis[pos] = val
    else:
        mid = (start+end)/2
        if(pos <= mid and pos >= start):
            upd(2*idx, start, mid, pos, val)
        elif (pos>mid and pos<=end):
            upd(2*idx+1, mid+1, end, pos, val)
            
        st[idx] = min(st[2*idx], st[2*idx+1])
        
def query(idx, start, end, l, r):
    if(l>end or r<start):
        return 10**6
    
    if(l<= start and end <= r):
        return st[idx]
    mid = (start+end)/2
    t1 = query(2*idx, start, mid, l, r)
    t2 = query(2*idx+1, mid+1, end,l,r)
    return min(t1,t2)


n,q = map(int, raw_input().split())
lis = [0] + map(int, raw_input().split())
st = [0]*(3*n+10)
build(1,1,n)

for _ in xrange(q):
    a,b,c = raw_input().split()
    if a == 'u':
        upd(1,1,n,int(b),int(c))
    else:
        print query(1,1,n,int(b),int(c))
    
    