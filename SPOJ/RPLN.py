import sys
import math
sys.setrecursionlimit(10**20)
max1 = 10**9 + 7
def cons_tree(low,high,pos):
	if (low == high):
		seg_tree[pos] = list1[low]
		return
	mid = (low + high)/2
	cons_tree(low,mid,2*pos + 1)
	cons_tree(mid+1,high,2*pos + 2)
	seg_tree[pos] = min(seg_tree[2*pos + 1],seg_tree[2*pos + 2])
 
def range_query(qlow,qhigh,low,high,pos):
	if(qlow <=low and qhigh >= high):
		return seg_tree[pos]
	if(qlow > high or qhigh < low):
		return max1
	mid = (low + high)/2
 
	return min(range_query(qlow,qhigh,low,mid,2*pos + 1),range_query(qlow,qhigh,mid+1,high,2*pos + 2))
 
T = input()
for t in xrange(T):
    n,q = map(int, raw_input().split())
    size2 = int(math.ceil(math.log(n,2)))
    list1 = map(int,raw_input().split())
    seg_tree = [0 for _ in xrange(2**(size2+1) - 1)]
    cons_tree(0,n-1,0)
    print "Scenario #" + str(t+1) + ":"
    print 
    for _    in xrange(q):
    	start,end = map(int,raw_input().split())
    	print range_query(start-1,end-1,0,n-1,0) 
