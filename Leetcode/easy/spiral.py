#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3557/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[-1]*n for _ in range(n)]
        
        left = 0
        right = n-1
        top = 0
        down = n-1
        
        
        cur = 1
        while(cur <= n**2):
            for i in range(left, right+1):
                ans[top][i] = cur
                cur += 1

            for j in range(top+1, down+1):
                ans[j][right] = cur
                cur += 1

            for k in range(right-1,left-1,-1):
                ans[down][k] = cur
                cur += 1

            for l in range(down-1, top,-1):
                ans[l][left] = cur
                cur += 1

            top += 1
            down -= 1
            left += 1
            right -= 1
        
        return ans
