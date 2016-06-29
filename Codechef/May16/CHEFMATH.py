mod1 = 10**9 + 7

def gen(X,K,cur_ele,cur_sum,lis):
  global dict1
  # print X,K,cur_ele,cur_sum,lis
  if cur_ele > 0:
    t = (cur_sum,cur_ele)
    if t in dict1:
      dict1[t] += 1%mod1
    else:
      dict1[t] = 1
    if cur_ele >= K:
      return

  for ele in list1:
    if ele + cur_sum > X:
      return
    else:
      temp = lis+[ele]
      temp.sort()
      if tuple(temp) not in memo[cur_ele]:
        memo[cur_ele][tuple(temp)] = 1
        gen(X,K,cur_ele + 1,cur_sum+ele,lis + [ele])

list1 = [1,2]
val = 3
while val <= 10**9:
  list1.append(val)
  val = list1[-1] + list1[-2]  
memo = [{} for i in xrange(10+1)]
dict1 = {}
gen(100,4,0,0,[])
flag = 0
for _ in xrange(input()):
  X,K = map(int,raw_input().split())
  if K > 4 and X < 101 and flag != 1:
    memo = [{} for i in xrange(10+1)]
    dict1 = {}
    gen(101,10,0,0,[])
    flag = 1
  if (X,K) in dict1:
    print dict1[(X,K)]%mod1
  else:
    print 0
# print memo
# print dict1