#https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        lis = [0]*60
        
        for ele in time:
            lis[ele%60] += 1
        
        ans = 0
        ans += lis[0]*(lis[0]-1)
        
        for i in range(1,60):
            if (i == 30):
                ans += lis[i]*(lis[i]-1)
            else:
                ans += lis[i]*lis[60-i]
        
        return ans//2
