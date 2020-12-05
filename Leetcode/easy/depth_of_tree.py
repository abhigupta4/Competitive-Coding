#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3551/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> int:
            if (root == None):
                return 0
            
            return max(dfs(root.left),dfs(root.right))+1
        
        return dfs(root)
        
