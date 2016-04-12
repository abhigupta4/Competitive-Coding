import math
M = [[1,1],[1,0]]
I = [[1,0],[0,1]]
mod = 10**9 + 7

def cons_tree(low,high,pos):
  if (low == high):
    seg_tree[pos] = add(I,fibo(list1[low]))
    return
  mid = (low + high)/2
  cons_tree(low,mid,2*pos + 1)
  cons_tree(mid+1,high,2*pos + 2)
  seg_tree[pos] = mult(seg_tree[2*pos + 1],seg_tree[2*pos + 2])

def range_query(qlow,qhigh,low,high,pos):
  if (qlow <= low and qhigh >= high):
    return seg_tree[pos]
  if (qlow > high or qhigh < low):
    return [[1,0],[0,1]]
  mid = (low + high)/2
  return mult(range_query(qlow,qhigh,low,mid,2*pos + 1),range_query(qlow,qhigh,mid+1,high,2*pos + 2))

def update(low,high,pos,index,val):
  if (low > high or index < low or index > high):
    return
  if (low == high):
    if low == index:
      seg_tree[pos] = add(I,fibo(val))
    return
  mid = (low + high)/2
  update(low,mid,2*pos + 1,index,val)
  update(mid+1,high,2*pos + 2,index,val)
  seg_tree[pos] = mult(seg_tree[2*pos + 1],seg_tree[2*pos + 2])

def add(A,B):
  C = [[0,0],[0,0]]
  C[0][0] = (A[0][0]%mod + B[0][0]%mod)%mod
  C[0][1] = (A[0][1]%mod + B[0][1]%mod)%mod
  C[1][0] = (A[1][0]%mod + B[1][0]%mod)%mod
  C[1][1] = (A[1][1]%mod + B[1][1]%mod)%mod
  return C

def mult(A,B):
  C = [[0,0],[0,0]]
  C[0][0] = (A[0][0]%mod*B[0][0]%mod)%mod + (A[0][1]%mod*B[1][0]%mod)%mod
  C[0][1] = (A[0][0]%mod*B[0][1]%mod)%mod + (A[0][1]%mod*B[1][1]%mod)%mod
  C[1][0] = (A[1][0]%mod*B[0][0]%mod)%mod + (A[1][1]%mod*B[1][0]%mod)%mod
  C[1][1] = (A[1][0]%mod*B[0][1]%mod)%mod + (A[1][1]%mod*B[1][1]%mod)%mod
  return C

def multiply(A,B):
  x = (A[0][0]%mod*B[0][0]%mod)%mod + (A[0][1]%mod*B[1][0]%mod)%mod
  y = (A[0][0]%mod*B[0][1]%mod)%mod + (A[0][1]%mod*B[1][1]%mod)%mod
  z = (A[1][0]%mod*B[0][0]%mod)%mod + (A[1][1]%mod*B[1][0]%mod)%mod
  w = (A[1][0]%mod*B[0][1]%mod)%mod + (A[1][1]%mod*B[1][1]%mod)%mod

  A[0][0] = x;
  A[0][1] = y;
  A[1][0] = z;
  A[1][1] = w;

def power(A,n):
  if (n == 0 or n == 1):
    return 
  power(A,n/2)
  multiply(A,A)
  if (n%2):
    multiply(A,M)

def fibo(n):
  F = [[1,1],[1,0]]
  if n == 0:
    return 0
  power(F,n)
  return F

size, query = map(int, raw_input().split())
list1 = map(int, raw_input().split())
size2 = int(math.ceil(math.log(size,2)))
seg_tree = [[[0,0],[0,0]] for i in range(2**(size2+1) - 1)]
cons_tree(0,size - 1,0)
for i in range(query):
  alpha,start,end = raw_input().split()
  if alpha == 'Q':
    print (range_query(int(start)-1,int(end)-1,0,size-1,0)[0][1])%mod
  else:
    update(0,size-1,0,int(start)-1,int(end))