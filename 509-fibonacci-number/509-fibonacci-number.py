class Solution:
    fibDict = {}
    
    def fib(self, n: int) -> int:
        if n < 2:
            
            return n
        
        if n in self.fibDict:
            
            return self.fibDict[n]
        
        self.fibDict[n] = self.fib(n - 2) + self.fib(n - 1)
        
        return self.fibDict[n] 