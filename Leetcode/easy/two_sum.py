#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i,ele in enumerate(nums):
            if (target-ele) in di:
                return [i, di[target-ele]]
            di[ele] = i
