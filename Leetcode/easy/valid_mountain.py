#https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        inc = 1
        
        for i in range(1,len(arr)):
            if i == 1 and arr[1] <= arr[0]:
                return False
            
            if inc == 1:
                if arr[i] == arr[i-1]:
                    return False
                elif arr[i] < arr[i-1]:
                    inc = -1
            else:
                if arr[i] >= arr[i-1]:
                    return False
        
        return True if inc == -1 else False
