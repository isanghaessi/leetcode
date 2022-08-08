class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        i = 1
        while i < len(prices):
            current = prices[i] - prices[i - 1]
            if current > 0:
                answer += current
            i += 1
        
        return answer