#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378/

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        ht = self.get_ht(root)
        
        ans = [[] for _ in xrange(ht)]
        
        q = deque([(root,ht-1)])
        
        while(q):
            
            cur = q.popleft()
            ans[cur[1]].append(cur[0].val)
            
            if cur[0].left != None:
                q.append((cur[0].left,cur[1]-1))
            
            if cur[0].right != None:
                q.append((cur[0].right,cur[1]-1))
                
        return ans
    
    def get_ht(self,node):
        if node == None:
            return 0
        
        return 1+ max(self.get_ht(node.left),self.get_ht(node.right))
