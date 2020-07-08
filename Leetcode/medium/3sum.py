#https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = {}
        ans = []
        count = {}
        
        lis = []
        
        for ele in nums:
            if ele in count:
                count[ele] += 1
            else:
                count[ele] = 1
                lis.append(ele)
        
        for i in xrange(len(lis)):
            for j in xrange(i+1,len(lis)):
                a = lis[i]
                b = lis[j]
                if -(a+b) in count:
                    if ((a==-(a+b) and count[a] <= 1) or (b==-(a+b) and count[b] <=1)):
                        continue
                    
                    trip = [a,b,-(a+b)]
                    trip.sort()
                    temp[str(trip[0])+'a'+str(trip[1])+'a'+str(trip[2])] = 1
        
        for ele in temp.keys():
            ans.append(map(int,ele.split('a')))
                    
        if 0 in count and count[0] >= 3:
            ans.append([0,0,0])
        
                        
        return ans
