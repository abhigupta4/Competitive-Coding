mod = 10**9 + 7
M = [[1,1],[1,0]]
I = [[1,0],[0,1]]
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

while True:
  print fibo(input())