#https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/562/week-4-october-22nd-october-28th/3507/

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        self.win = [-1] * (n+1)
        
        def check_win(num):
            
            if self.win[num] != -1:
                return self.win[num]
            
            if int(num**0.5)**2 == num:
                self.win[num] = True
                return True
            
            for i in range(1, int(num**0.5)+1):
                
                if (i**2) > num:
                    break
                
                if not (check_win(num-i**2)):
                    print(num-i**2)
                    self.win[num] = True
                    return True
            
            
            self.win[num] = False
            return False
                
        
        return check_win(n)