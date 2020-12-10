#https://leetcode.com/problems/missing-ranges/

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        lis = []
        nums = [lower-1] + nums + [upper+1]
        for i in range(len(nums)-1):
            temp = self.get_range(nums[i],nums[i+1])
            if len(temp) != 0:
                lis.append(temp)
        
        return lis
            
    def get_range(self, lower, upper):
        if lower+1 == upper-1:
            return str(lower+1)
        elif lower+1 < upper-1:
            return str(lower+1) + "->" + str(upper-1)
        return ""
