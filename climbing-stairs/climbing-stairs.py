class Solution:
    stairs = {}
    
    def climbStairs(self, n: int) -> int:
        if n < 3:
            
            return n
        if n not in self.stairs:
            self.stairs[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
            
        return self.stairs[n]