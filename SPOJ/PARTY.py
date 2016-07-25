def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K

while True:
  try:
    W,n = map(int, raw_input().split())
    if W == 0 and n == 0:
      break
    wt = []
    val = []
    for _ in range(n): 
      wt_temp,val_temp = map(int, raw_input().split())
      wt.append(wt_temp)
      val.append(val_temp)

    arr = knapSack(W,wt,val,n)
    ans = arr[n][W]
    val = 0
    while arr[n][W - val - 1] == arr[n][W]:
      val += 1
    print str(W - val) + " " + str(ans)
  except:
    pass


