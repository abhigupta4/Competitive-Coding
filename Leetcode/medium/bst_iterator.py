#https://leetcode.com/problems/binary-search-tree-iterator/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.dfs(root, None)
        
        self.set = set()
        self.cur = root
        while(self.cur.left != None):
            self.cur = self.cur.left
    
    def dfs(self, node:TreeNode, par: TreeNode):
        if (node == None):
            return
        
        node.par = par
        self.dfs(node.left, node)
        self.dfs(node.right, node)
        

    def next(self) -> int:
        temp = self.cur
        self.set.add(temp.val)
        print(temp.val)
        while (self.cur != None):
            if (self.cur.left != None and self.cur.left.val not in self.set):
                self.cur = self.cur.left
            elif (self.cur.val not in self.set):
                break
            elif (self.cur.right != None and self.cur.right.val not in self.set):
                self.cur = self.cur.right
            else:
                self.cur = self.cur.par
        
        return temp.val
        
    def hasNext(self) -> bool:
        if self.cur != None:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
