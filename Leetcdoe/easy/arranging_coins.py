#https://leetcode.com/explore/featured/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377/

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        cur = 1
        
        while(n >= cur):
            n -= cur
            cur += 1
            ans += 1
        
        return ans
