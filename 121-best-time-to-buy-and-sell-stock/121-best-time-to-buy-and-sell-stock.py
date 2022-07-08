class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        minPrice = float('inf')
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                answer = max(answer, price - minPrice)
        
        return answer