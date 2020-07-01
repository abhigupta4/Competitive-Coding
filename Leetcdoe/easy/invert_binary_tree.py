#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3347/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.recur(root)
        return root
        
        
    def recur(self, node):
        if node == None:
            return
        
        
        temp = node.right
        node.right = node.left
        node.left = temp
        self.recur(node.right)
        self.recur(node.left)
        
