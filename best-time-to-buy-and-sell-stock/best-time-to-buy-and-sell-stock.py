class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_stock = prices[0]
        for price in prices[1:]:
            min_stock = min(min_stock, price)
            result = max(result, price - min_stock)
        return result