mod = 10**9 + 7

def cons_tree(low,high,pos):
  if (low == high):
    seg_tree[pos][0].add(list1[low])
    seg_tree[pos][1] = 1
    return
  mid = (low + high)/2
  cons_tree(low,mid,2*pos + 1)
  cons_tree(mid+1,high,2*pos + 2)
  seg_tree[pos][0] = seg_tree[2*pos+1][0] | seg_tree[2*pos + 2][0]
  seg_tree[pos][1] = len(seg_tree[pos][0])

def range_query(qlow,qhigh,low,high,pos):
  if (qlow <= low and qhigh >= high):
    return seg_tree[pos][0]
  if (qlow > high or qhigh < low):
    return set()
  mid = (low + high)/2
  return mult(range_query(qlow,qhigh,low,mid,2*pos + 1),range_query(qlow,qhigh,mid+1,high,2*pos + 2))

size, query = map(int, raw_input().split())
list1 = map(int, raw_input().split())
size2 = int(math.ceil(math.log(size,2)))
seg_tree = [[set(),0] for i in xrange(2**(size2+1) - 1)]
cons_tree(0,size-1,0)
for i in range(query):
  alpha,start,end = raw_input().split()
  if alpha == 'Q':
    print (range_query(int(start)-1,int(end)-1,0,size-1,0)[0][1])%mod
  else:
    update(0,size-1,0,int(start)-1,int(end))