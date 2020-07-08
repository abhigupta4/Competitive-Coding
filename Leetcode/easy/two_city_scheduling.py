#https://leetcode.com/problems/two-city-scheduling/

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        temp = []
        
        for i in xrange(len(costs)):
            temp.append((costs[i][0]-costs[i][1],i))
        
        temp.sort()
        
        ans = 0
        marked = [0]*len(costs)
        
        for i in xrange(len(costs)/2):
            ans += costs[temp[i][1]][0]
            marked[temp[i][1]] = 1
        
        for i in xrange(len(costs)):
            if marked[i] == 0:
                ans += costs[i][1]
            
        return ans
