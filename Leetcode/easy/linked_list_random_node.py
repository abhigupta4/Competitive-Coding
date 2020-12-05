#https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3552/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        
        count = 0
        while (head != None):
            head = head.next
            count += 1
        self.count = count
        
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        n = random.randint(1,self.count)
        cur = self.head
        
        while(n-1):
            cur = cur.next
            n -= 1
        
        return(cur.val)
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
