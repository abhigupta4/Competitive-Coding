#https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.recur(p, q)

    def recur(self, node1, node2):
        if node1 == None or node2 == None:
            if node1 != node2:
                return False
        
            return True
        
        if node1.val == node2.val:
            return self.recur(node1.left,node2.left) and self.recur(node1.right,node2.right)
        
        return False
        
