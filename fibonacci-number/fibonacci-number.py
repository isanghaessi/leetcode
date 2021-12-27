class Solution:
    dp = {}
    
    def fib(self, n: int) -> int:
        if n < 2:
            
            return n
        if n not in self.dp:
            self.dp[n] = self.fib(n - 2) + self.fib(n - 1)
            
        return self.dp[n]
