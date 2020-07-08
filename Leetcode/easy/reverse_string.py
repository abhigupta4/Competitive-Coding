#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3350/

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return self.rev(s,0,len(s)-1)
    
    def rev(self,s, l,h):
        if h > l:
            s[h],s[l] = s[l],s[h]
            return self.rev(s,l+1,h-1)
        
        else:
            return s
