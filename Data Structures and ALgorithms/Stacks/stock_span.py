'''
Input:
2
7
100 80 60 70 60 75 85
6
10 4 5 90 120 80

Output:
1 1 1 2 1 4 6
1 1 2 4 5 1'''

t = input()

for _ in range(int(t)):
    n = int(input())
    lis = list(map(int,input().split()))
    ans = [0]*n
    temp = []
    for i in range(n):
        idx = n-i-1
        while(temp and lis[temp[-1]] < lis[idx]):
            ans[temp[-1]] = temp[-1]-idx
            temp.pop()
        
        temp.append(idx)
        
    while(temp):
        ans[temp[-1]] = temp[-1]+1
        temp.pop()
    print(ans)