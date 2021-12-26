class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        i = 0
        left = prices[i]
        while i + 1 < len(prices):
            if prices[i] > prices[i + 1]:
                answer += prices[i] - left
                left = prices[i + 1]
            i += 1
        answer += prices[i] - left
            
        return answer