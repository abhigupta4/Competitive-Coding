#https://leetcode.com/problems/maximum-width-of-binary-tree/

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        dq = deque([(root,0)])
        
        di = {}
        
        di[-1] = 0
        cur_ht = -1
        
        ans = 1
    
        while(dq):
            node, ht = dq.popleft()
            
            # print node,ht
            if ht != cur_ht:
                if cur_ht not in di:
                    break
                
                if node != None:
                    di[ht] = 1
                    cur_ht = ht
                    dq.append((node.left,ht+1))
                    dq.append((node.right,ht+1))
            else:
                di[ht] += 1
                
                if node == None:
                    dq.append((None,ht+1))
                    dq.append((None,ht+1))
                else:
                    ans = max(ans, di[ht])
                    dq.append((node.left,ht+1))
                    dq.append((node.right,ht+1))
        
        return ans
