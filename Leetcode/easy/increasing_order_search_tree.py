#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3553/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.lis = []
        self.recur(root)

        head = TreeNode(self.lis[0])
        cur = head

        for i in range(1, len(self.lis)):
            cur.right = TreeNode()
            cur = cur.right
            cur.val = self.lis[i]

        return head

    def recur(self, node):
        if node.left != None:
            self.recur(node.left)

        self.lis.append(node.val)

        if node.right != None:
            self.recur(node.right)